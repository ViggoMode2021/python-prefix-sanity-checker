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

    while True:

        greater_than_mask = (input(f"ip prefix-list TEST permit {subnet} ge __ le __"))

        try:
            greater_than_mask = int(greater_than_mask)
            if 0 <= greater_than_mask <= 32:
                break
            elif greater_than_mask > 32:
                print(f"Input {greater_than_mask} is out of valid range.")
        except ValueError:
            print(f"{greater_than_mask} is not a valid integer!")

    while True:

        less_than_mask = int(input(f"ip prefix-list TEST permit {subnet} ge {greater_than_mask} le __"))

        try:
            less_than_mask = int(less_than_mask)
            if 0 <= less_than_mask <= 32:
                break
            elif less_than_mask > 32:
                print(f"Input {less_than_mask} is out of valid range.")
        except ValueError:
            print(f"{less_than_mask} is not a valid integer!")

    full_statement = f"ip prefix-list TEST permit {subnet} ge {greater_than_mask} le {less_than_mask}"

    print(full_statement)

    subnet_lists = []

    while True:
        subnet_inputs = input("Add subnets that you would like to check.")

        if subnet_inputs == "done":
            break

        try:
            ipaddress.ip_network(subnet_inputs)
            subnet_lists.append(subnet_inputs)
        except ValueError:
            print(f"{subnet_inputs} is not a valid subnet with CIDR notation.")

        for network in subnet_lists:
            mask = int(network.split("/", 1)[1])

            if IPNetwork(network) in IPNetwork(subnet) and greater_than_mask <= mask <= less_than_mask:
                print(f"Yes, {network} is in {subnet} and meets the criteria of your prefix list!")
                subnet_lists.remove(subnet_inputs)
            elif IPNetwork(network) in IPNetwork(subnet):
                print(print(f"The {network} network is in {subnet}, but doesn't meet the comparison operator criteria."))
            else:
                print(f"No, {network} does not meet the criteria of your prefix list.")

if __name__ == "__main__":
    prefix_list_checker()
