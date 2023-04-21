import logging
import posixpath
import sys
import debug_utils

from unicorn import UcError, UC_HOOK_MEM_UNMAPPED, UC_HOOK_CODE
from unicorn.arm_const import *
from androidemu.emulator import Emulator

# Android Import
from android.Context import Context
from android.ApplicationInfo import ApplicationInfo
from android.PackageManager import PackageManager
from android.PackageInfo import PackageInfo
from android.Signature import Signature
from android.SettingsSecure import SettingsSecure
from android.Location import Location
from android.NetworkCapabilities import NetworkCapabilities
from android.ConnectivityManager import ConnectivityManager

# Java Import
from java.RuntimeException import RuntimeException
from java.File import File
from java.String import String
from java.Thread import Thread
from java.StackTraceElement import StackTraceElement
from java.Method import Method
from java.Constructor import Constructor
from java.AbstractMethod import AbstractMethod
from java.ArtMethod import ArtMethod
from java.Executable import Executable
from java.Class import Class
from java.ClassLoader import ClassLoader
from java.Field import Field
from java.ArtField import ArtField
from java.ZipFile import ZipFile
from java.ZipEntry import ZipEntry

# Snapchat Import
from com.snap.framework.misc.AppContext import AppContext

# Obfuscated Import
from Obfuscated.suks import suks
from Obfuscated.ktb import ktb
from Obfuscated.o import o
from Obfuscated.zvfb import zvfb
from Obfuscated.vug import vug

# Configure logging
logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)7s %(name)34s | %(message)s"
)

logger = logging.getLogger(__name__)

# Initialize emulator
emulator = Emulator(
    vfp_inst_set=True,
    vfs_root=posixpath.join(posixpath.dirname(__file__), "vfs")
)

emulator.load_library("libs/32/libc.so", do_init=True)
lib_module = emulator.load_library("libs/32/libscplugin.so", do_init=True)

# Obfuscated Load Class
emulator.java_classloader.add_class(suks)
emulator.java_classloader.add_class(vug)
emulator.java_classloader.add_class(o)
emulator.java_classloader.add_class(ktb)
emulator.java_classloader.add_class(zvfb)

# Java
emulator.java_classloader.add_class(RuntimeException)
emulator.java_classloader.add_class(File)
emulator.java_classloader.add_class(String)
emulator.java_classloader.add_class(Thread)
emulator.java_classloader.add_class(StackTraceElement)
emulator.java_classloader.add_class(Method)
emulator.java_classloader.add_class(Constructor)
emulator.java_classloader.add_class(AbstractMethod)
emulator.java_classloader.add_class(ArtMethod)
emulator.java_classloader.add_class(Executable)
emulator.java_classloader.add_class(Class)
emulator.java_classloader.add_class(ClassLoader)
emulator.java_classloader.add_class(Field)
emulator.java_classloader.add_class(ArtField)
emulator.java_classloader.add_class(ZipFile)
emulator.java_classloader.add_class(ZipEntry)

# Snapchat
emulator.java_classloader.add_class(AppContext)

# Android
emulator.java_classloader.add_class(Context)
emulator.java_classloader.add_class(ApplicationInfo)
emulator.java_classloader.add_class(PackageManager)
emulator.java_classloader.add_class(PackageInfo)
emulator.java_classloader.add_class(Signature)
emulator.java_classloader.add_class(SettingsSecure)
emulator.java_classloader.add_class(Location)
emulator.java_classloader.add_class(NetworkCapabilities)
emulator.java_classloader.add_class(ConnectivityManager)

# Show loaded modules.
logger.info("Loaded modules:")

for module in emulator.modules:
    logger.info("[0x%x] %s" % (module.base, module.filename))

try:
    emulator.system_properties = {
        'ro.product.model': 'SM-G960N',
        'ro.board.platform': 'aosp-user',
        'ro.build.date': '2021年 03月 18日 星期四 21:05:33 CST',
        'ro.build.date.utc': '1616072733',
        'ro.build.description': 'android_x86-user 7.1.2 N2G48C N975FXXU1ASGO release-keys',
        'ro.build.fingerprint': 'google/android_x86/x86:7.1.2/N2G48C/N975FXXU1ASGO:/release-keys',
        'ro.build.flavor': 'aosp-user',
        'ro.build.id': 'N2G48C',
        'ro.build.product': 'aosp',
        'ro.build.tags': 'release-keys',
        'ro.build.time': '1616073312',
        'ro.build.user': 'build',
        'ro.build.version.security_patch': '2017-10-05',
        'ro.build.display.id': 'N2G48C',
        'ro.build.version.release': '7.1.2',
        'ro.build.version.sdk': '25',
        'ro.build.version.incremental': 'N975FXXU1ASGO',
        'ro.opengles.version': '131072',
        'ro.product.brand': 'google',
        'ro.product.board': '',
        'ro.product.cpu.abi': 'x86',
        'ro.product.cpu.abilist': 'x86,armeabi-v7a,armeabi',
        'ro.product.cpu.abilist32': 'x86,armeabi-v7a,armeabi',
        'ro.product.device': 'aosp',
        'ro.product.name': 'android_x86',
    }
    Signer = vug()
    Signer.b(emulator, 'a', 'a', 'a')
    emulator.call_symbol(lib_module, 'JNI_OnLoad', emulator.java_vm.address_ptr, 0x00)
    emulator.mu.hook_add(UC_HOOK_MEM_UNMAPPED, debug_utils.hook_unmapped)
    print("String length is: %i" % emulator.mu.reg_read(UC_ARM_REG_R0))

except UcError as e:
    print("Exit at %x" % emulator.mu.reg_read(UC_ARM_REG_PC))
    raise