def convert_cidr_to_subnet(cidr: int) -> str:
    if (cidr > 32) or (cidr < 0):
        return "Not a valid CIDR"
    _subnet = ""
    for i in range(0, 32):
        if i < cidr:
            _subnet = _subnet + "1"
            continue
        _subnet = _subnet + "0"

    # For the 4 octets (so every 8 char) we convert it to int (cause it actually in binary like 1111111.1111111.etc..
    # And we convert to str to join it and can use it in the function
    return ".".join([str(int(_subnet[i:i + 8], 2)) for i in range(0, len(_subnet), 8)])


def get_cidr(subnet: list) -> int:
    """
    This function allow to convert subnet to CIDR
        Example :
        255.255.255.0 will result to 24
    """
    # For each octet in subnet mask we convert it to binary and count oh many 1 there is
    CIDR = [bin(i).count("1") for i in subnet]
    return sum(CIDR)


def get_ip_information(ip: str, subnet: str) -> str:
    def print_information():
        print("Entered ip : {}".format(ip))
        print("Entered subnet mask : {}".format(subnet))
        print("CIDR of the subnet mask : {}".format(get_cidr(subnet_int)))
        print("Network id : {}".format(".".join(network_id)))
        print("Broadcast : {}".format(".".join(broadcast)))
        print("Number of host : {}".format(2 ** (32 - get_cidr(subnet_int)) - 2))
        print("Max number of subnet : {}".format(2 ** (32 - get_cidr(subnet_int))))
        print("Max number of subnet with available host : {}".format(2 ** (30 - get_cidr(subnet_int))))

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

    isRunning = True
    while (isRunning):
        input_ip = input("Enter ip address (enter q to quit) : ")
        if input_ip == "q":
            isRunning = False
            break
        input_subnet = input("Enter subnet mask or CIDR : ")
        if input_subnet.isdigit():
            subnet = convert_cidr_to_subnet(int(input_subnet))
        else:
            subnet = input_subnet
        print("Subnet mask : {}".format(subnet))
        result: str = get_ip_information(input_ip, subnet)
        if result != "":
            print("An error occurred : {}".format(result))
        print("\n")
