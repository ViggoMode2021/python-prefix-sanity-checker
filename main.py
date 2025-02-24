#https://stackoverflow.com/questions/35115138/how-do-i-check-if-a-network-is-contained-in-another-network-in-python

from netaddr import IPNetwork, IPAddress
import re

def prefix_list_checker():

    subnet = input("ip prefix-list TEST permit ______________ ge __ le __")

    greater_than_mask = int(input(f"ip prefix-list TEST permit {subnet} ge __ le __"))

    less_than_mask = int(input(f"ip prefix-list TEST permit {subnet} ge {greater_than_mask} le __"))

    full_statement = f"ip prefix-list TEST permit {subnet} ge {greater_than_mask} le {less_than_mask}"

    print(full_statement)

    subnet_lists = ["192.168.123.0/24", "192.168.0.0/30", "192.168.0.0/16", "192.168.0.0/8"]

    for network in subnet_lists:
        mask = int(network.split("/", 1)[1])

        if IPNetwork(network) in IPNetwork(subnet) and greater_than_mask <= mask <= less_than_mask:
            print(f"Yes {network} meets the criteria of your prefix list!")
        elif IPNetwork(network) in IPNetwork(subnet):
            print(print(f"The {network} network is in {subnet}, but doesn't meet the comparison operator criteria."))
        else:
            print(f"No {network} does not meet the criteria of your prefix list.")

prefix_list_checker()
