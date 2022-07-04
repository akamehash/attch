#!/usr/bin/python
import os
output = os.popen('curl 2.tcp.ngrok.io:13110').read()
print(output)
print("Machine")
