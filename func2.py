sys.path.insert(0,'./scapy-master/')
import scapy.all as scapy
import scapy.utils as utils
src=""
dest=""sys.path.insert(0,'./scapy-master/')
import scapy.all as scapy
import scapy.utils as utils
src=""
dest=""
def find_src(summary):
    for x in range(17, 33):
        src+=summary[x]
    print(src)
def find_dest(summary):
    for x in range(37,50):
        dest+=summary[x]
    print(dest)
    
def pkt_handler(pkt):
    content=pkt.show(dump=True)
    summary= pkt.summary()
    hex=utils.hexdump(pkt,dump=True)
    print(content)
    print(summary)
    find_src(summary)
    find_dest(summary)
    print(hex)
pkt= scapy.sniff(iface=None,filter=None,count=3,prn=pkt_handler,store = 0)

    
def pkt_handler(pkt):
    content=pkt.show(dump=True)
    summary= pkt.summary()
    hex=utils.hexdump(pkt,dump=True)
    print(content)
    print(summary)
    find_src(summary)
    find_dest(summary)
    print(hex)
pkt= scapy.sniff(iface=None,filter=None,count=3,prn=pkt_handler,store = 0)