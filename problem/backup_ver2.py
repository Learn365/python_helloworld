import os
import time

# 1. The files and directories to be backed up are
# specified in a list.
# Example on Windows:
# ['d:\\Working\\Projects\\python\helloworld\\basic']
source = ['C:\\Users\\baker\\Documents\\Development\\python\\helloworld\\basic']
# Example on Mac OS X and Linux:
# source = ['/Users/swa/notes']
# Notice we had to use double quotes inside the string
# for names with spaces in it.

# 2. The backup must be stored in a
# main backup directory
# Example on Windows:
# 'd:\\Working\\Projects\\python\helloworld\\backup'
target_dir = 'C:\\Users\\baker\\Documents\\Development\\python\\helloworld\\backup'
# Example on Mac OS X and Linux:
# target="/Users/swa/backup"
# Remember to change this to which folder you will be using

# 3. The files are backed up into a zip file.
# 4. The current date is the name of the subdirectory
# in the main directory
today = target_dir + os.sep + time.strftime("%Y%m%d")
# the current time is the name of the zip archive
now = time.strftime("%H%M%S")

target = today + os.sep + now + '.zip'

# Create subdirectory if it isn't already there
if not os.path.exists(today):
    os.makedirs(today)  # make directory

# 5. We use the zip command to put the files in a zip archive
zip_command = "zip -r {0} {1}".format(target, ' '.join(source))

# Run the backup
print("Zip command is")
print(zip_command)
print("Running:")
if os.system(zip_command) == 0:
    print("Successful backup to", target)
else:
    print("Backup FAILED")
