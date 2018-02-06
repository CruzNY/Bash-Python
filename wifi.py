#!/usr/bin/python3
import os
import time
import subprocess

print('''
=============================================================================
        _       __ _  ____ _    __  ___                   
       | |     / /(_)/ __/(_)  /  |/  /___   ____   __  __
       | | /| / // // /_ / /  / /|_/ // _ \ / __ \ / / / /
       | |/ |/ // // __// /  / /  / //  __// / / // /_/ / 
       |__/|__//_//_/  /_/  /_/  /_/ \___//_/ /_/ \__,_/  
                                                    
=============================================================================

Created by Alexis Cruz
2/1/2018
A Wifi Menu for enabling wifi by using netctl interfaces 
''')

#Test for successful ping
#tests ping at google, since its like never down?
def ping_check():
    hostname = 'google.com'
    ping_response = os.system('ping -c 3 '+hostname) #sending defualt 3 packets
    #checking the response
    if ping_response == 0:
        ping_status = "Sucessful Ping, Connection has been established! "
    else:
        ping_status = "Error, Unsucessful Ping. "
    #returing appropriate string output.
    return ping_status


def test_ping():
    p = subprocess.Popen(['ping','64.233.160.0','-c','1',"-W","2"])
    p.wait()
    if p.poll():
        ping_status = "Error, Unsucessful Ping. "
    else:
        ping_status = "Sucessful Ping, Connection has been established! "

    return ping_status

    

#Actual Code
#-----------------------------------------------------------
os.chdir('/etc/netctl')
print('To Connect to CityTech WiFi, Enter  (1).')
print('To Connect to Home WiFi, Enter (2). ')
wifi = input(':')
#wifi = input('Enter: 1 for CityTech Wifi, or 0 for Home Wifi:  ')
if wifi == '1':
    os.system('sudo netctl start wlp3s0-CityTech-bWiFi')
elif wifi == '2':
    os.system('sudo netctl start wlp3s0-NETGEAR72')
else:
    print('Error:' + wifi + ' is not currently an option.')
    
#ping = test_ping()
#print(ping)
os.chdir('/home/alex')

