from netmiko import ConnectHandler

r1 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.101",
    "username": "student",
    "password": "Meilab123",
    "port": "22"
}
r2 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.102",
    "username": "student",
    "password": "Meilab123",
    "port": "22"
}
r3 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.103",
    "username": "student",
    "password": "Meilab123",
    "port": "22"
}

commands = [
    "show version",
    "show ip interface brief",
    "show interface description",
    "show inventory",
    "show logging"
]

for device in (r1, r2, r3):
    print("="*100)
    print(f"Connecting to device {device['ip']}")
    net_connect = ConnectHandler(**device)

    for command in commands:
        print("-" * 80)
        print(f"Output for '{command}' on device {device['ip']}:")
        output = net_connect.send_command(command)

        # For show running-config or very long output, you might want to limit lines or length,
        # but these commands are moderate size to print entirely.
        print(output)
    net_connect.disconnect()
    print("="*100 + "\n")



