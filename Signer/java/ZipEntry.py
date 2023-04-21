from zipfile import ZipInfo

from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_method_def import java_method_def
from androidemu.java.constant_values import MODIFIER_STATIC, MODIFIER_PUBLIC

class ZipEntry(metaclass=JavaClassDef, jvm_name='java/util/zip/ZipEntry'):

    def __init__(self, zip_info: ZipInfo):
        self._zip_info = zip_info

    @java_method_def(name='getCrc', signature='()J', modifier=(MODIFIER_PUBLIC | MODIFIER_STATIC))
    def get_crc(self, mu):
        return self._zip_info.CRC