import logging
import posixpath
import sys

from unicorn import *
from unicorn.arm_const import *

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

# Obfuscated Import
from obfuscated.sxhg import sxhg
from obfuscated.t import t
from obfuscated.umuy import umuy
from obfuscated.obl import obl
from obfuscated.turd import turd

# Snapchat Import
from com.snap.framework.misc.AppContext import AppContext

# Xposed Import
# from xposed.dummy.XResourcesSuperClass import XResourcesSuperClass

from androidemu.emulator import Emulator


# Create java class.
from samples import debug_utils
#Configure logging
logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)7s %(name)34s | %(message)s")

logger = logging.getLogger(__name__)

# Initialize emulator
emulator = Emulator(
    vfp_inst_set=True,
    vfs_root=posixpath.join(posixpath.dirname(__file__), "vfs")
)

# Snapchat
emulator.java_classloader.add_class(AppContext)

# Xposed

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

# Obfuscation
emulator.java_classloader.add_class(sxhg)
emulator.java_classloader.add_class(t)
emulator.java_classloader.add_class(umuy)
emulator.java_classloader.add_class(obl)
emulator.java_classloader.add_class(turd)

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

# Load all libraries.
emulator.load_library("libs/libdl.so")
emulator.load_library("libs/libc.so")
emulator.load_library("libs/libstdc++.so")
emulator.load_library("libs/libm.so")
lib_module = emulator.load_library("libs/libscplugin.so")

logger.info("Loaded modules:")
for module in emulator.modules:
    logger.info("=> 0x%08x - %s" % (module.base, module.filename))

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

    # Run JNI_OnLoad.
    emulator.call_symbol(lib_module, 'JNI_OnLoad', emulator.java_vm.address_ptr, 0x00)
    #emulator.mu.hook_add(UC_HOOK_MEM_UNMAPPED, debug_utils.hook_unmapped)
    #emulator.mu.hook_add(UC_HOOK_MEM_WRITE, debug_utils.hook_unmapped)
    #emulator.mu.hook_add(UC_HOOK_MEM_READ, debug_utils.hook_unmapped)
    #   JNI_OnLoad will call 'RegisterNatives'.
    # Do native stuff.
    emulator.call_native(0xCBCBE5D0 + 1)
    for i in range(0, 22):
        emulator.call_native(0xCBCF26FC + 1)
    emulator.call_native(0xCBCA5C48 + 1)
    emulator.call_native(0xCBCA5958 + 1)
    emulator.call_native(0xCBCA5C28 + 1)

    SCPluginWrapper = sxhg()
    print(SCPluginWrapper.d(emulator, "93095451ed51da286e052ce8f5adb30435e34d8119990a8429b4da14d7c514cb", 0, "/scauth/login", 0))
    print("Exited EMU.")
    #print("Native methods registered to SCPluginWrapper:")
    #for method in AppContext.jvm_methods.values():
        #if method.native:
            #logger.info("- [0x%08x] %s - %s" % (method.native_addr, method.name, method.signature))


except UcError as e:
    print("Exit at %x" % emulator.mu.reg_read(UC_ARM_REG_PC))
    raise
