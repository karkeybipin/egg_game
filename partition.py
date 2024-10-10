import psutil

def get_disk_partitions_info():
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"Device: {partition.device}")
        print(f"  Mountpoint: {partition.mountpoint}")
        print(f"  File System Type: {partition.fstype}")
        
        usage = psutil.disk_usage(partition.mountpoint)
        print(f"  Total Size: {usage.total / (1024**3):.2f} GB")
        print(f"  Used: {usage.used / (1024**3):.2f} GB")
        print(f"  Free: {usage.free / (1024**3):.2f} GB")
        print(f"  Usage: {usage.percent}%")
        print("-" * 30)

if __name__ == "__main__":
    get_disk_partitions_info()
