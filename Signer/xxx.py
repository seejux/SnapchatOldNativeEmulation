import time
import urllib.parse as urlparse
from http.server import BaseHTTPRequestHandler, HTTPServer
from hashlib import sha1
import hmac
from binascii import hexlify
import hashlib
import frida
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
from android.Context import Context
from android.ApplicationInfo import ApplicationInfo
from android.PackageManager import PackageManager
from android.PackageInfo import PackageInfo
from android.Signature import Signature
from android.SettingsSecure import SettingsSecure
from android.Location import Location

# Java Import
from obfuscated.zha import zha
from obfuscated.qyz import qyz

# Snapchat Import
from snapchat.SCPluginWrapper import SCPluginWrapper
from snapchat.AppContext import AppContext


from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_method_def import java_method_def


# Create java class.
from samples import debug_utils
# Configure logging
#logging.basicConfig(
 #   stream=sys.stdout,
  #  level=logging.DEBUG,
   # format="%(asctime)s %(levelname)7s %(name)34s | %(message)s"
#)

logger = logging.getLogger(__name__)

# Initialize emulator
emulator = Emulator(
    vfp_inst_set=True,
    vfs_root=posixpath.join(posixpath.dirname(__file__), "vfs")
)

# Android
emulator.java_classloader.add_class(SCPluginWrapper)
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
emulator.load_library("example_binaries/libdl.so")
emulator.load_library("example_binaries/libc.so")
emulator.load_library("example_binaries/libstdc++.so")
emulator.load_library("example_binaries/libm.so")
lib_module = emulator.load_library("example_binaries/libscplugin.so")

HOST_NAME = '127.0.0.1'
PORT_NUMBER = 8080

request_queue = dict()

def on_message(message, data):
    if message["type"] == "send":
        request_queue[message["payload"]["identifier"]] = message["payload"]["payload"]
    else:
        print(str(message["type"]))


class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        if '/useragent' in self.path:
            self.respond({'status': 200}, json.dumps({'success': True, 'response': 'Snapchat/10.35.6.0 (ONEPLUS A6003; Android 9#1903250100#28; gzip)'}))

        else:
            resp = ''
            self.respond({'status': 200}, {'req_token': resp})

    def do_POST(self):
        content_type = str(self.headers['Content-Type'])

        if content_type == 'application/json':
            content_length = int(self.headers['Content-Length'])
            post_json = json.loads(self.rfile.read(content_length).decode('utf8').replace("'", '"'))

            if '/sign/req_token' in self.path:
                req_token = post_json['req_token']
                self.respond({'status': 200}, json.dumps({'success': True, 'response': SCPluginWrapper_activity.signtoken(emulator, req_token)}))

            else:
                self.respond({'status:': 400}, json.dumps({'success': False, 'response': 'Invalid url path'}))

    def handle_http(self, status_code, resp):
        self.send_response(status_code)
        self.end_headers()
        return bytes(resp, 'UTF-8')

    def respond(self, opts, resp):
        response = self.handle_http(opts['status'], resp)
        self.wfile.write(response)


if __name__ == '__main__':

    emulator.system_properties = {
        'ro.product.model': 'ONEPLUS A6003',
        'ro.build.version.release': '9',
        'ro.build.version.sdk': '28',
        'ro.build.version.incremental': '1904032100'
    }

    emulator.call_native(0xCBCBC904 + 1)
    for i in range(0, 22):
        emulator.call_native(0xCBCFF248 + 1)
    emulator.call_native(0xCBCA2490 + 1)
    emulator.call_native(0xCBCA2C24 + 1)
    emulator.call_native(0xCBCA3234 + 1)
    emulator.call_native(0xCBCA285C + 1)
    emulator.call_native(0xCBCA31FC + 1)
    emulator.call_symbol(lib_module, 'JNI_OnLoad', emulator.java_vm.address_ptr, 0x00)
    emulator.mu.hook_add(UC_HOOK_MEM_UNMAPPED, debug_utils.hook_unmapped)
    SCPluginWrapper_activity = SCPluginWrapper()
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print(time.asctime(), 'Server Starts - %s:%s' % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), 'Server Stops - %s:%s' % (HOST_NAME, PORT_NUMBER))
