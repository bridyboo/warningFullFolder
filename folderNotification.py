import win32serviceutil
import win32service
import win32event
import servicemanager
import socket
import os
import sys
import time
import shutil
import InstallerFolder

# Global Variable
#######################################################################################################################
POSTFIX = r'5.txt'
base = r'C:\\Program Files (x86)\\archiveService\\filepath.txt'  # so this shit works, because it's a static path
#######################################################################################################################

folder = InstallerFolder.InstallFolder()

class MyService(win32serviceutil.ServiceFramework):
    _svc_name_ = 'ArchiveService'
    _svc_display_name_ = 'ArchiveService'

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)
        self.is_running = True

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.is_running = False

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self.main()

    def main(self):
        while self.is_running:
            # search through this file that has a list of all the fsrv folders for example:
            try:
                uncBase = os.path.join(folder.getBase())
                with open(base, "r") as file:  # as a service this opens up the python lib path and creates filepath.txt
                    for path in file:
                        path = path.rstrip('\n')  # important because OS reads the \n breaking the script
                        destination = trimPathName(path)
                        zipFolder(path, destination)
            except FileNotFoundError:
                with open(base, "w"):
                    pass

            # Sleep for 10 seconds
            time.sleep(10)

# This function walks through the path queried and zips all the files in the folder into an archive folder
# This will trigger when there's a file that ends with a specific 'postfix' i.e. testfile999 << ends at 999
def zipFolder(folder, zip_destination):
    for root, dirs, files in os.walk(folder, topdown=False):
        for file in files:
            if file.endswith(POSTFIX):  # modifies end with postfix
                shutil.make_archive(os.path.join(zip_destination), format='zip', base_dir=folder)
                # os.remove(base + file) ? don't know if this will work

# This function trims the dirname & basename to create unique .zip files for each folder in the 'filepath' file
def trimPathName(folder):
    root = os.path.dirname(folder)
    basename = os.path.basename(folder)
    destination = os.path.join(root, 'archives', 'archive_' + basename)
    return destination

if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(MyService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(MyService)
