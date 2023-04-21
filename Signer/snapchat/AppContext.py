from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_method_def import java_method_def
from androidemu.java.constant_values import MODIFIER_STATIC, MODIFIER_PUBLIC
from android.Context import Context


class AppContext(metaclass=JavaClassDef, jvm_name='com/snapchat/android/framework/misc/AppContext'):

    context = Context()

    def __init__(self):
        pass
    @staticmethod
    @java_method_def(name='get', signature='()Landroid/app/Application;', modifier=(MODIFIER_PUBLIC | MODIFIER_STATIC))
    def get(mu):
        return AppContext.context