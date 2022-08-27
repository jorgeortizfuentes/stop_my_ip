from requests import get


def get_ip():
    my_ip = get("https://api.ipify.org").text
    return my_ip


def ip_monitor():
    my_ip = get_ip()
    # Read "my_ip.log"
    my_ip_log = open("my_ip.log", "r").read()
    if my_ip_log == my_ip:
        change = False
        print("IP address has not changed.")
    else:
        change = True
        print(f"IP address has changed to {my_ip}")
        # Write ip to "my_ip.log"
        with open("my_ip.log", "w") as f:
            f.write(my_ip)
    return {"change": change, "ip": my_ip}


if __name__ == "__main__":
    ip_monitor()
