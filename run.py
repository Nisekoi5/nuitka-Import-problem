
import os
import sys

print(sys.path)
exe_dir = sys.path[1]
lib_dir = os.path.join(exe_dir, "lib")
sys.path.append(lib_dir)
print(sys.path)

import requests
print(requests.Session())