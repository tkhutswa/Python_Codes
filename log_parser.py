import pandas as pd

log = {"timezone":"2024-02-07 15:45:44:799 EST","acode":"TGu_GcWUPi-TIdNenwyLrA","thread":"SmtpThread-12142339","level":"INFO ","mimemessage":"Connection|10.20.216.242|185.70.41.104"}

#if you iterate using keys instead of values - we should get the info we looking for.
for i in log.values():
    i.split(",")
    print(i)
#the mimemessage in this case is the key for connection | IP address :)
