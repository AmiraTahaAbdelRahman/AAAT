import sys
from scapy.all import*
import datetime 
p=sniff(count=1)
#functions to get packet time, hexa view and pcapy file
print(datetime.datetime.now().time())
#returns pcapy file
wrpcap('sniffed.pcap', packets) 
#hexdump returns a list and prints it automatically so we use dump=true to return a string and be able to use it in gui   
s=hexdump(p[0],dump=True)
print(s)    