import os
import time

def generate_log_filename():
    desktop = os.path.join(os.path.expanduser("~"), "Downloads")
    timestamp = time.strftime("%Y%m%d-%H%M%S")

    return  os.path.join(desktop, f"folder_report_{timestamp}.txt")


def scan_folder(folder_path):
    log_file = generate_log_filename()

    with open(log_file, 'w', encoding='utf-8') as f:

        for root, dirs, files in os.walk(folder_path):

            f.write(f"\n Directory: {root}\n")

            for file in files:
                file_path = os.path.join(root,file)

                try:
                    size = os.path.getsize(file_path)
                    modified = time.ctime(os.path.getmtime(file_path))
                    f.write(f" · {file} | Size: {size} bytes | Last Modified: {modified}\n")

                except Exception as e:

                    f.write(f" · {file} | Error: {str(e)}\n")

    print(f"scan complete! Log saved to: {log_file}")
    return log_file