import serial, json, os, subprocess, time
from datetime import date, timedelta
from ftplib import FTP
rs232com = serial.Serial(port='/dev/serial0',baudrate=9600,parity=serial.PARITY_NONE,\
stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)
print("connected to: " + rs232com.portstr)
logPath = "/home/pi/Documents/DQMLogs"
os.makedirs(logPath, exist_ok=True)
fullLogPath = logPath + '/log-' + str(date.today()) + '.txt'
USBlog = open(fullLogPath, "a")
log = open(fullLogPath, "a")
lastUpdatedDate = date.today()
def connectToUSBStick():
    failed = False
    try:
        USBLogPath = "/media/pi/USB STICK/DQMLogs"
        os.makedirs(USBLogPath, exist_ok=True)
        USBfullLogPath = USBLogPath + '/log-' + str(date.today()) + '.txt'
        USBlog = open(USBfullLogPath, "a")
    except:
        print("Failed to open Log Path on USB STICK.")
        failed = True
    if(failed):
        connectToUSBStick1()
    else:
        print("Connected to USB STICK")
def connectToUSBStick1():
    failed = False
    try:
        USBLogPath = "/media/pi/USB STICK1/DQMLogs"
        os.makedirs(USBLogPath, exist_ok=True)
        USBfullLogPath = USBLogPath + '/log-' + str(date.today()) + '.txt'
        USBlog = open(USBfullLogPath, "a")
    except:
        print("Failed to open Log Path on USB STICK.")
        failed = True
    if(failed):
        connectToUSBStick()
    else:
        print("Connected to USB STICK1")
def updateLogPath():
    try:
        USBlog.close()
        connectToUSBStick()
    except:
        print("Failed to update USB Log Path")
    log.close()
    fullLogPath = logPath + '/log-' + str(date.today()) + '.txt'
    log.open(fullLogPath, "a")
def uploadViaFTP():
    ftp = FTP('192.168.1.28')
    ftp.login(user="admin", passwd='admin')
    try:
        ftp.cwd('DQM_Logs')
    except:
        #ftp.mkd('DQM_Logs')
        ftp.cwd('DQM_Logs')
        
    with open(fullLogPath, 'rb') as file:
        ftp.storbinary('STOR '+'log-'+str(date.today())+'.txt', file)
        file.close()
    ftp.quit()
uploadViaFTP()
connectToUSBStick()
while rs232com.isOpen():
    inString = rs232com.readline().decode()
    log.write(inString)
    try:
        USBlog.write(inString)
    except:
        print("Tried to write to USB Stick and failed. Trying the other USB Stick...")
        connectToUSBStick()
    list_of_files = os.listdir(logPath)
    full_path = ["/home/pi/Documents/DQMLogs/{0}".format(x) for x in list_of_files]
    print(inString)
    if len(list_of_files) > 90:
        oldest_file = min(full_path, key=os.path.getctime)
        os.remove(oldest_file)
        print('Removed: ' + oldest_file)
    if date.today() != lastUpdatedDate:
        uploadViaFTP()
        lastUpdatedDate = date.today
        updateLogPath()
        print("Yesterdays log uploaded to NAS.")