from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_method_def import java_method_def
from androidemu.java.constant_values import MODIFIER_STATIC, MODIFIER_PUBLIC

class ZipEntry(metaclass=JavaClassDef, jvm_name='java/util/zip/ZipEntry'):

    def __init__(self, entry):
        self._entry_ = entry
        pass

    @java_method_def(name='getCrc', signature='()J')
    def getCrc(self, emu):
        return self._entry_.CRC
