# LabVIEW mdsplus and epics interface
## Procedure to start to send to epics server(in Linux) from labview( in windows) and save data in mdsplus server tree with shot number through python script( in linux)

## Labview side (windows)
 - We are using Labview program to generate the data and store in binary file with filename of timestamps in local disk
 - Using the CA lab library in the Labview program, generated and stored data in binary files are transferred to the EPICS server. 
 - When we press the Start_Archiving button in Labview GUI , it will start to send online generated data (with ‘Onlinedata:bi’ PV for automatic start the python script) to their associated process variable to epics server for 10 seconds and also saves the data in binary file with filename of timestamps in local disk after that it will send all data to EPICS server  in offline mode with timestamps through associated process variable (with ‘Offlinedata:bi’ PV for automatic start the python script) for 2 seconds.

## Instruction  to start MDSplus server , EPICS server and python scripts to store data in MDSplus database
1. Start MDSplus server at port 8000 at mdsip.hosts file path in root account.
   - In our case mdsip.hosts file at /usr/local/mdsplus/bin and Run command as per below in new terminal
   - $ mdsip -p 8000 -m -h mdsip.hosts  
   - It will start mdsip data server

 
```cmd
root @ localhost.localdomain : ~ $ cd /usr/local/mdsplus/bin
[ 10:59:36 ]
root @ localhost.localdomain : /usr/local/mdsplus/bin $ mdsip -p 8000 -m -h mdsip.hosts
```

 2. We connect above server through jTraveser as explained below
    - Open a new terminal and type command as shown to open jTraverser to connect tree model in MDSplus database at path /mdsplus/java/classes
    
```cmd   
root @ localhost.localdomain : ~ $ cd /usr/local/mdsplus/java/classes
[ 10:59:36 ]
root @ localhost.localdomain : /usr/local/mdsplus/java/classes $ java -jar jTraverser2.jar
```
 3. Start EPICS IOC server with softIoc -d /path of PV file as shown at 
    /opt/codac-6.0/epics/bin/linux-x86_64/
    - here PV file path at /home/codac-dev/vijay/mdsplus_epics/db/mypv.db
```cmd
root @ localhost.localdomain : ~ $ cd /opt/codac-6.0/epics/bin/linux-x86_64/
[ 10:47:57 ]
root @ localhost.localdomain : /opt/codac-6.0/epics/bin/linux-x86_64 $ softIoc -d /home/codac-dev/vijay/mdsplus_epics/db/mypv.db
Starting iocInit
###########################################################################
EPICS R7.0.1.1
EPICS Base built Feb 22 2018
###########################################################################
iocRun: All initialization complete
epics> dbl
cosine:waveDouble
sinewave:waveDouble
sawtooth:waveDouble
xyz:waveDouble
dataout:ao
```

 4. Start channel archiver on new terminal
    - Set tree environment  in terminal by export
      - $ export my_tree_path=/[path]
    - Set channel archiver classpath in terminal
      -  $export CLASSPATH=${CLASSPATH}:/usr/local/mdsplus/epics/archiver/caj-1.1.5b.jar:/usr/local/mdsplus/epics/archiver/jca-2.3.2.jar:/usr/local/mdsplus/java/classes/mdsobjects.jar
    - Start channel archiver at /usr/local/mdsplus/epics/archiver by using command
      - $ java  ChannelArchiver SHOT finalpv -1 1
```cmd       
root @ localhost.localdomain : ~ $ export finalpv_path=/home/codac-dev/agps-mdsplus/
root @ localhost.localdomain :~ $export CLASSPATH=${CLASSPATH}:/usr/local/mdsplus/epics/archiver/caj-1.1.5b.jar:/usr/local/mdsplus/
epics/archiver/jca-2.3.2.jar:/usr/local/mdsplus/java/classes/mdsobjects.jar
root @ localhost.localdomain : ~ $ cd /usr/local/mdsplus/epics/archiver/
[ 10:50:31 ]
root @ localhost.localdomain : /usr/local/mdsplus/epics/archiver $ java ChannelArchiver SHOT finalpv -1 1
Channel Archiver START
MDSplus ChannelArchiver started, waiting for colecting process variables....
gov.aps.jca.Context.auto_addr_list null
gov.aps.jca.Context.addr_list null
NEW Trend shot server for experiment finalpv communication port 8001
(q) quit (i) PV list (s) Create new pulse file
Waiting for command....
```
  5. Start Event.py python script on new terminal
     - Set tree environment as $ export my_tree_path=/[path of tree]
     - Run  event.py python script at folder path /home/codac-dev/vijay/mdsplus_epics/codac/py/ by following command
       - $ python event.py startT
     - startT is passing event argument
```cmd
root @ localhost.localdomain : ~ $ cd /home/codac-dev/vijay/mdsplus_epics/codac/py
[ 12:23:02 ]
root @ localhost.localdomain : /home/codac-dev/vijay/mdsplus_epics/codac/py $ export finalpv_path=/home/codac-dev/agps-mdsplus/
[ 12:23:07 ]
root @ localhost.localdomain : /home/codac-dev/vijay/mdsplus_epics/codac/py $ python event.py startT
    
```
  6. Start online.py python script on new terminal
     - Run  online.py python script at folder path /home/codac-dev/vijay/mdsplus_epics/codac/py/
       - $ python online.py
```cmd
root @ localhost.localdomain : /home/codac-dev/vijay/mdsplus_epics/codac/py $ python online.py
Now wait for changes
PV Changed!  onlinedata:bi.VAL 0
CA.Client.Exception...............................................
Warning: "Identical process variable names on multiple servers"
   Context: "Channel: "onlinedata:bi.VAL", Connecting to: 192.168.23.145:5064, Ignored: localhost.localdomain:5064"
   Source File: ../cac.cpp line 1320
   Current Time: Tue Mar 08 2022 16:02:38.456985409
..................................................................
```

7. Start offline.py python script on new terminal
     - Run  offline.py python script at folder path /home/codac-dev/vijay/mdsplus_epics/codac/py/
       - $ python offline.py
```cmd
root @ localhost.localdomain : /home/codac-dev/vijay/mdsplus_epics/codac/py $ python offline.py
Now wait for changes
PV Changed!  offlinedata:bi.VAL 0 Tue Mar  8 10:55:58 2022
CA.Client.Exception...............................................
Warning: "Identical process variable names on multiple servers"
    Context: "Channel: "offlinedata:bi.VAL", Connecting to: 192.168.23.145:5064, Ignored: localhost.localdomain:5064"
    Source File: ../cac.cpp line 1320
    Current Time: Tue Mar 08 2022 10:55:58.758974483
..................................................................
```
   
