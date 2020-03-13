import numpy
import matplotlib.pyplot as plt
import time
import datetime
from datetime import datetime

def to_seconds(h):
   return (h>>32) + ((float)(h&0xffffffff))/pow(2,32)

f=open('20180719172433.ht', 'rb')
data=numpy.fromfile(f,'>f8')
size=(len(data)-1)/6
size=int(size)
print(size)

data=numpy.delete(data,[0],None) #delete first element
array=numpy.split(data,6) #split 2d array in 6 single arrays
array[0]=array[0].astype(numpy.int64) # convert array to int64 datatype
array[5]=array[5]-2082844800000000000 # (1904 to 1970) in seconds 2082844800
array[5]=array[5].astype(numpy.int64) # convert array to int64 datatype

# print arrays
print("Configuration \t",array[0])
print("Voltage \t \t", array[1])
print("Current \t \t", array[2])
print("DC Link \t \t", array[3])
print("Duty Cycle \t \t", array[4])
print("Time Stamps \t", array[5])

#Extracting timestamps
ts_64bit= array[5][0]
ts_end=array[5][size-1]
print(ts_end)
ts_float=(float(ts_64bit)/1e9)
ts_end_float=(float(ts_end)/1e9)
print("\nTime Stamp (64 bit) ","%19d" %ts_64bit)

print("Start Time Stamp (float) ","%.9f" %ts_float)
print("  End Time Stamp (float) ","%.9f" %ts_end_float)

ts_dt=datetime.fromtimestamp(ts_float)
print("Shot taken on", ts_dt)
ts_end_dt=datetime.fromtimestamp(ts_end_float)
print("Shot Ended on", ts_end_dt)
print("Shot length", ts_end_float-ts_float)

#plot data
plt.plot(array[5],array[1])
plt.show()


#Current Time
time2 = datetime.now().timestamp()
print(" \nCurrent Time\n",time2)
print(datetime.now())

f.close()
