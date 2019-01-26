#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile, os

def backuptoZip(folder):
    #backup the entire contents of folder into a zip file
    folder = os.path.abspath(folder)

    number = 1

    while True:
        zipFilename = os.path.basename(folder)+'_'+str(number)+'.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    print("Creating %s..." %(zipFilename))

    backupZip = zipfile.ZipFile(zipFilename, 'w')

    for foldername, subfolder,files in os.walk(folder):
        print('Adding files in %s.' %(foldername))
        #Add the current folder to zip file.
        backupZip.write(foldername)

        # Add all files in this folder to the Zip file.

        for filename in files:
            newBase = os.path.basename(folder)+'_'

            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue #dont backup the zip files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done')

backuptoZip("E:\\python\\projects")
