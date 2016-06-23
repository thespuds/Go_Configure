
import paramiko
import getpass
import subprocess
import time
import re

pw = getpass.getpass()

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.WarningPolicy())
#client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def start():
    global ip_list
    ip_file = raw_input("# Enter IP file name and extension: ")

    try:
        #open and read the selected file (device list)
        selected_ip_file = open(ip_file, 'r')
        selected_ip_file.seek(0)

        ip_list = selected_ip_file.readlines()
        ip_list = map(lambda s: s.strip(), ip_list)

    except IOError:
        print "\n* File %s does not exist! Please check and try again!\n" % ip_file
    finally:
        print " "

    #Checks to make sure IPs are valid
    #for ip in ip_list:
        #a = ip.split('.')

        #if (len(a) == 4) and (1 <= int(a[0]) <= 223) and (int(a[0]) != 127) and (int(a[0]) != 169 or int(a[1]) != 254) and (0 <= int(a[1]) <= 255 and 0 <= int(a[2]) <= 255 and 0 <= int(a[3]) <= 255):
            #check = True
            #break

            #else:
                #print "\n* There was an invalid IP address!  Please check and try again!\n"
                #check = False
                #continue

    for ip in ip_list:
        try:
            client.connect(ip, port=22, username='eshear', password=pw)
            #client.connect(ip, port=22, username=username, password=pw)
            print "Connection succeeded via SSH:%s\n\n" % ip
            ssh_device_log = open('ssh_device.txt', 'w')
            print >> ssh_device_log.write(ip + '\n')
            ssh_device_log.close()
            client.close
            time.sleep(5)

        except Exception as e:
            #client.close
            print 'Connection FAILED: %s' % ip + '\n'
            telnet_device_log = open('telnet_device.txt', 'w')
            print >> telnet_device_log.write(ip + '\n') #need to append to list.
            telnet_device_log.close()
            time.sleep(1)

        finally:
            print "Next"

    print "Task Completed"

start()
