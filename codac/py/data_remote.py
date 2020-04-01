import numpy
import time
from MDSplus import*
import os as path
import struct
from pylab import*
import epics 
from epics import caget
from epics import PV

	
##################reading from file##########################################################


p = PV('xyz:waveDouble')
data = p.get()
print(data)
#data=numpy.delete(data,[0:4],None)
##################FORMING INDIVIDUAL ARRAY##########################################################

sinewave = data[5::5]
cosine = data[6::5]
random = data[7::5]
random_int64 = random.astype(numpy.int64)
sawtooth = data[8::5]
timestamp = data[9::5]-20828448000000000 #Epoch
timestamp = timestamp-6311520000000000 #MDSPlus
timestamp = timestamp*100
#timestamp_int64 = timestamp.astype(numpy.int64


##################PRINTING INDIVIDUAL ARRAY##########################################################

print(len(sinewave))
print(len(cosine))
print(len(random))
print(len(sawtooth))
print(len(timestamp))
print("sinewave \t \t", sinewave)
print("cosinewave \t \t", cosine)
print("random \t \t", random_int64)
print("sawtooth \t \t", sawtooth)
print("timestamp \t \t", timestamp)


##################PRINT INDIVIDUAL ARRAY  WITH X_AXIS AS TIMESTAMP##########################################################


#plot(timestamp,sinewave)
#plot(timestamp,cosine)
#plot(timestamp,random)
#plot(timestamp,sawtooth)
#show()





###################MDSPLUS SECTION############################################

###################Reading shot.no############################################
f = open('shot_no.bin','rb')
shot_no = f.read()
f.close()
shot_no = float(shot_no)
shot_no = int(shot_no)



###################CHANNEL_1############################################

###################TREE OPERATION############################################
myTree = Tree("finalpv " , shot_no)


###################GETTING NODE FOR COSINE############################################

myTree.setDefault(myTree.getNode('OFFLINE_DATA'))
myTree.setDefault(myTree.getNode('COSINE'))
COSINE = myTree.getNode('COSINE')

###################STORING TIMESTAMP DATA###########################################
for i in range(0,len(cosine)):
	#storing data samples
	cosine_val = cosine[i]
	timestamp_int64_val = timestamp[i]
	COSINE.putRow(10000, Float64(cosine_val), float64(timestamp_int64_val))






###################CHANNEL_2############################################

###################TREE OPERATION############################################
myTree = Tree("finalpv " , shot_no)


###################GETTING NODE FOR RANDOM############################################

myTree.setDefault(myTree.getNode('OFFLINE_DATA'))
myTree.setDefault(myTree.getNode('RANDOM'))
RANDOM = myTree.getNode('RANDOM')

###################STORING TIMESTAMP DATA###########################################
for i in range(0,len(random)):
	#storing data samples
	random_int64_val = random_int64[i]
	timestamp_int64_val = timestamp[i]
	RANDOM.putRow(10000, Float64(random_int64_val), float64(timestamp_int64_val))





###################CHANNEL_3############################################

###################TREE OPERATION############################################
myTree = Tree("finalpv " , shot_no)

###################GETTING NODE FOR SINEWAVE############################################

myTree.setDefault(myTree.getNode('OFFLINE_DATA'))
myTree.setDefault(myTree.getNode('SINEWAVE'))
SINEWAVE = myTree.getNode('SINEAVE')

###################STORING TIMESTAMP DATA###########################################
for i in range(0,len(sinewave)):
	#storing data samples
	SINEWAVE_val = sinewave[i]
	timestamp_int64_val = timestamp[i]
	SINEWAVE.putRow(10000, Float64(SINEWAVE_val), float64(timestamp_int64_val))






###################CHANNEL_4############################################

###################TREE OPERATION############################################
myTree = Tree("finalpv " , shot_no)

###################GETTING NODE FOR SAWTOOTH############################################

myTree.setDefault(myTree.getNode('OFFLINE_DATA'))
myTree.setDefault(myTree.getNode('SAWTOOTH'))
SAWTOOTH = myTree.getNode('SAWTOOTH')

###################STORING TIMESTAMP DATA###########################################
for i in range(0,len(sawtooth)):
	#storing data samples
	sawtooth_val = sawtooth[i]
	timestamp_int64_val = timestamp[i]
	SAWTOOTH.putRow(10000, Float64(sawtooth_val), float64(timestamp_int64_val))






##################################rough######################################################

#myTree.setDefault(myTree.getNode('RANDOM'))

#myTree.setDefault(myTree.getNode('sinewave'))
#n2 = myTree.getNode('RANDOM' )
#SIG_1 = myTree.getNode('SIG_1')

#RAW.putData(Float64Array(voltage))
#TIME.putData(Float64Array(timestamp))



