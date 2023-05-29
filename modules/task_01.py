from ipaddress import ip_network


def has_access(ip, host):
    hosts_list = list(ip_network(host).hosts())
    ip_ad = list(ip_network(ip).hosts())
    access = False
    for host in hosts_list:
        if host == ip_ad[0]:
            access = True
    return access

print(has_access("91.142.84.30", "91.142.84.0/27"))
#--------------------------------------------------------
import ipaddress


def has_access(ip, network):
    # Преобразовываем адреса.
    ip = ipaddress.ip_address(ip)
    network = ipaddress.ip_network(network)

    # Выводим данные.
    return True if ip in network.hosts() else False

