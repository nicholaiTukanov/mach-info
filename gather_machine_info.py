import subprocess

class Machine:

    def __init__(self, name="", cpu_name="", cpu_freq=0.0, cores=0, os="", compilers=list()):
        self.init_name()
        self.init_os_info()
        self.init_cpu_info()
        self.init_compiler_info("")
        self.init_py_info()

    def __str__(self):
        info_str = (str(self.name) +"\n"+
                   str(self.cpu_name) +"\n"+
                   str(self.cpu_freq) +"\n"+
                   str(self.cores) +"\n"+
                   str(self.os) +"\n"+
                   str(self.compilers) +"\n"+
                   str(self.py_v))
        return info_str

    def init_name(self):
        import socket
        self.name = socket.gethostname()

    def init_os_info(self):
        import os
        self.os = os.uname()

    def init_cpu_info(self, name="", cpu_freq=0.0, cores=-1):
        import platform
        import multiprocessing
        self.cpu_name = platform.processor() if name=="" else name
        self.cores=multiprocessing.cpu_count() if cores==-1 else cores

        clock="cat /proc/cpuinfo"
        process = subprocess.Popen(clock.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        freq=0.0
        for o in output.split():
            if("MHz" in str(o)):
                self.cpu_freq=o
                break

    def init_compiler_info(self, path=""):
        #clang=path+"clang --version"
        gcc=path+"gcc --version"
        process = subprocess.Popen(gcc.split(), stdout=subprocess.PIPE)
        output_gcc, error = process.communicate()
        self.compilers=[output_gcc]

    def init_py_info(self, path=""):
        import sys
        self.py_v = sys.version_info


m=Machine()
print(m)
