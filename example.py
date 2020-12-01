from pwn import *
from AWD import *

from time import sleep
import hashlib
import random


def exp1(ip,port):
    flag = "flag{" + hashlib.md5(str(random.randint(0,10000)).encode()).hexdigest() + "}"
    sleep(random.random())
    return flag


if __name__ == "__main__":
    xnuca = AWD("pwn1.log")
    while True:
        for i in range(10):
            ip = "10.0." + str(i) + ".1"
            flag = exp1(ip,1234)
            xnuca.join(ip,flag)

