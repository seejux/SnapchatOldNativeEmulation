from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_field_def import JavaFieldDef
from androidemu.java.java_method_def import java_method_def
from androidemu.java.constant_values import MODIFIER_STATIC, MODIFIER_PUBLIC


class ActivityThread(metaclass=JavaClassDef, jvm_name='android/app/ActivityThread'):

    def __init__(self):
        pass


    @staticmethod
    @java_method_def(name='handleBindApplication', signature='(Landroid/app/ActivityThread$AppBindData;)V', modifier=424297)
    def handleBindApplication(self, mu):
        raise NotImplementedError("handleBindApplication")

    @staticmethod
    @java_method_def(name='currentActivityThread', signature='()Landroid/app/ActivityThread;', modifier=524297)
    def currentActivityThread(self, mu):
        raise NotImplementedError("currentActivityThread")

    @staticmethod
    @java_method_def(name='getSystemContext', signature='()Landroid/app/ContextImpl;', modifier=524289)
    def getSystemContext(self, mu):
        raise NotImplementedError("getSystemContext")