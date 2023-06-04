"# warningFullFolder" 
# This class keeps track of files that have been generated in this folder. It will notify the tech
#   when the folder is full (or close to full).
# This class will also possibly be able to automatically zip the generated files that is overcrowding the folder
# The program checks a file that has a list of all the folders that it "watches" over
# ok so it turns out python services, needs to have python rooted on to SYSTEMPATH (it's a DLL issue)


Both running a Python script as a Windows service and scheduling a Python script to run at specific times have their own advantages and use cases. Let's explore each option:

Windows Service of a Python Script:
Running a Python script as a Windows service allows the script to run continuously in the background, even when no user is logged in. This approach is suitable for tasks that require constant monitoring or need to respond to events in real-time. Some benefits of using a Windows service include:

Automatic startup: The service can start automatically when the system boots up.
Independence from user login: The service can run without any user logged in, ensuring continuous operation.
Event-driven or real-time tasks: Services can listen for events or perform actions as soon as they occur.
System-level access: Services have higher privileges and can access system resources.
Reliability: Services can automatically restart if they crash or encounter errors.
Scheduled Python Script:
Scheduling a Python script involves setting up a task scheduler to execute the script at specific times or intervals. This approach is suitable for tasks that need to be performed periodically or at specific times. Some advantages of scheduling Python scripts include:

Flexibility: You can schedule scripts to run at any desired time or frequency, such as daily, weekly, or specific intervals.
Easy configuration: Task schedulers in different operating systems provide user-friendly interfaces to set up scheduled tasks.
Resource management: Scripts only consume resources during their scheduled execution, allowing for efficient resource allocation.
Simplicity: Scheduling scripts is often easier to set up and manage compared to developing and deploying a Windows service.
Considerations:

Time requirements: If your script needs to run continuously and perform real-time actions, a Windows service is more appropriate. If it needs to execute at specific times or intervals, scheduling is a better fit.
Access to system resources: Windows services have greater access to system-level resources, making them suitable for tasks that require deeper integration.
Development complexity: Creating a Windows service typically requires more development effort than setting up a scheduled task.
System dependencies: If your script relies on specific system conditions or services, running it as a service may be more reliable.
In summary, choosing between running a Python script as a Windows service or scheduling it depends on the nature of the task, the required execution behavior, and the system resources it needs to access.