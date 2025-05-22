from netmiko import Netmiko

devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",
        "username": "student",
        "password": "Meilab123",
        "port": "22",
    }
]

description = 'Description set with Netmiko'
description_config = [
    "interface GigabitEthernet3",
    f"description {description}"
]

# New Loopback interface configuration commands
loopback_config = [
    "interface Loopback0",
    "ip address 10.10.10.1 255.255.255.0",
    "description Loopback interface configured by Netmiko"
]

for device in devices:
    net_connect = Netmiko(**device)

    # Configure Loopback interface
    loopback_output = net_connect.send_config_set(loopback_config)
    print(f"Loopback configuration output on {device['ip']}:\n{loopback_output}")

    # Configure GigabitEthernet3 description
    description_output = net_connect.send_config_set(description_config)
    print(f"Description configuration output on {device['ip']}:\n{description_output}")

    net_connect.disconnect()

