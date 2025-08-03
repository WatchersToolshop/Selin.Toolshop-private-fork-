from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os

class ChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            print(f"[Prime.Forge] Modified: {os.path.basename(event.src_path)}")
            # Simulate patch response trigger
            # Call into Prime.Forge logic if desired

    def on_created(self, event):
        if not event.is_directory:
            print(f"[Prime.Forge] Created: {os.path.basename(event.src_path)}")
            # Simulate patch response trigger

if __name__ == "__main__":
    folder = input("Enter folder path to watch: ").strip()
    if not os.path.isdir(folder):
        print("[Prime.Forge] Invalid path.")
        exit()

    observer = Observer()
    event_handler = ChangeHandler()
    observer.schedule(event_handler, folder, recursive=False)
    observer.start()
    print(f"[Prime.Forge] Watching: {folder}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
