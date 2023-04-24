# This class keeps track of files that have been generated in this folder. It will notify the tech
#   when the folder is full (or close to full).
# This class will also possibly be able to automatically zip the generated files that is overcrowding
#   the folder


import os
import shutil
import time
import win32serviceutil
import win32service
import win32event


class ArchiveService(win32serviceutil.ServiceFramework):
    _svc_name_ = "ArchiveService"
    _svc_display_name_ = "Archive Service"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.stop_event)

    def SvcDoRun(self):
        while True:
            files = os.listdir("B:\ForWatchdogProject")
            for file in files:
                if file.endswith("9999"):
                    source_path = os.path.abspath(file)
                    dest_path = os.path.abspath("archive/" + file)  # archiving starts here
                    shutil.move(source_path, dest_path)
                    print(f"{file} archived to {dest_path}")
            time.sleep(10)


if __name__ == "__main__":
    win32serviceutil.HandleCommandLine(ArchiveService)