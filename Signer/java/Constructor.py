from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_method_def import java_method_def
from androidemu.java.java_field_def import JavaFieldDef

class Constructor(metaclass=JavaClassDef, jvm_name='java/lang/reflect/Constructor', jvm_fields=[
    JavaFieldDef('slot', 'I', False),
    JavaFieldDef('declaringClass', 'Ljava/lang/Class;', False),
]):

    def __init__(self):
        pass

    #  @java_method_def(name='xx', signature='(Ljava/lang/String;)Ljava/lang/String;')
        # def xx(self, mu):
    #   raise NotImplementedError("xx[Constructor]")