#!/bin/bash

# a program to take desired number of ip and return percent of packet loss

for ip in $@
do
    echo -n "$ip " ; ping -c5 -q $ip | grep -o '\d*\.\d%'
done