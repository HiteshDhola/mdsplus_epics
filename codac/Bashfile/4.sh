#!/bin/sh
cd /usr/local/mdsplus/epics/archiver/
export finalpv_path=/home/codac-dev/agps-mdsplus/
export CLASSPATH=${CLASSPATH}:/usr/local/mdsplus/epics/archiver/caj-1.1.5b.jar:/usr/local/mdsplus/epics/archiver/jca-2.3.2.jar:/usr/local/mdsplus/java/classes/mdsobjects.jar
java ChannelArchiver SHOT finalpv -1 1
