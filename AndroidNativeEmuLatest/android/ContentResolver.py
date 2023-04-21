from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_field_def import JavaFieldDef
from androidemu.java.java_method_def import java_method_def

class ContentResolver(metaclass=JavaClassDef, jvm_name='android/content/ContentResolver'):

    def __init__(self):
        pass