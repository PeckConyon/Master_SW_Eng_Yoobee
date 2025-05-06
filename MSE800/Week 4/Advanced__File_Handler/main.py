import time
import os
from Classes.File_Detectors.folder_watcher import FolderWatcher

def main():
    
    print("Starting folder watcher...")
    
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Path to Advanced__File_Handler
    path_to_watch = os.path.join(base_dir, 'Files')
    folder_watcher = FolderWatcher(path_to_watch)
    
    try:
        print("\nPress Ctrl+C to stop watching...")
        while True:
            time.sleep(1)  # Keeps main thread alive
    except KeyboardInterrupt:
        print("\nStopping folder watcher...")
        folder_watcher.stop()
        print("\nFolder Watcher stopped.")
    
if __name__ == "__main__":
    main()