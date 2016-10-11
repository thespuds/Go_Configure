import socket
import subprocess
import sys

########################## Application Step 1. #############################
#Looks to see if there is an open socket for SSH or Telnet.

def how_connect(ip):
    ClientSocket = socket.socket()
    port = 0

    try:
        ClientSocket.connect((ip, 22))
        port = 22

    except socket.error:
        pass
        try:
            ClientSocket.connect((ip, 23))
            port = 23
        except socket.error:
            pass

    finally:
        if port == 22:
            #Generate a Log file of devices that can connect via
            print(ip, 'connects via SSH')
            ssh_log = open('ssh_log.txt', 'a')
            ssh_log.write(ip + "\n")
            ssh_log.close()
        elif port == 23:
            #Generate a Log file of devices that can connect via Telnet.
            print(ip, 'connects via Telnet')
            telnet_log = open('telnet_log.txt', 'a')
            telnet_log.write(ip + "\n")
            telnet_log.close()
        else:
            #generates a log file containing unreachable devices.
            print(ip, 'cannot connect via either SSH or TELNET!')
            error_log = open('error_log.txt', 'a')
            error_log.write(ip + "\n")
            error_log.close()
        ClientSocket.close()


################################ MAIN #########################################


#Prompts for the user to enter the name and extension of the file with the devices you want to configure.
ip_file = input('Please enter the name the devices file: ' )
#open the selected file for reading
selected_ip_file = open(ip_file, 'r')
#start at the beginning of the file
selected_ip_file.seek(0)
#read each line in the file and assign it to ip_list
ip_list = selected_ip_file.read().splitlines()

#Check each ip in a list.
for ip in ip_list:
    how_connect(ip)

#Clean up and exit
selected_ip_file.close()
sys.exit()
