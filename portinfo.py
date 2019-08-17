#!/usr/bin/env python3

import sys
import webbrowser

def load():
    ports = {}
    with open("portList.csv") as file: #read .CSV file with port info
        file.readline()
        for i in file.readlines():
            line = i.split(","); line.pop()
            if str(line[0]) in ports: #To store multiple port apllication under 1 port
                ports[str(line[0])] = ports[str(line[0])] + [{"tcp": line[1], "udp": line[2], "name": line[3].replace("\xa0", " ")}]
            else: #To store 1 port application under 1 port
                ports.update({ str(line[0]): [{"tcp": line[1], "udp": line[2], "name": line[3].replace("\xa0", " ")}] })
    return ports

def portinfo(arg):
    for i in ports[arg]:
        print("*"*25)
        print("TCP: " + i['tcp'])
        print("UDP: " + i['udp'])
        print("Name/Smal Description: " + i['name'])

if __name__ == '__main__':
    errmsg = """Please follow the following format;
    ./portinfo.py [port number] returns Port info
    ./portinfo.py -s [port number] returns Port info and Searches more info online
    ./portinfo.py -h returns info on the input format"""
    ports = load()
    try:
        if len(sys.argv) == 2 and sys.argv[1] in ports:
            portinfo(sys.argv[1])
        elif len(sys.argv) == 3 and sys.argv[1] == '-s' and sys.argv[2] in ports:
            portinfo(sys.argv[2])
            webbrowser.open('https://www.speedguide.net/port.php?port=' + sys.argv[2])
        elif sys.argv[1] == '-h':
            print(errmsg)
        else :
            print("Port Not found.")
            webbrowser.open('https://www.speedguide.net/port.php?port=' + "".join(sys.argv[1:3]).replace('-s',''))
    except:
        print(errmsg)
