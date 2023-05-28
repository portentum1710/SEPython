from ipaddress import ip_network


def has_access(a, b):
    hosts_list = list(ip_network(b).hosts())
    ip_ad = list(ip_network(a).hosts())
    access = False
    for host in hosts_list:
        print(host)
    return ip_ad[0]




access = has_access("91.142.84.30", "91.142.84.0/27")
print(access)
