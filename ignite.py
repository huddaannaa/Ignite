from params import *
import os
import json
import warnings
import sys
import getpass
import os.path
import signal
import time
from elasticsearch import helpers, Elasticsearch, RequestsHttpConnection
from func import clsr, touch, hashfile,make_parce, str2bool, timx, handler, csv_parse, mappings_get_value, mapping_list_keys, rollover
from art import inpt, cat, success, introm, msd
import shutil



warnings.filterwarnings("ignore")
signal.signal(signal.SIGINT, handler)


#clear screen where linux or windows
clsr()



#readme
if readme:
        print("")
        print ("")
        print (msd)
        print ("")
        print ("")
        sys.exit()



#flush program
if xflush:
        print ("")
        print ("")
        print ("")
        print ("[+] This option will wipe the application's") 
        print ("    data and return the program to its original state")
        print ("")
        print ("[+] IMPORTANT: Please backup signature.db if tool is used in production")
        print ("[+] Hence:")
        print ("")
        starx=""
        try:
                starx= input("[+] Are you sure of this decision \n    Hit the {} key to continue \n    or type exit to quit the application: ".format(bcolors.OKGREEN+"*ENTER*"+bcolors.ENDC ))
        except EOFError:pass    
        if starx.lower() == "exit":
                print ("")
                print ("[+] The system will gracefully exit in peace...")
                print ("")
                sys.exit()
        elif starx.lower() == "":
                pass
        else:
                print ("")
                print ("[+] You typed random characters and hence,")
                print ("[+] the system will gracefully exit in peace...")
                print ("    Thank you ...")
                print ("")
                sys.exit()

        print ("")
        print ("")
        print ("")
        print ("[+] Clearing application data ..")
        print ("    and meta files ..")
        print ("")
        print ("")
        print ("")
        
        try:
                shutil.rmtree(os.path.join('_event-tracker_'))
        except:pass
        
        try:
                shutil.rmtree(os.path.join('_json-output_'))
        except:pass
        try:
                os.remove("csv-operations.log")
        except:pass
        try:
                os.remove("success.log")
        except:pass
        try:
                os.remove("signature.db")
        except:pass
        try:
                os.remove("error.log")                
        except:pass
        
        print ("[+] Done ...")
        print ("")
        sys.exit()


if elasticsearch:
        try:os.mkdir(os.path.join('_event-tracker_'))
        except:pass
else:
        try:os.mkdir(os.path.join('_json-output_'))
        except:pass


#introduction
#======================
print ("")
print (cat)
#print ("")
print ("                          {0}".format(version_c))
print (introm)



starx=""
try:
    starx= input("[+] Hit the {} key to continue \n    or type exit to quit the application: ".format(bcolors.OKGREEN+"*ENTER*"+bcolors.ENDC ))
except EOFError:pass    
if starx.lower() == "exit":
    print ("")
    print ("[+] The system will gracefully exit in peace...")
    print ("")
    sys.exit()
elif starx.lower() == "":
    pass
else:
    print ("")
    print ("[+] You typed random characters and hence,")
    print ("[+] the system will gracefully exit in peace...")
    print ("    Thank you ...")
    print ("")
    sys.exit()



#clear screen where linux or windows
clsr()



#this is not a csv file dependant operation
#[OPTIONAL] param
if list_parcers:
        print ("")
        print ("")
        try:
                print ("")
                print ("[+] The list of modules(parcers) are: ")
                print ("")
                if len(mapping_list_keys()) != 0:
                    kl=0
                    for jjj in list(mapping_list_keys()):
                        print (bcolors.OKGREEN+"    [{}]".format(str(kl)),jjj+bcolors.ENDC)
                        kl=kl+1
                else:
                    print ("[+] There are no modules(parcers) to display")
                print ("")
        except Exception as err:
                print (err)
                print ("")
        finally:
                sys.exit()
else:pass



