#!/usr/bin/python2
#-*- coding: utf-8 -*-
#marshal py2

'''
PyMarshal - Compile Python Script
This project was created by MrRobot Framework 
Copyright 15 - 01 - 2021
'''

try:
        import os,sys,time,marshal
except Exception as F:
        exit("[ModuleErr] %s"%(F))
        
if sys.version[0] in '3':
        exit("[sorry] use python version 2")

# Color
a='\033[1;30m'
r='\033[1;31m'
g='\033[32;1m' 
y='\033[1;33m'
c='\033[1;36m' 
w='\033[1;37m' 
n='\033[0;00m' 
br='\033[91;7m' 

bannerpy2 = """
         {}___ 
{} ___ ___|{}_  {}{}| {}Author  {}:{} MrRobot
{}| . | | |{}  _{}{}| {}Code    {}:{} Python
{}|  _|_  |{}___{}{}| {}Version {}:{} v.5.0
{}|_| |___| {}*{} Youtube : MrRobot Framework
""".format(r,y,br,n,y,w,r,w,y,br,n,y,w,r,w,y,br,n,y,w,r,w,y,r,a)

'''
Author   : MrRobot
Telegram : MrRobot Corp 
Youtube  : MrRobot Framework
Please Like dan Subscribe ya

The quieter you become, the more you are able to hear
'''

os.system('clear')
try:
    print(bannerpy2)
    print (y+' ['+w+'#'+y+'] '+w+'Example '+y+':'+w+' /sdcard/dfv.py')
    file = raw_input(y+' ['+w+'?'+y+'] '+w+'Input your file location'+y+' :'+w+' ')
    dfv = file.replace('.py', '')
except KeyboardInterrupt:
    sys.exit()
else:
    try:
        strng = open(file, 'r').read()
    except IOError:
        print (r+'\n ['+w+'!'+r+'] '+r+'[ '+w+'Error '+r+'] '+w+'No such file or directory '+r+': '+w+'"'+dfv+'"\n')
        sys.exit()
    try:
        code = compile(strng, '<daffa>', 'exec')
        data = marshal.dumps(code)
    except TypeError:
        sys.exit()
fileout = open(dfv +'enc.py', 'wb')
fileout.write('#Compiled By MrRobot404\n')
fileout.write('#https://www.youtube.com/c/MrRobotFramework\n')
fileout.write('import marshal\n')
fileout.write('exec(marshal.loads('+repr(data)+'))')
fileout.close()
time.sleep(3) 
print (y+'\n ['+w+'+'+y+'] '+w+'File succes to compile   '+y+': ' + w + dfv + 'enc.py\n')
