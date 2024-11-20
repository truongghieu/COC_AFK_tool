import os
import tempfile
import shutil
import psutil
import subprocess


def clean_temp_files():
    temp_dir = tempfile.gettempdir()
    for filename in os.listdir(temp_dir):
        file_path = os.path.join(temp_dir, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Removed file: {file_path}")
            elif os.path.isdir(file_path):
                os.rmdir(file_path)  # Remove empty directories
                print(f"Removed directory: {file_path}")
        except Exception as e:
            print(f"Error removing {file_path}: {e}")

def close_unwanted_processes(process_names):
    for process in psutil.process_iter(['pid', 'name']):
        try:
            if process.info['name'] in process_names:
                process.terminate()  # Close the process
                print(f"Closed: {process.info['name']}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
def disable_firewall():
    try:
        # Execute PowerShell command to disable Windows Firewall
        result = subprocess.run(['powershell', '-Command', 'Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False'], capture_output=True, text=True)

        # Check the output and return code
        if result.returncode == 0:
            print("Windows Firewall has been disabled successfully.")
        else:
            print("Failed to disable Windows Firewall.")
            print("Error message:", result.stderr)

    except Exception as e:
        print("An error occurred:", str(e))


def cleann():
    # List of processes to close
    unwanted_processes = [
        "ZaloCall.exe",
        "UniKeyNT.exe",
        "Zalo.exe",
        "msedge.exe",
        "powershell.exe",
        "language_server_windows_x64.exe",
        "Code.exe",
        "pet.exe",
        "winpty-agent.exe"
    ]

    # send_text("Closing unwanted processes...")
    # close_unwanted_processes(unwanted_processes)
    clean_temp_files()
    close_unwanted_processes(unwanted_processes)
   

if __name__ == "__main__":
    cleann()