#checking crusial files
#======================
print ("")
print ("[+] Loading application files ..")
print ("")
if os.path.isfile(fields):
    print ("    ",fields)
    if os.path.isfile(settings_file):
        print ("    ",settings_file)
        if os.path.isfile(parce_file):
            print ("    ",parce_file)
        else:
            print ("    ",settings_file," is not available")
            print ("[] Please rectify or contact admin")
            print ("")
            sys.exit()
    else:
        print ("    ",parce_file," is not available")
        print ("[] Please rectify or contact admin")
        print ("")
        sys.exit()
else:
    print ("    ",fields," is not available")
    print ("[] Please rectify or contact admin")
    print ("")
    sys.exit()
print ("")
    
    
    

print ("[+] Validating application settings")
try:
    params = readersx(settings_file)
    data = params.file_to_dict()
    addr  =    data["addr"].split(",")    
    if index: print ("[+] The app will use {} as index".format(index));pass
    else: index =    str(data["index"]).strip()
    doc_type = str(data["doc_type"]).strip()
    ssl      = str2bool(data["ssl"])
    certs    = str2bool(data["certs"])
    security = str2bool(data["security"])
    rollover_time = str(data["index_rollover"])
    print ("[+] All configurations cleared")
    print ("[+] App is proceeding to validate the CSV")
    print ("[+] {} provided as input".format(user_n))
except Exception as err:
    print ("[+] Please review settings.ini for missing configuration")
    print (err)
    ecs.writer2newFile("error.log", "Please review settings.ini for missing configuration")
    ecs.writer2newFile("error.log", err)


addr_c = bcolors.OKBLUE+str(addr)+bcolors.ENDC




#csv validation
#====================
if cs.csv_validate():      
    #print ("")
    print ("[+] {} input file is a csv ...".format(file_basename_c))
    print ("[+] Hence, the application will proceed ...")
    print ("    [loading] ...")
    #print ("[+]")
    print ("    Computing CSV file statistics: ")
    cs.csv_stats()
    pass
else:    
    print ("")
    print ("[+] The input file is not a csv ...")
    print ("[+] Hence, the application will exit ...")
    print ("                    Yours sincerely,")
    print ("                    Hud Daannaa ..")
    sys.exit()






#this will go [optional]
# creating a parcer template
#===========================

if create_parce:
    mk="""
Below is the parcer template generated
from the input csv file: {0}.
Copy this template and fill in the required
fields (|ECS recommended) that you wish to 
populate into elasticsearch.

After, filling in the fields, please make
sure to add the newly created fields to 
fields.db and then validate {0} with the -g
parameter on ignite...
""".format(bcolors.OKBLUE+file_basename+bcolors.WARNING)
    print (bcolors.WARNING+mk+bcolors.ENDC)
    csv_collss = cs.csv_columns()
    parc = make_parce(create_parce, csv_collss)
    print ("")
    print (bcolors.OKCYAN+parc+bcolors.ENDC)
    print ("")
    sys.exit()







#this will go [optional]
#arg to get columns and validate only
if get_csv_columns:
    print ("")
    print ("The function will compute and check the columns in the CSV file")
    print ("that was provided at input ...")
    ssge="""
    IMPORTANT:
    
    "The CSV columns available in
    {} are below, hence, these are 
    the original columns present 
    in the original CSV:   
    """.format(file_basename_c)
    print (ssge)
    print ("")
    collss = cs.csv_columns()
    #print ("")
    col_cnt = 0
    for uu in collss:
        print (bcolors.OKCYAN+"     [{}]".format(str(col_cnt+1))+bcolors.ENDC,uu)
        col_cnt=col_cnt+1
    print ("")
    print ("    The csv file has {} columns".format(str(col_cnt)))
    print ("")
    
    #validating columns in a csv
    #get applications columns from fields
    
    
    ssge="""
    IMPORTANT:
    
    "The CSV columns below are 
    extracted from {} and 
    compared to default and custom 
    ECS fields in fields.db which 
    has a relationship with parcer.conf
    the results are below:"
    
    """.format(file_basename_c)
    print (ssge)
    ecs_columns  = ecs.xreader()
    for cols in collss:
        if cols in ecs_columns:
            print (bcolors.OKGREEN+"    (#)Available: [{}]".format(cols)+bcolors.ENDC)
        else:
            print (bcolors.FAIL+"    (X)Unavailable: [{}]".format(cols)+bcolors.ENDC)
    
    print ("")
    print ("    The app will close, since this command is only")
    print ("    used to give an analyst the columns in a given csv ...")
    print ("")
    sys.exit()
