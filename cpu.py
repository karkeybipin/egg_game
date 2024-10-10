import psutil
import time

def monitor_cpu_memory(interval=1):
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            memory_usage = memory.percent
            print(f"CPU Usage: {cpu_usage}% | Memory Usage: {memory_usage}%")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    monitor_cpu_memory()
