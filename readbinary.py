import numpy
import time

def to_seconds(h):
   return (h>>32) + ((float)(h&0xffffffff))/pow(2,32)

f=open('20180719172433.ht', 'rb')
data=numpy.fromfile(f,'>f8')
size=(len(data)-1)/6
data=numpy.delete(data,[0],None)
array=numpy.split(data,6)
print("Configuration \t",array[0])
print("Voltage \t \t", array[1])
print("Current \t \t", array[2])
print("DC Link \t \t", array[3])
print("Duty Cycle \t \t", array[4])
print("Time Stamps \t", array[5])
time_stamp= array[5][0]
time_conv=(float(time_stamp)/1e7)
print(time_conv)
print("\n Time Stamp (64 bit) ","%d" %time_stamp)
print("\n Shot taken on", time.ctime(to_seconds(3630550620525219330)))

f.close()
