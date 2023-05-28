import ipaddress


def has_access(a, b):
    return ipaddress(a)


access = has_access("91.142.84.30", "91.142.84.0/27")
print(access)
