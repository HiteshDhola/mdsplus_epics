import numpy
import time
from MDSplus import*
import os as path
import struct
from pylab import*


##################reading from file##########################################################

file_path="/home/codac-dev/USEFUL FOLDERS/SHOT_FILE/20190116150205.ht"
f=open(file_path, 'rb')
data=numpy.fromfile(f,'>d')
print(data)

##################FORMING INDIVIDUAL ARRAY##########################################################


size=(len(data)-1)/6
data=numpy.delete(data,[0],None)
array=numpy.split(data,6)
print("Configuration \t",array[0])
print("Voltage \t \t", array[1])
print("Current \t \t", array[2])
print("DC Link \t \t", array[3])
print("Duty Cycle \t \t", array[4])
print("Time Stamps \t", array[5])

##################conversion of timestamp ##########################################################

timestamp = array[5]/100
timestamp = timestamp - 20828448000000000 #Epoch
timestamp = timestamp - 6311520000000000 #MDSPlus
timestamp = timestamp*100

Voltage = array[1]
Current = array[2]
DC_Link = array[3]
Duty_Cycle = array[4]

f.close()

print(len(Voltage))
print(len(Current))
print(len(DC_Link))
print(len(Duty_Cycle))

###################MDSPLUS SECTION############################################
###################CHANNEL_1############################################


shot_no = int(raw_input("enter the shot_no:"))


###################TREE OPERATION############################################
myTree = Tree("offline_data " , shot_no)


###################GETTING NODE FOR COSINE############################################

EOU = myTree.getNode('EOU')

###################STORING TIMESTAMP DATA###########################################
for i in range(0,len(Voltage)):
	#storing data samples
	EOU_val = Voltage[i]
	timestamp_int64_val = timestamp[i]
	EOU.putRow(10000, Float64(EOU_val), float64(timestamp_int64_val))






###################CHANNEL_2############################################

###################TREE OPERATION############################################
myTree = Tree("offline_data " , shot_no)


###################GETTING NODE FOR RANDOM############################################

IOU = myTree.getNode('IOU')

###################STORING TIMESTAMP DATA###########################################
for i in range(0,len(Current)):
	#storing data samples
	Current_val = Current[i]
	timestamp_int64_val = timestamp[i]
	IOU.putRow(10000, Float64(Current_val), float64(timestamp_int64_val))





###################CHANNEL_3############################################

###################TREE OPERATION############################################
myTree = Tree("offline_data " , shot_no)

###################GETTING NODE FOR SINEWAVE############################################

DC_LINK = myTree.getNode('DC_LINK')

###################STORING TIMESTAMP DATA###########################################
for i in range(0,len(DC_Link)):
	#storing data samples
	DC_LINK_val = DC_Link[i]
	timestamp_int64_val = timestamp[i]
	DC_LINK.putRow(10000, Float64(DC_LINK_val), float64(timestamp_int64_val))






###################CHANNEL_4############################################

###################TREE OPERATION############################################
myTree = Tree("offline_data " , shot_no)

###################GETTING NODE FOR SAWTOOTH############################################

DUTY_CYCLE = myTree.getNode('DUTY_CYCLE')

###################STORING TIMESTAMP DATA###########################################
for i in range(0,len(Duty_Cycle)):
	#storing data samples
	DUTY_CYCLE_val = Duty_Cycle[i]
	timestamp_int64_val = timestamp[i]
	DUTY_CYCLE.putRow(10000, Float64(DUTY_CYCLE_val), float64(timestamp_int64_val))






