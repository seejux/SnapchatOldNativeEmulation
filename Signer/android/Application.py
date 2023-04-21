from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_method_def import java_method_def
from androidemu.java.constant_values import MODIFIER_STATIC, MODIFIER_PUBLIC
from android.Context import Context


class Application(metaclass=JavaClassDef, jvm_name='android/app/Application'):

    def __init__(self):
        pass

    @staticmethod
    @java_method_def(name='attach', signature='(Landroid/content/Context;)V', modifier=(MODIFIER_PUBLIC | MODIFIER_STATIC))
    def handleBindApplication(self, mu):
        raise NotImplementedError("attach")