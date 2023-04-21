from androidemu.emulator import Emulator
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_method_def import java_method_def
from java.StackTraceElement import StackTraceElement
class Thread(metaclass=JavaClassDef, jvm_name='java/lang/Thread'):

    def __init__(self):
        pass

    @staticmethod
    @java_method_def(name='currentThread', signature='()Ljava/lang/Thread;', native=False)
    def currentThread(self, *args, **kwargs):
        return Thread()

    @java_method_def(name='getStackTrace', signature='()[Ljava/lang/StackTraceElement;', native=False)
    def getStackTrace(self, *args, **kwargs):
        return [StackTraceElement("com.snap.mushroom."),
                StackTraceElement("com.snap.mushroom.MainActivity"),
                StackTraceElement("com.snap.dagger."),
                StackTraceElement("java.lang.reflect.Method"),
                StackTraceElement("java.lang.reflect.Method"),
                StackTraceElement("android.support.v7.app.AppCompatViewInflater$DeclaredOnClickListener"),
                StackTraceElement("android.view.View"),
                StackTraceElement("android.os.Handler"),
                StackTraceElement("android.os.Handler"),
                StackTraceElement("android.os.Looper"),
                StackTraceElement("android.app.ActivityThread"),
                StackTraceElement("java.lang.reflect.Method"),
                StackTraceElement("java.lang.reflect.Method"),
                StackTraceElement("com.android.internal.os.ZygoteInit$MethodAndArgsCaller"),
                StackTraceElement("com.android.internal.os.ZygoteInit"),
                StackTraceElement("dalvik.system.NativeStart")]
    #[StackTraceElement("")]