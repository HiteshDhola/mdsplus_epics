# LabVIEW mdsplus and epics interface
## Instruction  to start MDSplus server , EPICS server and python scripts to store data in MDSplus database
1. Start MDSplus server at port 8000 at mdsip.hosts file path in root account.
   - In our case mdsip.hosts file at /usr/local/mdsplus/bin and Run command as per below in new terminal
   - $ mdsip -p 8000 -m -h mdsip.hosts  
   - It will start mdsip data server

 
```
      root @ localhost.localdomain : ~ $ cd /usr/local/mdsplus/bin
      [ 10:59:36 ]
      root @ localhost.localdomain : /usr/local/mdsplus/bin $ mdsip -p 8000 -m -h mdsip.hosts
```
 2. We connect above server through jTraveser as explained below
    - Open a new terminal and type command as shown to open jTraverser to connect tree model in MDSplus database at path /mdsplus/java/classes
```   
    root @ localhost.localdomain : ~ $ cd /usr/local/mdsplus/java/classes
    [ 10:59:36 ]
    root @ localhost.localdomain : /usr/local/mdsplus/java/classes $ java -jar jTraverser2.jar
```
 3. Start EPICS IOC server with softIoc -d /path of PV file as shown at 
    /opt/codac-6.0/epics/bin/linux-x86_64/
    - here PV file path at /home/codac-dev/vijay/mdsplus_epics/db/mypv.db
```
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
```      
    root @ localhost.localdomain : ~ $ export finalpv_path=/home/codac-dev/agps-mdsplus/
    root @ localhost.localdomain :~ $export CLASSPATH=${CLASSPATH}:/usr/local/mdsplus/epics/archiver/caj-1.1.5b.jar:/usr/local/mdsplus/epics/archiver/jca-2.3.2.jar:/usr/local/mdsplus/java/classes/mdsobjects.jar
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
     - Run  event.py python script at folder path /home/codac-dev/vijay/mdsplus_epics/codac/py by following command
       - $ python event.py startT
     - startT is passing event argument
```
    root @ localhost.localdomain : ~ $ cd /home/codac-dev/vijay/mdsplus_epics/codac/py
    [ 12:23:02 ]
    root @ localhost.localdomain : /home/codac-dev/vijay/mdsplus_epics/codac/py $ export finalpv_path=/home/codac-dev/agps-mdsplus/
    [ 12:23:07 ]
    root @ localhost.localdomain : /home/codac-dev/vijay/mdsplus_epics/codac/py $ python event.py startT
    
```
    

   