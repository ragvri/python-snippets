from cx_Freeze import setup, Executable

setup(name='distme', version='0.1', description='Parse stuff', executables=[Executable('executable_scripts.py')])
# name=: name of the exe

# after this open the command windows where the setup file and the file to be made executable are
# and run $ python3 setup.py build
