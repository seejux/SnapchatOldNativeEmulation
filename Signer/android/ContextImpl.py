from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_method_def import java_method_def
from androidemu.java.constant_values import MODIFIER_STATIC, MODIFIER_PUBLIC
from android.Context import Context


class ContextImpl(metaclass=JavaClassDef, jvm_name='android/app/ContextImpl'):

    def __init__(self):
        pass


    @staticmethod
    @java_method_def(name='getPackageManager', signature='()Landroid/content/pm/PackageManager;', modifier=(MODIFIER_PUBLIC | MODIFIER_STATIC))
    def getPackageManager(self, mu):
        raise NotImplementedError("getPackageManager")

    @staticmethod
    @java_method_def(name='getPackageName', signature='()Ljava/lang/String;', modifier=(MODIFIER_PUBLIC | MODIFIER_STATIC))
    def getPackageName(self, mu):
        raise NotImplementedError("getPackageName")

    @staticmethod
    @java_method_def(name='getApplicationInfo', signature='()Landroid/content/pm/ApplicationInfo;', modifier=(MODIFIER_PUBLIC | MODIFIER_STATIC))
    def getApplicationInfo(self, mu):
        raise NotImplementedError("getApplicationInfo")
