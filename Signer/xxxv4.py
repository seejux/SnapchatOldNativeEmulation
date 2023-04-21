import time
import urllib.parse as urlparse
from socketserver import TCPServer
from http.server import SimpleHTTPRequestHandler
from ssl import wrap_socket
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
import random

from unicorn import *
from unicorn.arm_const import *
from samples import debug_utils

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

HOST_NAME = '0.0.0.0'
PORT_NUMBER = 80

request_queue = dict()

def on_message(message, data):
    if message["type"] == "send":
        request_queue[message["payload"]["identifier"]] = message["payload"]["payload"]
    else:
        print(str(message["type"]))


class MyHandler(SimpleHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json; charset=utf-8')
        self.end_headers()

    def do_GET(self):
        if '/useragent' in self.path:
            self.respond({'status': 200}, json.dumps({'success': True, 'response': 'Snapchat/10.79.5.0 (ONEPLUS A6003; Android 9#1904032100#28; gzip)' }))
        if '/appleuseragent' in self.path:
            self.respond({'status': 200}, json.dumps({'success': True, 'response': 'Snapchat/10.79.5.0 (ONEPLUS A6003; iOS 12.1.4; gzip)' }))

        else:
            resp = ''
            self.respond({'status': 200}, {'req_token': resp})

    def do_POST(self):
        content_type = str(self.headers['Content-Type'])

        if content_type == 'text/plain; charset=utf-8':
            content_length = int(self.headers['Content-Length'])
            post_json = json.loads(self.rfile.read(content_length).decode('utf8').replace("'", '"'))

            if '/sign/req_token' in self.path:
                req_token = post_json['req_token']
                resp = SCPluginWrapper_activity.signtoken(emulator, req_token)
                self.respond({'status': 200}, json.dumps({'success': True, 'response': resp}))

            #if '/signregister/client_token_register' in self.path:
                # signtype = post_json['signtype']
             #   username = post_json['username']
             #   timestamp = post_json['timestamp']
             #   req_token = post_json['req_token']
             #   path = post_json['path']
             #   dtoken1i = post_json['dtoken1i']
             #   dsig = post_json['dsig']
             #   password = post_json['password']
             #   resp = SCPluginWrapper_activity.signrequest(emulator, ['username', 'password', 'timestamp', 'req_token', 'dsig', 'dtoken1i'], [username, password,  timestamp, req_token, dsig, dtoken1i], path, bytearray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
             #   self.respond({'status': 200}, json.dumps({'success': True, 'response': resp}))

            if '/sign/client_token' in self.path:           
                # signtype = post_json['signtype']
                username = post_json['username']
                #timestamp = post_json['timestamp']
                req_token = post_json['req_token']
                path = post_json['path']
                resp = SCPluginWrapper_activity.signrequest(emulator, ['username', 'req_token'], [username, req_token], path, bytearray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
                self.respond({'status': 200}, json.dumps({'success': True, 'response': resp}))

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
    httpd = TCPServer(('0.0.0.0', 443), MyHandler)
    httpd.socket = wrap_socket(httpd.socket, certfile='./cert.pem', keyfile='./cert.key', server_side=True)
    print(time.asctime(), 'Server Starts - %s:%s' % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), 'Server Stops - %s:%s' % (HOST_NAME, PORT_NUMBER))

