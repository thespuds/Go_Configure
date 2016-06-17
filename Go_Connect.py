#Go_Connect

import paramiko
import threading
import os.path
import subprocess
import time
import sys
import re


def ip_is_valid():
    check = False
    global ip_list

while True:
    ip_file = raw_input("# Enter IP file name and extension: ")

    try:
        #open and read the selected file (device list)
        selected_ip_file = open(ip_file, 'r')

        selected_ip_file.seek(0)

        ip_list = selected_ip_file.readlines()

    except IOError:
        print "\n* File %s does not exist! Please check and try again!\n" % ip_file

    #Checks to make sure IPs are valid
    for ip in ip_list:
        a = ip.split('.')

        if (len(a) == 4) and (1<= int(a[0]) <= 223) and (int(a[0]) != 127) and (int(a[0]) != 169 or int(a[1]) != 254) and check = True
        break

    else:
        print "\n* There was an invalid IP address!  Please check and try again!\n"
        check = False
        continue

    #Evaluate the 'check' flag
     if check == True:
         break

    #check reachability
    print "\n* Checking IP reachability. Please standby...\n"

    check2 = False

    while True:
        for ip int ip_list:
            ping_reply = subprocess.call(['ping', '-c', '2', '-w', '2', '-q', '-n', ip])

            if ping_reply == 0:
                check2 = True
                continue

            elif ping_reply == 2:
                print "\n* No response from device %s." % ip
                ip_log = open('ip_log.txt', 'w')
                print >> ip_log.write('Unable to reach the following IPs!\n %s' % ip)
                ip_log.close()
                break

            else:
                print "\n* Ping to the following device has FAILED:", ip


#Connect to the device using username and password



#Open SSH or Telnet and log the result.
def open_connection(ip):
    try:
        #Define SSH parameters
        selected_user_file = open(user_file, 'r')

        #Starting from the beginning of the file
        selected_user_file.seek(0)

        #Reading the username from the file
        username = selected_user_file.readlines()[0].split(',')[0]

        #Starting from the beginning of the file
        selected_user_file.seek(0)

        #Reading the password from the file
        password = selected_user_file.readlines()[0].split(',')[1].rstrip("\n")

        #Reading enable password from file
        enablePass = selected_user_file.readlines()[0].split(',')[2].rstrip("\n")

        #Logging into device
        session = paramiko.SSHClient()

        #For testing purposes, this allows auto-accepting unknown host keys
        #Do not use in production! The default would be RejectPolicy
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        #Connect to the device using username and password
        def test_login(user_file):
            for each_login in user_file:
                try:
                    session.connect(ip, username = username, password = password)
                    if return True:
                        break

                except (paramiko.PasswordRequiredException, paramiko.AuthenticationException) as error:
                    print '\n* Login failed, trying next login...\n'
                    print repr(error)
                    sleep(interval)
                finally continue
            for each_login in userfile:
            login_device_log = open('login_device.txt', 'w')
            print >> login_device_log.write('%s,%s,%s SSH' % ip,username,password)
            login_device_log.close()

    ssh_device_log = open('ssh_device.txt', 'w')
    print >> ssh_device_log.write('%s,%s,%s' % ip,username,password)
    ssh_device_log.close()
