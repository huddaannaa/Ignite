import hashlib
import sys
from art import license
from libs import csvx
import os
import ast
import time
import json
from params import parce_file, host_os_family
from datetime import datetime

def clsr():
        if host_os_family == "Windows":
            try:os.system('cls')
            except:pass
        elif host_os_family == "Linux":
            try:os.system('clear')
            except:pass
        else:pass

def rollover(formt):
    return str(datetime.now().strftime(formt))

def touch(fname, times=None):
    with open(fname, 'a'):
        os.utime(fname, times)
def hashfile(file_):
        BLOCK_SIZE = 65536              # The size of each read from the file
        file_hash = hashlib.sha256()    # Create the hash object, can use something other than `.sha256()` if you wish
        with open(file_, 'rb') as f:     # Open the file to read it's bytes
            fb = f.read(BLOCK_SIZE)     # Read from the file. Take in the amount declared above
            while len(fb) > 0:          # While there is still data being read from the file
                file_hash.update(fb)    # Update the hash
                fb = f.read(BLOCK_SIZE) # Read the next block from the file
        return (file_hash.hexdigest())  # Get the hexadecimal digest of the hash
def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")
def timx():
    return str(time.asctime(time.localtime(time.time())))
def handler(signum, frame):
    print ("[] Since you pressed CTRL+C ")
    print ("[] This program will terminate gracefully ...")
    print (license)
    sys.exit(1989)

def mappings_get_value (modd):
     
    parcerx=open(parce_file)
    nn=parcerx.read()
    o=nn.replace("\n","").replace("'",'"').strip()
    
    for i in o.split("#"):
        if len(i) != 0:
            t=ast.literal_eval(i.strip())
            if modd in list(t.keys()):
                return (list(t.values())[0])
        
def mapping_list_keys ():
    
    parcerx=open(parce_file)
    nn=parcerx.read()
    o=nn.replace("\n","").replace("'",'"').strip()

    oo=o.split("#")
    kys=[]
    for i in oo:
        if len(i) != 0:
            t=ast.literal_eval(i.strip())
            kys.append(list(t.keys())[0])
        else:pass
    return [ nn for nn in kys]
    

def csv_parse(module, file_name, delimiter):
        json_dicter=""
        try:
            json_dicter = mappings_get_value(module)
        except Exception as de:
            print ("[+] Could no retrieve parcer")
            print ("[+] Reason: {}".format(de))
        print ("")
        print ("[+] This module will parce the csv data into required fields")
        print ("    these are the mappings specified in parcer.conf")
        print ("    the specified fields are ECS recommended")
        print ("")
        
        csp = csvx(file_name, delimiter)
        parcee = csp.csv_dicter()
        
        parced=[]
        try:
            for rws in parcee:
                pc={}
                for key, value in rws.items():
                    if key in json_dicter.keys():
                        #print ("[] Found key: [{}] in the parcer provided".format(key), end="\r", flush=True)
                        pc[json_dicter[key]]=value
                    else:
                        #print ("[] Could not find key: {} in the parcer provided".format(key), end="\r", flush=True)
                        pass
                parced.append(pc)                    
            return parced
        except Exception as err:
            print (err)

def make_parce(module, csv_collss):
    shell_1={}
    shell_2={}
    for u in csv_collss:
        shell_1[u]=""  
        shell_2[module]=shell_1
    shell_2=json.dumps(shell_2,indent=1)
    return ("#\n"+shell_2)