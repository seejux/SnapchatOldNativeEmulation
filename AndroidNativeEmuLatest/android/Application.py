from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_field_def import JavaFieldDef
from androidemu.java.java_method_def import java_method_def

class Application(metaclass=JavaClassDef, jvm_name='android/app/Application'):

    def __init__(self):
        pass