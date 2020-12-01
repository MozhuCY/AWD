import _thread
from time import sleep,time
from submitflag import submit
import random

class AWD:
    def __init__(self,log_file = None):
        random.seed(time())
        if(log_file == None):
            log_file = "".join(random.sample("1234567890abcdef",8)) + ".log"
            print("logfile:%s"%log_file)
        self.log_flag = 1
        self.log_file = open(log_file,"a+")
        self.add_submit_thread()
        self.flag_list = []
    
    def Log(self,ss,lf = 0):
        if lf == 1:
            print(ss)
        self.log_file.write(ss + "\n")
        self.log_file.flush()

    def submit_thread(self):
        while True:
            if len(self.flag_list) != 0:
                for i in self.flag_list:
                    ret = submit(i[1])
                    if(ret == 1):
                        self.Log("[%s:DONE] %s"%(i[0],i[1]))
                        self.flag_list.remove(i)
                    elif(ret == 2):
                        self.Log("[%s:DUP] %s"%(i[0],i[1]))
                        self.flag_list.remove(i)
                    else:
                        self.Log("[%s:ERROR] %s"%(i[0],i[1]))
            else:
                sleep(1)

    def add_submit_thread(self):
        _thread.start_new_thread(self.submit_thread,())

    def join(self,ip,flag):
        self.flag_list.append([ip,flag])
