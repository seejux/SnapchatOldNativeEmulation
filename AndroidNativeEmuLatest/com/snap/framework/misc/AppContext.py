from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_method_def import java_method_def
from androidemu.java.constant_values import MODIFIER_STATIC, MODIFIER_PUBLIC
from android.Application import Application

class AppContext(metaclass=JavaClassDef, jvm_name='com/snap/framework/misc/AppContext'):

    def __init__(self):
        pass

    @java_method_def(name='get', signature='()Landroid/app/Application;', modifier=(MODIFIER_PUBLIC | MODIFIER_STATIC))
    def get(self):
        return Application()