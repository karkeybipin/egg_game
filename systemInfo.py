import platform
import psutil
import cpuinfo
from datetime import datetime

def get_system_info():
    system_info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "Architecture": platform.architecture()[0]
    }
    cpu_info = cpuinfo.get_cpu_info()
    system_info["CPU"] = cpu_info["brand_raw"]
    system_info["Cores"] = psutil.cpu_count(logical=False)
    system_info["Logical Cores"] = psutil.cpu_count(logical=True)
    system_info["Max Frequency"] = f"{psutil.cpu_freq().max:.2f} MHz"
    virtual_mem = psutil.virtual_memory()
    system_info["Total RAM"] = f"{virtual_mem.total / (1024**3):.2f} GB"
    system_info["Available RAM"] = f"{virtual_mem.available / (1024**3):.2f} GB"
    disk_usage = psutil.disk_usage('/')
    system_info["Total Disk"] = f"{disk_usage.total / (1024**3):.2f} GB"
    system_info["Used Disk"] = f"{disk_usage.used / (1024**3):.2f} GB"
    system_info["Free Disk"] = f"{disk_usage.free / (1024**3):.2f} GB"
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    system_info["Boot Time"] = boot_time.strftime("%Y-%m-%d %H:%M:%S")
    addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in addrs.items():
        for address in interface_addresses:
            if str(address.family) == 'AddressFamily.AF_INET':
                system_info[f"Network Interface: {interface_name}"] = f"IP Address: {address.address}"
    return system_info
def print_system_info():
    system_info = get_system_info()
    print("\nSystem Specifications:\n")
    for key, value in system_info.items():
        print(f"{key}: {value}")
if __name__ == "__main__":
    print_system_info()