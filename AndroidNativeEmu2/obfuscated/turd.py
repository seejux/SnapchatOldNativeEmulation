from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_field_def import JavaFieldDef
from androidemu.java.java_method_def import java_method_def


class turd(metaclass=JavaClassDef, jvm_name='jvj/turd', jvm_fields=[
]):

    def __init__(self):
        pass

    @staticmethod
    @java_method_def(name='a', signature='()I')
    def a(mu):
        return 0