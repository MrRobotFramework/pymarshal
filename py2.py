# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Jan  8 2021, 21:22:55) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: <daffa>
"""
PyMarshal - Compile Python Script
This project was created by MrRobot Framework 
Copyright 15 - 01 - 2021
"""
try:
    import os, sys, time, marshal
except Exception as F:
    exit('[ModuleErr] %s' % F)

if sys.version[0] in '3':
    exit('[sorry] use python version 2')
a = '\x1b[1;30m'
r = '\x1b[1;31m'
g = '\x1b[32;1m'
y = '\x1b[1;33m'
c = '\x1b[1;36m'
w = '\x1b[1;37m'
n = '\x1b[0;00m'
br = '\x1b[91;7m'
bannerpy2 = ('\n         {}___ \n{} ___ ___|{}_  {}{}| {}Author  {}:{} MrRobot\n{}| . | | |{}  _{}{}| {}Code    {}:{} Python\n{}|  _|_  |{}___{}{}| {}Version {}:{} v.5.0\n{}|_| |___| {}*{} Youtube : MrRobot Framework\n').format(r, y, br, n, y, w, r, w, y, br, n, y, w, r, w, y, br, n, y, w, r, w, y, r, a)
os.system('clear')
try:
    print bannerpy2
    print y + ' [' + w + '#' + y + '] ' + w + 'Example ' + y + ':' + w + ' /sdcard/dfv.py'
    file = raw_input(y + ' [' + w + '?' + y + '] ' + w + 'Input your file location' + y + ' :' + w + ' ')
    dfv = file.replace('.py', '')
except KeyboardInterrupt:
    sys.exit()
else:
    try:
        strng = open(file, 'r').read()
    except IOError:
        print r + '\n [' + w + '!' + r + '] ' + r + '[ ' + w + 'Error ' + r + '] ' + w + 'No such file or directory ' + r + ': ' + w + '"' + dfv + '"\n'
        sys.exit()

    try:
        code = compile(strng, '<daffa>', 'exec')
        data = marshal.dumps(code)
    except TypeError:
        sys.exit()

fileout = open(dfv + 'enc.py', 'wb')
fileout.write('#Compiled By DfvTools\n')
fileout.write('#https://github.com/md4fv\n')
fileout.write('import marshal\n')
fileout.write('exec(marshal.loads(' + repr(data) + '))')
fileout.close()
time.sleep(3)
print y + '\n [' + w + '+' + y + '] ' + w + 'File succes to compile   ' + y + ': ' + w + dfv + 'enc.py\n'