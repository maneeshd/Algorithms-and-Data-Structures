def validate_ip(ip: str) -> str:
    ipv4 = ip.split(".")
    if len(ipv4) == 4:
        # May be IPv4
        for val in ipv4:
            try:
                if val[0] == "0":
                    return "Neither"
                val = int(val)
                if val < 0 or val > 255:
                    return "Neither"
            except (ValueError, IndexError):
                return "Neither"
        return "IPv4"

    ipv6 = ip.split(":")
    if len(ipv6) == 8:
        # Maybe IPv6
        for val in ipv6:
            try:
                if len(val) > 4:
                    return "Neither"
                if int(val, 16) < 0:
                    return "Neither"
            except (IndexError, ValueError):
                return "Neither"
        return "IPv6"

    return "Neither"


if __name__ == "__main__":
    print(f"validate_ip('10.10.10.4')      : {validate_ip('10.10.10.4')}")
    print(f"validate_ip('10.1234.901.1')   : {validate_ip('10.1234.901.1')}")
    print(f"validate_ip('')                : {validate_ip('')}")
    print(f"validate_ip('adasdasdasdasd')  : {validate_ip('adasdasdasdasd')}")
    print(f"validate_ip('-1.35.-7.9')      : {validate_ip('-1.35.-7.9')}")
    print(f"validate_ip('255.255.255.255') : {validate_ip('255.255.255.255')}")
    print(f"validate_ip('0.0.0.0')         : {validate_ip('0.0.0.0')}")
    print(f"validate_ip('192.168.1.1')     : {validate_ip('192.168.1.1')}")
