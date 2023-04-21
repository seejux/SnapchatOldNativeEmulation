from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_method_def import java_method_def

class ConnectivityManager(metaclass=JavaClassDef, jvm_name='android/net/ConnectivityManager'):

    def __init__(self):
        pass

    @java_method_def(name='getAllNetworks', signature='()[Landroid/net/Network;')
    def getAllNetworks(mu):
        raise NotImplementedError("getAllNetworks")

    @java_method_def(name='getNetworkCapabilities', signature='(Landroid/net/Network;)Landroid/net/NetworkCapabilities;')
    def getNetworkCapabilities(mu):
        raise NotImplementedError("getNetworkCapabilities")