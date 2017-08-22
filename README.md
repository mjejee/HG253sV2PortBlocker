# HG253sV2PortBlocker
Periodically checks if the HG253s V2 router has port 443 open and closes it, avoiding leaking the wireless password to the Internet. Based on the bug published by Vicen Dominguez: https://github.com/vicendominguez/http-enum-vodafone-hua253s

It includes 3 files:
* securerouterhttps - LSB script for running the python code as a service
* securerouterhttps.py - Periodically checks if the router has port 443 open. If that's the case it runs routernohttps using expect
* routernohttps - expect script that connects to the router and adds an iptables rule that blocks incoming connections to port 443.


More info at my blog: https://onlyifsecure.blogspot.com/2017/08/huawei-hg253s-bug.html
