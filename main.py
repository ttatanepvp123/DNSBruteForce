import socket
import sys
import json
import argparse

parser = argparse.ArgumentParser(description='DNS Brute Force')
parser.add_argument('domain', metavar='domain', type=str, nargs=1,help='domain to subdomain brute force')

args = parser.parse_args()

fileName = "subdomains.list"

with open(fileName) as fp:
    subDomains = fp.read().split("\n")

for subDomain in subDomains:
    try:
        addr = socket.gethostbyname(f"{subDomain}.{args.domain[0]}")
        print(f"{subDomain}.{args.domain[0]} - {addr}")
    except:
        pass