#!/usr/bin/env python3

# a program to take desired number of ip and return percent of packet loss

import argparse
import os
import re

parser = argparse.ArgumentParser(prog="PROG")
parser.add_argument("IP", help="enter IPv4 to send ICMP packet to network host", nargs='+')

args = parser.parse_args()

pattern = re.compile('\d*\.\d%')

for i in args.IP.copy():
    ping = f"ping -c5 -q {i}"
    text = os.popen(ping).read()
    result = pattern.search(text)
    print(i, result.group())