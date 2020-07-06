

import sys
import socket
from datetime import datetime

# Define our target

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip>")
    sys.exit()
#Best banner ever
print("-"*50)
print('/'*50)
print("Scanning target "+target)
print("time started:"+str(datetime.now()))
print('/'*50)
print("-"*50)

try:
    for port in range(1,65000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) # is float
        result = s.connect_ex((target,port))
        #print("Checking port {}".format(port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()
except socket.gaierror:
    print("\nHostname could not be resolved.")
    sys.exit()
except socket.error:
    print("\nCouldn't connect to server.")
    sys.exit()
