import epics
import time
import subprocess




def onChanges(pvname=None, value=None, char_value=None, **kw):
	print 'PV Changed! ', pvname, char_value, time.ctime()
        if (char_value == '1'):
        	subprocess.Popen("python data_remote.py", shell="True")


mypv = epics.PV('offlinedata:bi.VAL')
mypv.add_callback(onChanges)

print 'Now wait for changes'

t0 = time.time()
while time.time() - t0 < 12000.0:
	time.sleep(1.e-3)
print 'Done.'
