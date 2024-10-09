import subprocess
from pydbus import SystemBus
from time import sleep

def scan_bluetooth_devices():
    print("Scanning for Bluetooth devices...")
    result = subprocess.run(["bluetoothctl", "scan", "on"],
                            capture_output=True, text=True)
    sleep(5)
    subprocess.run(["bluetoothctl", "scan", "off"])
    print(result.stdout)

def pair_device(device_mac):
    print(f"Attempting to pair with {device_mac}...")
    subprocess.run(["bluetoothctl", "pair", device_mac],
                   capture_output=True, text=True)

def trust_device(device_mac):
    print(f"Trusting the device {device_mac}...")
    subprocess.run(["bluetoothctl", "trust", device_mac],
                   capture_output=True, text=True)

def connect_device(device_mac):
    print(f"Connecting to {device_mac}...")
    subprocess.run(["bluetoothctl", "connect", device_mac],
                   capture_output=True, text=True)

def set_audio_output(device_mac):
    bus = SystemBus()
    bluez = bus.get("org.bluez", "/org/bluez/hci0/dev_" +
                    device_mac.replace(":", "_"))
    bluez.Connect()
    print(f"Connected to {device_mac} for audio output.")

if __name__ == "__main__":
    device_mac = "XX:XX:XX:XX:XX:XX"
    scan_bluetooth_devices()
    pair_device(device_mac)
    trust_device(device_mac)
    connect_device(device_mac)
    set_audio_output(device_mac)