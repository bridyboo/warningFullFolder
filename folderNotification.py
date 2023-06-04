# Creates a windows service that does the following:
# Reads through a file containing a list of paths that needs to be 'monitored'
# Folders will be archived and sent into a \basename\archive\ folder


import os
import shutil
import win32serviceutil
import win32service
import win32event

base = os.path.join('B:', 'ForWatchdogProject', 'files')
dest = os.path.join('B:', 'ForWatchdogProject', 'archives', 'archive')
root = os.path.join('B:', 'ForWatchdogProject', 'archives.zip')


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
        # search through this file that has a list of all the fsrv folders for example:
        with open(base, "r") as file:
            for path in file:
                path = path.rstrip('\n')  # important because OS reads the \n breaking the script
                destination = trimPathName(path)
                zipFolder(path, destination)


# This function walks through the path queried and zips all the files in the folder into an archive folder
def zipFolder(folder, zip_destination):
    for root, dirs, files in os.walk(folder, topdown=False):
        for file in files:
            if file.endswith("5.txt"):
                shutil.make_archive(zip_destination, format='zip', base_dir=folder)
                # os.remove(base + file) ? don't know if thi will work


# This function trims the dirname & basename to create unique .zip files for each folder in the 'filepath' file
def trimPathName(folder):
    root = os.path.dirname(folder)
    basename = os.path.basename(folder)
    destination = os.path.join(root, 'archives', 'archive_' + basename)
    return destination


if __name__ == "__main__":
    win32serviceutil.HandleCommandLine(ArchiveService)
