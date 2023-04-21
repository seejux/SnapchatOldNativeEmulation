from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_method_def import java_method_def
from androidemu.java.java_field_def import JavaFieldDef

class AbstractMethod(metaclass=JavaClassDef, jvm_name='java/lang/reflect/AbstractMethod', jvm_fields=[
    JavaFieldDef('artMethod', 'Ljava/lang/reflect/ArtMethod;', False),
    JavaFieldDef('accessFlags', 'I', False),
]):

    def __init__(self):
        pass