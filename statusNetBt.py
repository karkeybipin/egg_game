import socket
import subprocess

def check_internet_connectivity(host="8.8.8.8", port=53, timeout=3):
    """
    Check internet connectivity by trying to connect to Google's public DNS.
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        return False
    # try:
    #     socket.setdefaulttimeout(timeout)
    #     socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
    #     return True
    # except socket.error as ex:
    #     return False

def check_bluetooth_status():
    """
    Check Bluetooth service status and paired devices.
    """
    try:
        result = subprocess.run(["systemctl", "is-active", "bluetooth"], capture_output=True, text=True)
        bt_service_status = result.stdout.strip()

        result = subprocess.run(["bluetoothctl", "paired-devices"], capture_output=True, text=True)
        paired_devices = result.stdout.strip()

        if bt_service_status == "active":
            print("Bluetooth service is active.")
            print("Paired devices:\n", paired_devices if paired_devices else "No paired devices found.")
        else:
            print("Bluetooth service is not active.")
    except Exception as e:
        print(f"Error checking Bluetooth status: {e}")
    #     if bt_service_status == "active":
    #         print("Bluetooth service is active.")
    #         print("Paired devices:\n", paired_devices if paired_devices else "No paired devices found.")
    #     else:
    #         print("Bluetooth service is not active.")
    # except Exception as e:
    #     print(f"Error checking Bluetooth status: {e}")

if __name__ == "__main__":
    if check_internet_connectivity():
        print("Internet is connected.")
    else:
        print("No internet connection.")

    check_bluetooth_status()
