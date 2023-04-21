from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_method_def import java_method_def


class ClassLoader(metaclass=JavaClassDef, jvm_name='java/lang/ClassLoader'):

    def __init__(self):
        pass

    @staticmethod
    @java_method_def(name='getSystemClassLoader', signature='()Ljava/lang/ClassLoader;')
    def getSystemClassLoader(mu):
        raise NotImplementedError("getSystemClassLoader")