else:
    pass






#computing hash file
file_hash = hashfile(file_name)
if elasticsearch:
        ##this will go to
        #get hash of file
        if os.path.isfile("signature.db"):pass
        else:touch("signature.db")

        #print ("")
        for hashz in ecs.readfile("signature.db"):
            try:
                if file_hash in hashz.split("|")[2]:        
                    print ("[+] The file has already been ingested at {}".format(hashz.split("|")[0]))
                    print ("")
                    sys.exit()
                else:pass
            except Exception as err:
                print ("[+] Simply check signature.db for inconsistent characters")
                print ("")
                ecs.writer2newFile("error.log", err)
                sys.exit()
    









if elasticsearch:
        #validating addr
        #default kickback
        if addr:addr=addr
        else:addr=['https://localhost:9200']







if elasticsearch:
        #checking if security is on, use cred or vise versa
        #user and pass validation
        print ("")
        if security == True:
            if username:username=username.strip()          
            else:
                print ("[+] Please check/input username")
                sys.exit()           
            if password:
                password=password.strip()     
            else:
                print ("[+] Please check/input password")
                sys.exit()           
        else:pass









################################################
#===============================================
#the parce effect starts here
#validating columns in a csv
#get applications columns from fields
ecs_columns  = ecs.xreader()
collss = cs.csv_columns()
#print ("")
ssge="""
    IMPORTANT:
    
    "The CSV columns available in
    {} are below, hence, these are 
    the original columns present 
    in the original CSV, the app checks
    to see if the columns are in the right
    template format (ECS) if not the app
    will EXIT, unless a parcer module was
    specified with the '-p <parcer_name>' 
    tag, hence the deduced columns are:   
    """.format(file_basename_c)
print (ssge)
    #print ("")
for cols in collss:
    if cols in ecs_columns:
        print (bcolors.OKGREEN+"    (#)Valid : [{}]".format(cols)+bcolors.ENDC)
    else:
        print (bcolors.FAIL+"    (X)Invalid : [{}]".format(cols)+bcolors.ENDC)
        extt=1
        
        
        
      
      
        
        
        
