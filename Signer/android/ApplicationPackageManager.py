from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_method_def import java_method_def
from androidemu.java.constant_values import MODIFIER_STATIC, MODIFIER_PUBLIC
from android.Context import Context


class ApplicationPackageManager(metaclass=JavaClassDef, jvm_name='android/app/ApplicationPackageManager'):

    def __init__(self):
        pass

    @staticmethod
    @java_method_def(name='getResourcesForApplication', signature='(Landroid/content/pm/ApplicationInfo;)Landroid/content/res/Resources;', modifier=(MODIFIER_PUBLIC | MODIFIER_STATIC))
    def handleBindApplication(self, mu):
        raise NotImplementedError("getResourcesForApplication")

    @staticmethod
    @java_method_def(name='getPackageInfo', signature='(Ljava/lang/String;I)Landroid/content/pm/PackageInfo;', modifier=(MODIFIER_PUBLIC | MODIFIER_STATIC))
    def getPackageInfo(self, mu):
        raise NotImplementedError("getPackageInfo")