from netmiko import Netmiko

def push_config(csv_data):
    device = {
        "host": csv_data[1],
        "username": csv_data[2],
        "password": csv_data[3],
        "device_type": csv_data[4],
    }
    commands = list(csv_data)
    # print(device)
    del commands[0:5]
    # print(commands)
    try:
        net_connect = Netmiko(**device)
        output = net_connect.send_config_set(commands)
        # print(output)
        log_device = {
            "devicename" : csv_data[0],
            "ip" : csv_data[1],
            "status" : "success mamang"
        }
    except:
        log_device = {
            "devicename" : csv_data[0],
            "ip" : csv_data[1],
            "status" : "error coy"
        }
    return log_device