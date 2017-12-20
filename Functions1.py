import sys
from scapy.all import*
p=sniff(count=1,iface="Ralink RT3290 802.11bgn Wi-Fi Adapter",prn=lambda x: x.sprintf("{IP:proto=%IP.proto%}{Raw:%Raw.load%\n}"))
#functions to get source IP destination IP packet length and  protocol
source=p[0][1].src
des=p[0][1].dst
size=p[0][1].len
print(source)
print(dest)
print(size)
# Scapy may replace the value with a more friendly text value for the summary views,
# but not in the values returned for an individual field. so we searched for the values of some protocols
#and changed it ti string by if conditions
#https://en.wikipedia.org/wiki/List_of_IP_protocol_numbers
prot=p[0][1].proto
if(prot==1):
    prottype="ICMP"
elif(prot==6):
    protype="TCP"
elif (prot==17):
    protype="UDP"
elif (prot==54):
    protype="NARP"
print(protype)    
