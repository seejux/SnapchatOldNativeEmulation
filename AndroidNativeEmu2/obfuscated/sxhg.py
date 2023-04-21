from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_field_def import JavaFieldDef
from androidemu.java.java_method_def import java_method_def
data = [120, 66, -53, -77, -109, 21, -98, 14, -63, -24, 1, 2, -47, 75, 26, -98, -42, 77, -56, -41, -106, -79, -96, -109, 85, 14, -125, 54, 3, -7, -106, 33, -38, -83, 94, -19, -88, -77, -39, 122, -15, -29, -22, -50, 37, 72, -72, -122, -88, 47, 63, 49, -89, -26, -110, 108]
def twoscomplement_to_unsigned(i):
    return i % 256
class sxhg(metaclass=JavaClassDef, jvm_name='luwt/sxhg', jvm_fields=[
    JavaFieldDef('f', '[B', True, bytearray(map(twoscomplement_to_unsigned, data))),
]):

    def __init__(self):
        pass

    @java_method_def(name='h', signature='(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;[B)[B', native=True)
    def h(self, mu):
        pass

    @java_method_def(name='b', signature='(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;[B)Ljava/lang/String;', native=True)
    def b(self, mu):
        pass

    @java_method_def(name='d', signature='(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;[B)Ljava/lang/String;', native=True)
    def d(self, mu):
        pass

    @java_method_def(name='c', signature='([B[B)I', native=True)
    def c(self, mu):
        pass
    @java_method_def(name='g', signature='([B[B)I', native=True)
    def g(self, mu):
        pass

    @java_method_def(name='a', signature='(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;[B)Ljava/lang/String;', native=True)
    def a(self, mu):
        pass

    @java_method_def(name='e', signature='(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;[B)Ljava/lang/String;', native=True)
    def e(self, mu):
        pass