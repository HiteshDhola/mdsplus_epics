import sys
import MDSplus
from MDSplus import *
import time
import numpy
import subprocess




def test_var_args_call(arg1, arg2, arg3):
    print "arg1:", arg1
    print "Treename:", arg2
    print "shot_no:", arg3
    tcl('set %s %s'%("tree" , arg2))
    tcl('create %s %d'%("pulse", arg3))
    tcl('set tree %s/shot=%d'%(arg2, arg3))
    tcl('do action_1')
    time.sleep(10)
    tcl('do action_2')
    time.sleep(5)
    #subprocess.Popen("data.py" , shell = 'True')
    print("Everything is completed")





f = open('shot_no.bin','rb')
data = f.read()
#f.close()
data = float(data)
shot_no = int(data)
kwargs = {"arg3": shot_no, "arg2": "finalpv"}
test_var_args_call("hello_this_start_event", **kwargs)
