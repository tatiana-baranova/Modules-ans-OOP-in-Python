from watchdog.observers import Observer
import os
import time
from watchdog.events import FileSystemEventHandler
import shutil

folder_track = r'E:\Users\molmo@Nitro\Desktop\Download'
folder_dest = r'E:\Users\molmo@Nitro\Desktop'
class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_track):
            src_path = os.path.join(folder_track, filename)
            dest_path = os.path.join(folder_dest, filename)
            if os.path.isfile(src_path):
                if not os.path.exists(dest_path):
                    shutil.move(src_path, dest_path)
                else:
                    print(f"{filename} вже існує в папці призначення!")

handle = Handler()
observer = Observer()
observer.schedule(handle, folder_track, recursive=True)
observer.start()

try:
    while(True):
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()