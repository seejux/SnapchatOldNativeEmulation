from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_field_def import JavaFieldDef
from androidemu.java.java_method_def import java_method_def


class suks(metaclass=JavaClassDef, jvm_name='eyrc/suks', jvm_fields=[
]):

    def __init__(self):
        pass

    @staticmethod
    @java_method_def(name='a', signature='()Ljava/lang/String;')
    def a(mu):
        return 0