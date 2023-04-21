from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_method_def import java_method_def
from androidemu.java.java_field_def import JavaFieldDef

class NetworkCapabilities(metaclass=JavaClassDef, jvm_name='android/net/NetworkCapabilities', jvm_fields=[
   JavaFieldDef('TRANSPORT_VPN', 'I', True, 0),
]):

    def __init__(self):
        pass

    @java_method_def(name='hasTransport', signature='(I)Z')
    def hasTransport(mu):
        raise NotImplementedError("hasTransport")