import subprocess

def get_system_temperature():
    try:
        result = subprocess.run(['sensors'], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"Error fetching system temperature: {e}")

if __name__ == "__main__":
    get_system_temperature()
