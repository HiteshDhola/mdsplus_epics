import epics
import time
import subprocess




def onChanges(pvname=None, value=None, char_value=None, **kw):
	print 'PV Changed! ', pvname, char_value
        if (char_value == '1'):
        	subprocess.Popen("setevent startT", shell="True")


mypv = epics.PV('onlinedata:bi.VAL')
mypv.add_callback(onChanges)

print 'Now wait for changes'

t0 = time.time()
#while time.time() - t0 < 12220.0:
while 1:
	time.sleep(1.e-3)
print 'Done.'