#triger mssge if not parce
#hence this new modification promises to exit if a filed is not mapped or parced
if extt == 1:
    if not parce:
        print ("")
        print ("[+] please review {}, hence the app will exit now ..".format(file_basename_c))
        print ("[+] due to inconsistent columns")
        print ("")
        sys.exit()
    if parce and parce in mapping_list_keys ():
      
        print ("")
        print (bcolors.WARNING+"    NOTE: Since the parce parameter is enabled: "+bcolors.ENDC)
        print ("          the app will use: [{}]".format(parce_c))
        print ("          as a parcer/mapper")

        #we have  to check if mapping key are in DB
        print ("")
        print ("[+] Verifying parcer **keys&values** ...")
        print ("[+] Inspecting to check wether the [{0}] parcer keys are available in {1}: ".format(parce_c, file_basename_c))
        print ("")
        #checking if mapping values are in DB
        cols_keys_a=[]
        cols_keys_u=[]
        #this loop is supposed to compile the columns into a list
        for cols_keys in collss:
            if cols_keys in list(mappings_get_value(parce).keys()):
                cols_keys_a.append(cols_keys)
            else:
                cols_keys_u.append(cols_keys)               
                
         #this loop is just to display colums
        if len(cols_keys_a) != 0:         
            for cols_keysa in cols_keys_a:
                print (bcolors.OKGREEN+"    (#)Available: [{}]".format(cols_keysa)+bcolors.ENDC)
        
        if len(cols_keys_u) != 0:
            for cols_keysu in cols_keys_u:
                print (bcolors.FAIL+"    (X)Unavailable: [{}]".format(cols_keysu)+bcolors.ENDC)                
            print ("")
            print ("[+] Some keys in the parcer: [{0}] do not match the original columns in the csv: {1}".format(parce_c, file_basename_c))
            print ("[+] Please check if the parcer used in the correct one ...")
            print ("[+] Please do so and proceed ...")
            print ("")
            sys.exit(0)
        
        ##########
        
        print ("")
        print ("[+] Inspecting to check wether the [{}] parcer values are in the DB of fields: ".format(parce_c))
        print ("[+] Hence, this section will display all fields/values in the group/parcer..")
        print ("")
        #checking if mapping values are in DB
        mcols_a=[]
        mcols_u=[]
        #this loop is supposed to compile the columns into a list
        for mcols in list(mappings_get_value(parce).values()):
            if mcols in ecs_columns:
                mcols_a.append(mcols)
            else:
                mcols_u.append(mcols)               
                
         #this loop is just to display colums
        if len(mcols_a) != 0:         
            for mcolsa in mcols_a:
                print (bcolors.OKGREEN+"    (#)Available: [{}]".format(mcolsa)+bcolors.ENDC)
        
        if len(mcols_u) != 0:
            for mcolsu in mcols_u:
                print (bcolors.FAIL+"    (X)Unavailable: [{}]".format(mcolsu)+bcolors.ENDC)                
            print ("")
            print ("[+] Some values in the parcer: [{0}] are not registered in the fields.db".format(parce_c))
            print ("[+] Please do so and proceed ...")
            print ("")
            sys.exit(0)
    else:
        print ("[+] The wrong module was parced: {}".format(parce_c))
        print ("[+] the app will exit gracefully ...")
        print ("")
        sys.exit()







#parcing will happen  here
#print (mappings["indicator"])
#input_file = csv_parse(parce)
#print (input_file)
print ("")
print ("[+] App will commence parcing")
#print ("")
time.sleep(2)
if parce:
    module=parce
    input_file = csv_parse(module, file_name, delimiter)
else:
    input_file = cs.csv_dicter()







#get the size of the csv file
#print ("")
size="n/a"
try:
    if parce:
        size = len(input_file)
    else:
        size = cs.get_row_count()
    print ("[+] Computed the size of the file: {} rows".format(str(size)))
except:    
    print ("[+] The program was not able to get the size of the file")   
    sys.exit()








#consent
consent="""


        DISCLAIMER:

        The analyst by computer name: {0},
        and provided username: {3}
        has agreed that, if he/she has added any custom 
        fields or parcer/mappings to

          a)fields.db and 
          b)parcer.conf
          
        by specifying the -p option as: {4}
        he/she has properly validated them and 
        can proceed to upload CSV data from {1} 
        into elasticsearch on: {2}
        Hence, 




""".format(user_n_c, file_basename_c, addr_c, username_c, parce_c)
print (consent)
print ("")
starxc=""
try:
    starxc= input("[+] Input YES/NO to continue: ")
except EOFError:pass
if starxc.lower() == "no":
    print ("")
    print ("[+] I do not agree and wish to re-validate my inputs.")
    print ("")
    sys.exit()
elif starxc.lower() == "yes":
    print ("[+] I do agree and wish to proceed...")
    time.sleep(1)
    pass
else:
    print ("")
    print ("[+] PLEASE INPUT YES/NO")
    print ("[+] You typed random characters and hence,")
    print ("[+] the system will gracefully exit in peace...")
    print ("    Thank you ...")
    print ("")
    sys.exit()

#clear screen where linux or windows
#clsr()





if elasticsearch:
        #get password
        print ("")
        password  = getpass.getpass(prompt="\n\nInput password for the {} : ".format(username_c))






