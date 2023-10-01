def get_ip_information(ip: str, subnet: str) -> str:
    def print_information():
        print("Entered ip : {}".format(ip))
        print("Entered subnet mask : {}".format(subnet))
        print("Network id : {}".format(".".join(network_id)))
        print("Broadcast : {}".format(".".join(broadcast)))
        print("Number of host : {}".format(sum(inverted_subnet) - 1))

    # Set all ip in int list from input like "192.168.1.1" to [192, 168, 1, 1]
    """
    The syntaxe [] is like a for loop that in reality look like this:
    ip_int = []
    for i in ip.split("."):
        ip_int.append(int(i))
    is equal to ip_int= [int(i) for i in ip.split(".")]
    """
    ip_int = [int(i) for i in ip.split(".")]

    # This line is just to check if the ip is valid
    if not len(ip_int) == 4:
        return "Not a valid ip address"
    # We check all value in the list to check if they are between 0 and 255
    if not all([0 <= i <= 255 for i in ip_int]):
        return "Ip address must be between 0 and 255"

    # Same as above but with subnet mask
    subnet_int = [int(i) for i in subnet.split(".")]
    if not len(subnet_int) == 4:
        return "Not a valid subnet mask"
    if not all([0 <= i <= 255 for i in subnet_int]):
        return "Subnet mask must be between 0 and 255"
    # This doesn't check if the subnet mask like 255.0.255.255 (that is not valid)

    # Get the inverted subnet mask (allow to get broadcast address and number of host)
    inverted_subnet = [255 - subnet_int[i] for i in range(4)]

    # Get the network id (or operation between the ip and the subnet mask) and convert to str to join it later
    network_id = [str(ip_int[i] & subnet_int[i]) for i in range(4)]
    # Get the broadcast address (or operation between the ip and the inverted subnet mask)
    broadcast = [str(ip_int[i] | inverted_subnet[i]) for i in range(4)]

    print_information()

    return ""


if __name__ == '__main__':
    result: str = get_ip_information(input("Enter ip address : "),
                                     input("Enter subnet mask : ")
                                     )
    if result is not "":
        print("An error occurred : {}".format(result))
