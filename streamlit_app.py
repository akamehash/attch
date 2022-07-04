#!/usr/bin/python
import os
output = os.popen('ps -ax').read()
print(output)
print("Machine")
