from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_method_def import java_method_def


class String(metaclass=JavaClassDef, jvm_name='java/lang/String'):

    def __init__(self):
        pass

    #@java_method_def(name='xx', signature='(Ljava/lang/String;)Ljava/lang/String;')
    #def xx(self, mu):
        #raise ("Tostring")