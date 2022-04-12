import sys
import time
from time import gmtime, strftime
import datetime
from MDSplus import *
import MDSplus
import subprocess

class MyEvent(Event):
       def run(self):
             print("RECEIVED EVENT " + self.getName())
             print(self.getTime())
             print(strftime("%y%m%d000", gmtime())) #
             print(self.getRaw()) 
             if (self.getName() =="startc!"):
	             subprocess.Popen("python START_ACQ_CONTINOUS.py",shell = 'true')
	     elif (self.getName() =="startT"):
		     y=strftime("%y%m%d000",gmtime())
                     f = open('shot_no.bin','r')
		     data = f.read()
                     f.close()
                     a=int(data[-3:])
		     b=int(data[0:6])
		     c=int(y[0:6])
		     print(data)

                     if((a>0 and b<c) or a==0):
    			f = open("shot_no.bin",'w')
    			f.write(y)
    			f.close()
                    # f = open("shot_no.bin",'wb')
		    # x = str(self.getTime())
		    # print(x)
		    # f.write(x)
                    # f.close()
                     subprocess.Popen("python START_ACQ_TIMESTAMP.py",shell = 'true')
             elif(self.getName() =="start!"):
		     subprocess.Popen("python START_ACQ.py",shell = 'true')
	     elif(self.getName() =="start_file!"):
		     subprocess.Popen("python START_ACQ_FILE.py",shell = 'true')



def main(arg):
      eventObj=MyEvent(arg)
      eventObj.run()

if __name__=="__main__":
      arg = str(sys.argv[1])
      main(arg)
