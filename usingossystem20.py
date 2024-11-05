import os
from  datetime import datetime 
"""
print(dir(os))

print(os.getcwd())

os.chdir('C:\Vedang\Software\PythonCodes\Ai path')
print(os.getcwd())
"""
#section 2

os.chdir('C:\Vedang\Software\PythonCodes\Ai path')


os.mkdir('OS-Demo-2')
os.makedirs('OS-Demo-2')
print(os.listdir())


#section 3
os.chdir('C:\Vedang\Software\PythonCodes\Ai path')
mod_time = os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp(mod_time))

#section 4
os.chdir('C:\Vedang\Software\PythonCodes\Ai path')

for dirpath, dirnames, filenames in os.walk('C:\Vedang\Software\PythonCodes\Ai path'):
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()

#section 5

os.chdir('C:\Vedang\Software\PythonCodes\Ai path')
print(os.environ.get('HOME'))

file_path = os.path.join(os.environ.get('HOME'), 'test2.txt')
print(file_path)

with open(file_path, 'w') as f:
    f.wte

#section 6


os.chdir('C:\Vedang\Software\PythonCodes\Ai path')
print(os.path.split('/tmp/test.txt'))
print(os.path.exists('/tmp/test.txt'))
print(os.path.isdir('/tmp/efwgifw'))
print(os.path.isfile('/tmp/efwgifw'))
print(os.path.splitext('/tmp/test.txt'))