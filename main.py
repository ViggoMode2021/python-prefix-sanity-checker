# https://stackoverflow.com/questions/35115138/how-do-i-check-if-a-network-is-contained-in-another-network-in-python

from netaddr import IPNetwork, IPAddress
import ipaddress
import re

def prefix_list_checker():
    while True:
        subnet = input("ip prefix-list TEST permit ______________ ge __ le __")

        try:
            ipaddress.ip_network(subnet)
            break
        except ValueError:
            print(f"{subnet} is not a valid subnet with CIDR notation.")

    greater_than_mask = int(input(f"ip prefix-list TEST permit {subnet} ge __ le __"))

    less_than_mask = int(input(f"ip prefix-list TEST permit {subnet} ge {greater_than_mask} le __"))

    full_statement = f"ip prefix-list TEST permit {subnet} ge {greater_than_mask} le {less_than_mask}"

    print(full_statement)

    subnet_lists = []

    while True:
        subnet_inputs = input("Add subnets that you would like to check.")

        subnet_lists.append(subnet_inputs)

        cidr_pattern = r'^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/([0-9]|[1-2][0-9]|3[0-2]))$'

        if subnet_inputs == "done":
            subnet_lists.remove("done")
            break
        elif not re.match(subnet_inputs, cidr_pattern):
            print(f"{subnet_inputs} does not match regex for prefix + cidr")

        subnet_lists.append(subnet_inputs)

    for network in subnet_lists:
        mask = int(network.split("/", 1)[1])

        if IPNetwork(network) in IPNetwork(subnet) and greater_than_mask <= mask <= less_than_mask:
            print(f"Yes, {network} is in {subnet} and meets the criteria of your prefix list!")
        elif IPNetwork(network) in IPNetwork(subnet):
            print(print(f"The {network} network is in {subnet}, but doesn't meet the comparison operator criteria."))
        else:
            print(f"No, {network} does not meet the criteria of your prefix list.")

if __name__ == "__main__":
    prefix_list_checker()
