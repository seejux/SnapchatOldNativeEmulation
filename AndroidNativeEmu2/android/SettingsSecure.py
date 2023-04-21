from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_method_def import java_method_def
from androidemu.java.java_field_def import JavaFieldDef

import uuid
class SettingsSecure(metaclass=JavaClassDef, jvm_name='android/provider/Settings$Secure', jvm_fields={
    JavaFieldDef('ALLOW_MOCK_LOCATION', 'Ljava/lang/String;', True, 'mock_location'),
}):

    def __init__(self):
        pass

    @java_method_def(name='getString', signature='(Landroid/content/ContentResolver;Ljava/lang/String;)Ljava/lang/String;', args_list=['jobject', 'jstring'])
    def getString(self, content_resolver, key):
        if key.value == 'android_id':
            return '90ea053c25d2b3d1'
        else:
            raise NotImplementedError("Unknown key %s" % key)