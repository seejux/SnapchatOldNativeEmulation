import time
import urllib.parse as urlparse
from http.server import BaseHTTPRequestHandler, HTTPServer
from hashlib import sha1
import hmac
from binascii import hexlify
import hashlib
import sys
import base64
import json
import uuid
import cgi
from cgi import parse_header, parse_multipart
import logging
import posixpath
import sys

from unicorn import *
from unicorn.arm_const import *

# Java Import
from java.File import File
from java.String import String
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
from android.Application import Application
from android.ApplicationPackageManager import ApplicationPackageManager
from android.ActivityThread import ActivityThread
from android.Context import Context
from android.ApplicationInfo import ApplicationInfo
from android.PackageManager import PackageManager
from android.PackageInfo import PackageInfo
from android.Signature import Signature
from android.SettingsSecure import SettingsSecure
from android.Location import Location
from android.ContextImpl import ContextImpl

# Java Import
from obfuscated.zha import zha
from obfuscated.qyz import qyz

# Snapchat Import
from snapchat.SCPluginWrapper import SCPluginWrapper
from snapchat.AppContext import AppContext
from com.snap.opera.view.NewConcentricTimerView import NewConcentricTimerView
from com.snap.opera.view.CountdownTimerView import CountdownTimerView
from com.snapchat.android.LandingPageActivityV1 import LandingPageActivityV1
from com.snapchat.android.framework.crypto.CbcEncryptionAlgorithm import CbcEncryptionAlgorithm
from com.snap.opera.view.TextureVideoView import TextureVideoView

#xposed
from xposed.dummy.XResourcesSuperClass import XResourcesSuperClass

from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_method_def import java_method_def


# Create java class.
from samples import debug_utils
 #Configure logging
logging.basicConfig(
    stream=sys.stdout,
    level=logging.ERROR,
    format="%(asctime)s %(levelname)7s %(name)34s | %(message)s")

logger = logging.getLogger(__name__)

# Initialize emulator
emulator = Emulator(
    vfp_inst_set=True,
    vfs_root=posixpath.join(posixpath.dirname(__file__), "vfs")
)

#Snapchat
emulator.java_classloader.add_class(SCPluginWrapper)
emulator.java_classloader.add_class(NewConcentricTimerView)
emulator.java_classloader.add_class(CountdownTimerView)
emulator.java_classloader.add_class(TextureVideoView)
emulator.java_classloader.add_class(LandingPageActivityV1)
emulator.java_classloader.add_class(CbcEncryptionAlgorithm)

#xposed
emulator.java_classloader.add_class(XResourcesSuperClass)

# Android
emulator.java_classloader.add_class(Application)
emulator.java_classloader.add_class(ContextImpl)
emulator.java_classloader.add_class(ApplicationPackageManager)
emulator.java_classloader.add_class(ActivityThread)
emulator.java_classloader.add_class(AppContext)
emulator.java_classloader.add_class(Context)
emulator.java_classloader.add_class(ApplicationInfo)
emulator.java_classloader.add_class(PackageManager)
emulator.java_classloader.add_class(PackageInfo)
emulator.java_classloader.add_class(Signature)
emulator.java_classloader.add_class(SettingsSecure)
emulator.java_classloader.add_class(Location)

# Obfuscation
emulator.java_classloader.add_class(zha)
emulator.java_classloader.add_class(qyz)

# Java Libs
emulator.java_classloader.add_class(File)
emulator.java_classloader.add_class(String)
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

#logger.info("Loaded modules:")
for module in emulator.modules:
    logger.info("=> 0x%08x - %s" % (module.base, module.filename))


try:
    emulator.system_properties = {
        'ro.product.model': 'ONEPLUS A6003',
        'ro.build.version.release': '9',
        'ro.build.version.sdk': '28',
        'ro.build.version.incremental': '1904032100'
    }


    # Run JNI_OnLoad.
    #   JNI_OnLoad will call 'RegisterNatives'.
    emulator.call_symbol(lib_module, 'JNI_OnLoad', emulator.java_vm.address_ptr, 0x00)
    emulator.mu.hook_add(UC_HOOK_MEM_UNMAPPED, debug_utils.hook_unmapped)

    # Do native stuff.
    emulator.call_native(0xCBCBC904 + 1)
    for i in range(0, 22):
        emulator.call_native(0xCBCFF248 + 1)
    emulator.call_native(0xCBCA2490 + 1)
    emulator.call_native(0xCBCA2C24 + 1)
    emulator.call_native(0xCBCA3234 + 1)
    emulator.call_native(0xCBCA285C + 1)
    emulator.call_native(0xCBCA31FC + 1)
    SCPluginWrapper_activity = SCPluginWrapper()
    #response = SCPluginWrapper_activity.signrequest(emulator, [
     #   'req_token',
      #  'timestamp',
       # 'username',
    #], ['930bba5ec5111dc86ea141e6faafc6144ee54d80196eda8689b49514dac512eb0b0f3560316f326366336c35326465666f03e60d4f7edd8e6b9de1ff6a93ed532c6e3e2e461c','1559269798123','swedishfish' ], '/scauth/login',bytearray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    # arr = ["930bba5ec5111dc86ea141e6faafc6144ee54d80196eda8689b49514dac512eb", "1562810823630"]
   #print(SCPluginWrapper_activity.signrequest(emulator, ['req_token','timestamp', 'username'], ['930bba5ec5111dc86ea141e6faafc6144ee54d80196eda8689b49514dac512eb', '1562810823630', 'swedishfish'], '/bq/post_story',bytearray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])))
   # print(response)
    # emulator.mu.hook_add(UC_HOOK_BLOCK, debug_utils.hook_code)
    # print(SCPluginWrapper_activity.signtoken(emulator, '930bba5ec5111dc86ea141e6faafc6144ee54d80196eda8689b49514dac512eb'))
   #logger.info("Response from signtoken call: %s" % SCPluginWrapper_activity.signtoken(emulator, '930bba5ec5111dc86ea141e6faafc6144ee54d80196eda8689b49514dac512eb'))
   # logger.info("Response from getnonce call: %s" % SCPluginWrapper_activity.getnonce(emulator))

    print("Response from signrequest call: %s" % SCPluginWrapper_activity.signrequest(emulator, ['req_token', 'username'], ['096bd51fc80e8ac506b30a1bb080e31ce46f1bc852ecd7d6dc1d525a22b9541f', 'swedishfish'], '/bq/post_story',bytearray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])))
    print("Response from signrequest call: %s" % SCPluginWrapper_activity.signrequest(emulator, ['req_token', 'username'], ['096bd51fc80e8ac506b30a1bb080e31ce46f1bc852ecd7d6dc1d525a22b9541f', 'swedishfish'], '/bq/post_story',bytearray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])))
    print("Exited EMU.")
    print("Native methods registered to SCPluginWrapper:")
    for method in SCPluginWrapper.jvm_methods.values():
        if method.native:
           logger.info("- [0x%08x] %s - %s" % (method.native_addr, method.name, method.signature))

            
except UcError as e:
    print("Exit at %x" % emulator.mu.reg_read(UC_ARM_REG_PC))
    raise
