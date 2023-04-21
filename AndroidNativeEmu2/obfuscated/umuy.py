from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_field_def import JavaFieldDef
from androidemu.java.java_method_def import java_method_def
from android.Location import Location

class umuy(metaclass=JavaClassDef, jvm_name='aebg/umuy', jvm_fields=[
]):

    def __init__(self):
        pass

    @staticmethod
    @java_method_def(name='a', signature='()Landroid/location/Location;')
    def a(mu):
        return Location()