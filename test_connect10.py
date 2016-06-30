import socket
import subprocess, sys, re, time

def how_connect(ip):
    ClientSocket = socket.socket()
    try:
        ClientSocket.connect((ip, 22))
        port = 22
    except socket.error:
        ClientSocket.connect((ip, 23))
        port = 23
    finally:
    #command = "sshpass -ppassword ssh -t -t username@remote_host -p {0}".format(port).split()
    #subprocess.call(command)
    #ClientSocket.close()
        if port == 22:
            print(ip, ' connects via SSH')
            ssh_log = open('ssh_log.txt', 'a')
            ssh_log.write(ip + "\n")
            ssh_log.close()
        elif port == 23:
            print(ip, ' connects via Telnet')
            telnet_log = open('telnet_log.txt', 'a')
            telnet_log.write(ip + "\n")
            telnet_log.close()
        else:
            print('Cannot Connect via either SSH or TELNET!')

#Prompts for the user to enter the name and extension of the file with the devices you want to configure.
ip_file = input('Please enter the name the devices file: ' )
#open the selected file for reading
selected_ip_file = open(ip_file, 'r')
#start at the beginning of the file
selected_ip_file.seek(0)
#read each line in the file and assign it to ip_list
ip_list = selected_ip_file.read().splitlines()


for ip in ip_list:
    how_connect(ip)
