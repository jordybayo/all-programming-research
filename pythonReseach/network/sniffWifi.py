#need to install scapy and winpcap
import sys
from scapy.all import *

devices = set()


def packetHandler(pkt):
    if pkt.haslayer(Dot11):

        dot11_layer = pkt.getlayer(Dot11)
        if dot11_layer.addr2 and ( dot11_layer.addr2 not in devices ):
            deices.add(dot11_layer.addr2)
            print( len(devices), dot11_layer.addr2)


sniff(iface = sys.argv[1], count = int(sys.argv[2]), prn=packetHandler)

