from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_method_def import java_method_def
from androidemu.java.java_field_def import JavaFieldDef

class Field(metaclass=JavaClassDef, jvm_name='java/lang/reflect/Field', jvm_fields=[
    JavaFieldDef('accessFlags', 'I', False),
    JavaFieldDef('slot', 'I', False),
    JavaFieldDef('declaringClass', 'Ljava/lang/Class;', False),
    JavaFieldDef('artField', 'Ljava/lang/reflect/ArtField;', False),
]):

    def __init__(self):
        pass

    @java_method_def(name='getFieldModifiers', signature='(Ljava/lang/Class;I)I')
    def getFieldModifiers(self, mu):
        raise NotImplementedError("getFieldModifiers")