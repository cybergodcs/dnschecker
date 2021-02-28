import socket
import sys

print('''          
            _                                 _ 
  ___ _   _| |__   ___ _ __    __ _  ___   __| |
 / __| | | | '_ \ / _ \ '__|  / _` |/ _ \ / _` |
| (__| |_| | |_) |  __/ |    | (_| | (_) | (_| |
 \___|\__, |_.__/ \___|_|     \__, |\___/ \__,_|
      |___/                   |___/             
            
''')

try:
    host = sys.argv[1]
    print"Domain name : ",host
    print"Address ip :",socket.gethostbyname (host)
    dns_server = gethostbyaddr (host)
    for i in dns_server:
        print"Dns server > ",i
except:
    print"Done."




