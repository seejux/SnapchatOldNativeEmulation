from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_method_def import java_method_def
from androidemu.java.java_field_def import JavaFieldDef
def twoscomplement_to_unsigned(i):
    return i % 256
data = [13, 5, 97, -121, -26, -42, 82, -10, 114, -66, 38, -94, -79, -2, 121, -73, 41, 53, 121, 101, -91, -30, -40, -51, 61, 4, -93, -102, -4, 126, -27, 73, -76, 58, 92, 119, -28, -93, 68, -69, -103, -2, 52, 92, -110, 13, 37, -23]
class vug(metaclass=JavaClassDef, jvm_name='nxzn/vug', jvm_fields=[
    JavaFieldDef('f', '[B', True, bytearray(map(twoscomplement_to_unsigned, data))),
]):
    def __init__(self):
        pass

    @java_method_def(name='g', signature='(Ljava/lang/String;Ljava/lang/String;)[B', native=True)
    def g(self, mu):
        pass

    @java_method_def(name='d',
                     signature='(Ljava/lang/String;Ljava/lang/String;)[B',
                     native=True)
    def d(self, mu):
        pass

    @java_method_def(name='b', signature='([BLjava/lang/String;)[B', native=True)
    def b(self, mu):
        pass

    @java_method_def(name='e', signature='(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;', native=True)
    def e(self, mu):
        pass

    @java_method_def(name='c', signature='(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;', native=True)
    def c(self, mu):
        pass

    @java_method_def(name='a', signature='(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;', native=True)
    def a(self, mu):
        pass