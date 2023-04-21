from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_field_def import JavaFieldDef
from androidemu.java.java_method_def import java_method_def
from android.PackageInfo import PackageInfo
class PackageManager(metaclass=JavaClassDef, jvm_name='android/content/pm/PackageManager', jvm_fields={
    JavaFieldDef('GET_SIGNATURES', 'I', True, 64),
}):

    def __init__(self):
        self.packinfo = PackageInfo()
        pass

    @java_method_def(name='getPackageInfo', signature='(Ljava/lang/String;I)Landroid/content/pm/PackageInfo;', args_list=['jstring', 'jint'])
    def getPackageInfo(self, mu, s, i):
        return self.packinfo

    @java_method_def(name='getInstallerPackageName', signature='(Ljava/lang/String;)Ljava/lang/String;')
    def getInstallerPackageName(self, mu):
        return "com.android.vending"