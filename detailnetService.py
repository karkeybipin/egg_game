import psutil

def get_network_stats():
    net_io = psutil.net_io_counters()
    print(f"Bytes Sent: {net_io.bytes_sent / (1024**2):.2f} MB")
        #   (1024**2):.2f} MB")
    print(f"Bytes Received: {net_io.bytes_recv / (1024**2):.2f} MB")
    connections = psutil.net_connections(kind='inet')
    print("\nActive Network Connections:")
    for conn in connections:
        laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
        raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
        print(f"{conn.status} | Local: {laddr} | Remote: {raddr}")
    
if __name__ == "__main__":
    get_network_stats()
