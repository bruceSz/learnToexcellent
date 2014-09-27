#!/usr/bin/env python
#coding=utf8

import fcntl
import getopt
import logging
import os
import socket
import struct
import sys
import threading
import time

from Queue import Queue
import pcapy

MAX_HASH = 100000
store_queue = Queue(MAX_HASH)

netdev = None
filter_str = None
log_file = "/var/log/sniffer.log"
logger = logging.getLogger(__file__)
file_handler = logging.FileHandler(log_file)
logger.addHandler(file_handler)

def eth_addr(a):
    # convert a string of 6 characters of ethernet address into 
    # a hash separated hex string.
    bytes = map(lambda x:'%.2x'%x,map(ord,a))
    return ":".join(bytes)

def parse_packet(packet):
    # parse ethernet header
    eth_length = 14

    eth_header = packet[:eth_length]

    print eth_header
    eth = struct.unpack('!6s6sH',eth_header)
    eth_protocol = socket.ntohs(eth[2])
    print 'Destination MAC: '+eth_addr(packet[0:6])+\
            'Source MAC:'+eth_addr(packet[6:12])+\
            'Protocol:'+str(eth_protocol)

    if eth_protocol == 8:
        ip_header = packet[eth_length:20+eth_length]

        iph = struct.unpack('!BBHHHBBH4s4s',ip_header)
        version_ihl = iph[0]
        version = version_ihl >> 4
        ihl = version_ihl & 0xF

        iph_length = ihl*4

        ttl = iph[5]
        protocol = iph[6]
        s_addr = socket.inet_ntoa(iph[8])
        d_addr = socket.inet_ntoa(iph[9])

        print "Version:" + str(version)+ 'IP Header Length'+str(ihl)+\
                'TTL :'+str(ttl) + 'Protocol:' +str(protocol)+\
                'Source Address: '+str(s_addr)+\
                'Destination Address: '+str(d_addr)

        if protocol ==6:
            pass
        elif protocol == 1:
            pass
        elif protocol == 17:
            u = iph_length+eth_length
            udph_length=8
            udp_header = packet[u:u+8]

        

    

