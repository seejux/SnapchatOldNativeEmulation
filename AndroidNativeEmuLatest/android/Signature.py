from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_method_def import java_method_def
class Signature(metaclass=JavaClassDef, jvm_name='android/content/pm/Signature'):

    def __init__(self, signature):
        self._signature = bytearray.fromhex(signature)

    @java_method_def(name='toByteArray', signature='()[B')
    def toByteArray(self, mu):
        return self._signature