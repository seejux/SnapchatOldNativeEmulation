from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_method_def import java_method_def


class Class(metaclass=JavaClassDef, jvm_name='java/lang/Class'):

    def __init__(self):
        pass

    @staticmethod
    @java_method_def(name='forName', signature='(Ljava/lang/String;)Ljava/lang/Class;')
    def forName(mu):
        raise NotImplementedError("forName")

    @staticmethod
    @java_method_def(name='forName', signature='(Ljava/lang/String;ZLjava/lang/ClassLoader;)Ljava/lang/Class;')
    def forName_two(mu):
        raise NotImplementedError("forName2")