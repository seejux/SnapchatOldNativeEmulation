from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_method_def import java_method_def

class SCPluginWrapper(metaclass=JavaClassDef, jvm_name='com/snapchat/android/core/security/SCPluginWrapper'):

    def __init__(self):
        pass

    @java_method_def(name='signToken', signature='(Ljava/lang/String;)Ljava/lang/String;', native=True)
    def signtoken(self, mu):
        pass

    @java_method_def(name='signRequest',
                     signature='([Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;[B)Ljava/lang/String;',
                     native=True)
    def signrequest(self, mu):
        pass

    @java_method_def(name='getNonce', signature='(Ljava/lang/String;)Ljava/lang/String;', native=True)
    def getnonce(self, mu):
        pass