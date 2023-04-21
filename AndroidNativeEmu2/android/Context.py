from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_method_def import java_method_def
from android.ApplicationInfo import ApplicationInfo
from android.PackageManager import PackageManager
from androidemu.java.java_field_def import JavaFieldDef
from android.ContentResolver import ContentResolver

class Context(metaclass=JavaClassDef, jvm_name='android/content/Context', jvm_fields=[
   JavaFieldDef('CONNECTIVITY_SERVICE', 'Ljava/lang/String;', True, ""),
]):

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
        #return 'com.toyopagroup.picaboo'

    @java_method_def(name='getContentResolver', signature='()Landroid/content/ContentResolver;')
    def getContentResolver(self, mu):
        return self.content_resolver

    @java_method_def(name='getFilesDir', signature='()Ljava/io/File;')
    def getFilesDir(self, mu):
        raise NotImplementedError("getFilesDir")

    @java_method_def(name='getSystemService', signature='(Ljava/lang/String;)Ljava/lang/Object;')
    def getSystemService(self, mu):
        return 0

    @java_method_def(name='checkCallingOrSelfPermission', signature='(Ljava/lang/String;)I')
    def checkCallingOrSelfPermission(self, mu):
        raise NotImplementedError("checkCallingOrSelfPermission")