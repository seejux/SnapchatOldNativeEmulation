from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_field_def import JavaFieldDef
from androidemu.java.java_method_def import java_method_def

class SCPluginWrapper(metaclass=JavaClassDef, jvm_name='com/snapchat/android/core/security/SCPluginWrapper', jvm_fields={
    JavaFieldDef('DATA', '[B', True, bytearray.fromhex("2852E16D09555F4D3979CB7F3BBA8AE56D0FB749"
                                                       "EB0C9FEAA97FF5C5AC580443447E309DB730CBA9"
                                                       "EFC29C56F08CBCA908539DC669FC30CAC41D6A9D"
                                                       "365E2048")),
}):

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