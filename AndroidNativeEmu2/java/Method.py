from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_method_def import java_method_def
from androidemu.java.java_field_def import JavaFieldDef

class Method(metaclass=JavaClassDef, jvm_name='java/lang/reflect/Method', jvm_fields=[
    JavaFieldDef('slot', 'I', False),
    JavaFieldDef('declaringClass', 'Ljava/lang/Class;', False),
]):

    def __init__(self):
        pass

    @staticmethod
    @java_method_def(name='getMethodModifiers', signature='(Ljava/lang/Class;I)I')
    def getMethodModifiers(mu):
        raise NotImplementedError("getMethodModifiers")