if elasticsearch:
        print ("")
        print("[+] Connecting to ES instance ...")
        if security:
            #connection to elastic instance
            try:
                es = Elasticsearch(addr, http_auth=(username, password), connection_class=RequestsHttpConnection,  use_ssl=ssl, verify_certs=certs)
                print ("[+] Configuring elasticsearch instance: {}".format(str(addr_c)))
            except Exception as err:
                print("[+] Could not connect to ES instance")
                ecs.writer2newFile("error.log", "[+] Could not connect to ES instance | reason: ".format(err))
        else:
            #connection to elastic instance
            try:
                es = Elasticsearch(addr)
                print ("[+] Configuring elasticsearch instance: {}".format(str(addr_c)))
            except Exception as err:
                print("[+] Could not connect to ES instance")
                ecs.writer2newFile("error.log", "[+] Could not connect to ES instance | reason: ".format(err))









#reading the whole csv
print ("[+] Uploading data ..")
#print ("=================")
print ("")
#input_file = cs.csv_dicter()
cnt=0

if elasticsearch:
        index = "{0}_{1}".format(index, rollover(rollover_time))
else:
        index = "n/a"

for row in input_file:            
    
    try:
        chr=0

        #print (row)
        #print (type(row))
        #dataxt=json.dumps(row)

        #net
        row["@version"] = "1"
        row["analyst.user_name"] = str(user_n)
        row["analyst.host_name"] = str(host_name)
        row["analyst.host_ip"] = str(host_ip)
        row["analyst.host_os_platform"] = str(host_architecture)     
        row["analyst.host_architecture"] = str(host_architecture)

        row["event.module"]  = "hudcsvparcer"
        row["event.dataset"] = data_source_name
        row["event.created"] = timerx
        row["event.start"] = timerx
        row["event.end"] = timerx


        row["@timestamp"]    = timerx
        row["agent.id"] = "b7db14b2-5e1e-hud-4b88-a685-2681c9c5bc9e"
        row["agent.ephemeral_id"] = "78e1c6e4-9a89-47f4-aea8-a5a5ea32150b-07d62c2a-58f3-4c41-83a0-5e91232dd92e"
        row["agent.type"] = "csvparcer"
        row["agent.hostname"] = str(host_name)
        row["agent.name"] = str(host_name)
        row["agent.version"] = "{}".format(version_)
        row["ecs.version"] = "{}".format(ecs_version)



        dataxt=json.dumps(row)



        #send to elastic
        if elasticsearch:
                es.index(index=index, doc_type=doc_type, body=dataxt)
                ecs.writer2newFile(os.path.join('_event-tracker_', event_tracker_location), "filename: {2}, index: {3} [{0}/{1}] rows_sent!, message: {4}\n".format(str(cnt+1), str(size), file_name, index, dataxt))
        else:
                ecs.writer2newFile(os.path.join('_json-output_', "{0}_{1}_{2}.json".format(file_hash, str(epoch_time), file_basename)), row)
        
        
        print (bcolors.OKCYAN, end="\r", flush=True)
        print ("[{0}/{1}] rows sent !".format(str(cnt+1), str(size)), end="\r", flush=True)
        print (bcolors.ENDC, end="\r", flush=True)




    except Exception as er:
        ecs.writer2newFile("error.log","{4} destination: {5} | filename: {2} | [{0}/{1}] error ! | reason: {3}".format(str(cnt+1), str(size), file_name, er, timx(), destination))
        chr=1
        if "AuthenticationException" in str(er):
            print ("")
            print ("[XXXX] APP WILL SHUTDOWN \n       REASON: {}".format(er))
            print ("")
            sys.exit()
        else:pass
    finally:
        #meta file for success log
        mssge = "{3} destination: {5} | filename: {2} | index: {4} | [{0}/{1}]rows sent !".format(str(cnt+1), str(size), file_name, timx(), index, destination)
    cnt = cnt + 1
    
    
    
    
ecs.writer2newFile("success.log", mssge)

if elasticsearch:
        ecs.writer2newFile("signature.db", "{0}|{1}|{2}".format(timx(), file_name, file_hash))




if mssge == "No csv recorded":
    print (mssge)
if chr == 1:
    print ("[] Please check error.log for some vital information")
print ("")
#print (success)
print ("")
print (inpt)
print ("")
print ("""[+] Knowledge is in thin space ..
    and our friend the rat knows ...

""")