from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_method_def import java_method_def


class Location(metaclass=JavaClassDef, jvm_name='android/location/Location'):

    def __init__(self):
       pass

    @staticmethod
    @java_method_def(name='a', signature='()Landroid/location/Location;')
    def a(mu):
       raise NotImplementedError("Location: a")

    @java_method_def(name='isFromMockProvider', signature='()Z')
    def a(self, mu):
        return False