#!/usr/bin/python
import os
output = os.popen('ls -la').read()
print(output)