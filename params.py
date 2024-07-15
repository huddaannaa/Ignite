import socket
import platform
from datetime import datetime
import getpass
from args import args
from libs import csvx, readersx, bcolors
import os
import time




#version
#=============
version_ = "v1.16"
version_c = bcolors.FAIL+version_+bcolors.ENDC 
fields   = "fields.db"
settings_file = "settings.ini"
parce_file  = "parcer.conf"
ecs_version = "1.10.0"




#sys meta data
#=============
host_ip           = "n/a"
host_name         = "n/a"
user_n            = "Default_Analyst_1"
host_architecture = "n/a"
host_os_family    = "n/a"
host_os_name      = "n/a"
host_os_version   = "n/a"




try:
    host_ip           = socket.gethostbyname(socket.gethostname())
    host_name         = socket.gethostname()
    user_n            = getpass.getuser()
    host_architecture = platform.architecture()[0]+"_"+platform.architecture()[1]+"_"+platform.machine()
    host_os_family    = platform.system()
    host_os_name      = platform.platform()
    host_os_version   = platform.version()
except:pass




timerx=str(datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ'))[:-4]+"Z"
rollover=str(datetime.now().strftime('%Y_%m_%d_%H'))
namer=str(datetime.now().strftime('%Y%m%d%H%M%S'))


#args variables
password         = "HudSeiduDaannaa"
file_name        = ""
try:
    file_name        = os.path.join(args.csvfile)
except:pass
username         = args.username
index            = args.index
data_source_name = args.data_source_name
get_csv_columns  = args.get_csv_columns
delimiter        = args.delimiter
parce            = args.parce
list_parcers     = args.list_parcers
create_parce     = args.create_parce
elasticsearch    = args.elasticsearch
xflush           = args.flush
readme           = args.readme

file_basename    = os.path.basename(file_name)
file_basename_c    = bcolors.OKBLUE+str(os.path.basename(file_name))+bcolors.ENDC
parce_c            = bcolors.OKBLUE+str(parce)+bcolors.ENDC
username_c         = bcolors.OKBLUE+str(username)+bcolors.ENDC
user_n_c           = bcolors.OKBLUE+str(user_n)+bcolors.ENDC
file_name_c        = bcolors.OKBLUE+str(file_name)+bcolors.ENDC

#Global variables 1
ecs          = readersx(fields)
cs           = csvx(file_name, delimiter)
extt         = 0
chr          = 0
mssge        = "No csv recorded"

event_tracker_location = "{1}_event-tracking-for-{0}.log".format(file_basename, namer)

epoch_time = int(time.time())

#output file section
#===================
if elasticsearch:
    destination = "elasticsearch_instance"
else:
    destination = "json_text_file"
