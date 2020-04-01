import sys
from MDSplus import *
import MDSplus
import subprocess

class MyEvent(Event):
       def run(self):
             print("RECEIVED EVENT " + self.getName())
             print(self.getTime())
             print(self.getRaw()) 
             if (self.getName() =="startc!"):
	             subprocess.Popen("python START_ACQ_CONTINOUS.py",shell = 'true')
	     elif (self.getName() =="startT"):
                     f = open("shot_no.bin",'wb')
		     x = str(self.getTime())
		     f.write(x)
                     f.close()
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
