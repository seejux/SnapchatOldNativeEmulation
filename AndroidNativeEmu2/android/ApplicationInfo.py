from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_method_def import java_method_def
from androidemu.java.java_field_def import JavaFieldDef
class ApplicationInfo(metaclass=JavaClassDef, jvm_name='android/content/pm/ApplicationInfo', jvm_fields=[
    JavaFieldDef('FLAG_DEBUGGABLE', 'I', True, 2),
    JavaFieldDef('flags', 'I', False),
    JavaFieldDef('sourceDir', 'Ljava/lang/String;', False),
]):

    def __init__(self):
        self.flags = 953695812
        self.sourceDir = "/data/app/com.snapchat.android-1/base.apk"
        # self.checksum = "A25EA392"