from distutils.core import setup
from py2exe import *
from numpy import *
import matplotlib
import prigogine

setup(
    data_files=matplotlib.get_py2exe_datafiles(),
    options = {
        "py2exe":{
            'includes': ['zmq.backend.cython', "matplotlib.backends.backend_qt4agg", "prigogine.PrigogineCore"],
            'excludes': ['zmq.libzmq'],
            "dll_excludes": ["MSVCP90.dll", "HID.DLL", "w9xpopen.exe", "libzmq.pyd"],
    }
},
console = [{'script': './prigogine/Prigogine.py'}]
)


