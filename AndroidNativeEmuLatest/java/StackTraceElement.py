from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_method_def import java_method_def


class StackTraceElement(metaclass=JavaClassDef, jvm_name='java/lang/StackTraceElement'):
    def __init__(self, _name):
        self.name = _name

    @java_method_def(native=False, name='getClassName', signature="()Ljava/lang/String;")
    def getClassName(self, *args, **kwargs):
        return self.name
