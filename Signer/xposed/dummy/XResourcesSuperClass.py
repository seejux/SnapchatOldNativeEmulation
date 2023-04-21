from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_method_def import java_method_def

class XResourcesSuperClass(metaclass=JavaClassDef, jvm_name='xposed/dummy/XResourcesSuperClass', jvm_ignore=True):

    def __init__(self):
        pass