from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_method_def import java_method_def


class File(metaclass=JavaClassDef, jvm_name='java/io/File'):

    def __init__(self):
        pass

    @java_method_def(name='getPath', signature='()Ljava/lang/String;')
    def getPath(self, mu):
        raise NotImplementedError("getPath")