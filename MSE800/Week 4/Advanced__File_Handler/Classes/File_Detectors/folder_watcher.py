from watchdog.observers import Observer
from .folder_watcher_event_handler import FolderEventHandler  

class FolderWatcher:
    
    def __init__(self, folder_path):
        self.folder_path = folder_path;
        self.event_handler = FolderEventHandler()
        self.observer = Observer()
        self.observer.schedule(self.event_handler, path=self.folder_path, recursive=False)
        self._start_observer()
    
    # Mostly private method as its denoted using double underscores as a prefix of the method identifier and single underscore for protected
    # Method becomes _FolderWatcher__startWatch (Name Mangling)
    # Still not truly private — can be accessed if needed using mangled name
    # Meant for internal use without subclass interference
    # Helps avoid accidental overrides or access in subclasses
    def _start_observer(self):
        self.observer.start()
        print(f"\nStarted watching: {self.folder_path}")
        
    def stop(self):
        print("\nStopping observer...")
        self.observer.stop()
        self.observer.join()
        print("\nObserver stopped.")
            