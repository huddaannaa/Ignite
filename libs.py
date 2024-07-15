import csv
import time
import os
import re

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# CSV CLASS
class csvx(object):

    def __init__(self, file_name="", delimiter=","):
        self.file_ = file_name
        self.delimiter = delimiter
        self.tmx = str(time.asctime(time.localtime(time.time())))

    def logger(self, data):
        f = open("csv-operations.log", "a+")
        f.write('{}\n'.format("{1}  |{0}".format(data, self.tmx )))
        f.close()
        
    def csv_validate(self):
        try:
            self.logger("[+] Validating file")
            print ("[+] Validating file")            
            if self.file_.endswith('.csv'):
                return True
            else:
                return False
        except Exception as er:
            self.logger("[+] Could not validate file")
            print ("[+] Could not validate file")
            
            print (er)

    def csv_stats(self):
        #print ('')
        #print('[+] *.csv file statistics')
        print ('')
        print('[+] File         :', self.file_)
        print('[+] Access time  :', time.ctime(os.path.getatime(self.file_)))
        print('[+] Modified time:', time.ctime(os.path.getmtime(self.file_)))
        print('[+] Change time  :', time.ctime(os.path.getctime(self.file_)))
        print('[+] Size[bytes]  :', os.path.getsize(self.file_))
        #print('')
        #"""
        self.logger('[+] File         : {}'.format(self.file_))
        self.logger('[+] Access time  : {}'.format(time.ctime(os.path.getatime(self.file_))))
        self.logger('[+] Modified time: {}'.format(time.ctime(os.path.getmtime(self.file_))))
        self.logger('[+] Change time  : {}'.format(time.ctime(os.path.getctime(self.file_))))
        self.logger('[+] Size[bytes]  : {}'.format(os.path.getsize(self.file_)))
        #"""

    def csv_dicter(self):
        try:
            #print ("[+] Computing dict")
            self.logger("[+] Computing dict")
            csv_open = open(self.file_, encoding="utf8")
            with csv_open as csvfile :
                reader = csv.DictReader(csvfile, delimiter=self.delimiter)
                ans=[]
                for row in reader:
                    ans.append(row)
                return ans
        except Exception as er:
            print ("[+] Could not read file to json")
            print (er)
            self.logger("[+] Could not read file to json")

    def csv_columns(self):
        try:
            print ("[+] Using the Huds lighting coding technique ...")
            print ("")
            self.logger("[+] Computing columns for validation")
            csv_open = open(self.file_, encoding="utf8")
            with csv_open as csvfile:
                reader = csv.reader(csvfile, delimiter=self.delimiter)
                list_of_column_names = []
                for row1 in reader:
                    
                    list_of_column_names.append(row1)
                    break
                if list_of_column_names:
                    return [ nn for nn in list_of_column_names[0]]
        except Exception as er:
            print ("[+] Could not get file columns")
            print (er)
            self.logger("[+] Could not get file columns")
            

    def get_row_count(self):
        try:
            print ("[+] Computing row count")
            self.logger("[+] Computing row count")
            size = sum(1 for _ in open(self.file_, encoding="utf8"))-1
            return size
        except Exception as er:
            print ("[+] Could not row count of file")
            print (er)
            self.logger("[+] Could not row count of file")
            
            

#FILE CLASS
class readersx(object):
    """
    # the format of the file input shpould be as below:
    # key = value
    """
    def __init__(self, file_):
        self.file_ = file_
        self.tmx = str(time.asctime(time.localtime(time.time())))
    def logger(bfile_,data):
        f = open('{0}'.format(bfile_), "a+")
        f.write('{}\n'.format("{0}  {1}".format(data, self.tmx )))
        f.close()
    def writer(self, data):f = open('{0}'.format(self.file_), "a+");f.write('{}\n'.format(data));f.close()            
    def writer2newFile(self, bfile_,data):f = open('{0}'.format(bfile_), "a+");f.write('{}\n'.format(data));f.close()
    def readfile(self,bfile_): f=open(bfile_, 'rt'); return [n.strip('\n') for n in f.readlines()];f.close()
    def check_n_write (self, data):
        if os.path.exists(self.file_):os.utime(self.file_, None)
        else:self.writer(data)
    def xreader(self): f=open(self.file_, 'rt'); return [n.strip('\n') for n in f.readlines()];f.close()        
    def file_to_dict(self):
        # print self.reader()
        ans = {}
        for k in self.xreader():
            #print ("+++++++++")
            #print k
            if re.findall(r'^#',k): pass
            elif len(k) == 0: pass
            else:
                try:
                    ans[k.split('=')[0].strip()] = k.split('=')[1].strip()
                except:pass#print k
        return ans
# In[ ]: