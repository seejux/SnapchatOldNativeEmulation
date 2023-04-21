from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_method_def import java_method_def
from android.ApplicationInfo import ApplicationInfo
from android.PackageManager import PackageManager
from android.ContentResolve import ContentResolver

class Context(metaclass=JavaClassDef, jvm_name='android/content/Context'):

    def __init__(self):
        self.application_info = ApplicationInfo()
        self.package_manager = PackageManager()
        self.content_resolver = ContentResolver()

    @java_method_def(name='getApplicationInfo', signature='()Landroid/content/pm/ApplicationInfo;')
    def getApplicationInfo(self, mu):
        return self.application_info

    @java_method_def(name='getPackageManager', signature='()Landroid/content/pm/PackageManager;')
    def getPackageManager(self, mu):
        return self.package_manager

    @java_method_def(name='getPackageName', signature='()Ljava/lang/String;')
    def getPackageName(self, mu):
        return 'com.snapchat.android'

    @java_method_def(name='getContentResolver', signature='()Landroid/content/ContentResolver;')
    def getContentResolver(self, mu):
        return self.content_resolver

    @java_method_def(name='getFilesDir', signature='()Ljava/io/File;')
    def getFilesDir(self, mu):
        raise NotImplementedError("getFilesDir")