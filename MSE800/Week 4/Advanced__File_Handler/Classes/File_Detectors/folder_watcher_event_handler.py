from watchdog.events import FileSystemEventHandler
from .file_identifier import FileIdentifier

class FolderEventHandler(FileSystemEventHandler): # FileSystemEventHandler acts as the base class and FolderWatcher will inherit that.
        
    # Overriding base class method on_created (Base class actually has a set of empty methods more like abstract )
    def on_created(self, event):
        if not event.is_directory:
            print(f"\nFile detected and started to process : {event.src_path}")
            file_identifier = FileIdentifier(event.src_path)
            file_identifier.start_process()
      
            