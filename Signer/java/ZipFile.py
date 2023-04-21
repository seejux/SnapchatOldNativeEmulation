from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_method_def import java_method_def
from androidemu.java.constant_values import MODIFIER_STATIC, MODIFIER_PUBLIC
from java.ZipEntry import ZipEntry
import zipfile
class ZipFile(metaclass=JavaClassDef, jvm_name='java/util/zip/ZipFile'):

    def __init__(self):
        self._file_name = None
        self._zip = None

    @java_method_def(name='<init>', signature='(Ljava/lang/String;)V', args_list=['jstring'], modifier=(MODIFIER_PUBLIC | MODIFIER_STATIC))
    def init(self, emu, file_name):
        self._file_name = file_name.value
        self._zip = zipfile.ZipFile(emu.vfs.translate_path(self._file_name), 'r')

    @java_method_def(name='getEntry', signature='(Ljava/lang/String;)Ljava/util/zip/ZipEntry;', args_list=['jstring'], modifier=(MODIFIER_PUBLIC | MODIFIER_STATIC))
    def get_entry(self, mu, entry_name):
        try:
            return ZipEntry(self._zip.getinfo(entry_name.value))
        except KeyError:
            return 0

    @java_method_def(name='close', signature='()V')
    def close(self, mu):
        self._zip.close()