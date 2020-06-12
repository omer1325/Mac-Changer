#!usr/bin/enc python

import subprocess
import argparse
import random
import os
import re


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_argument("-m", "--mac", dest="new_mac", help="New MAC address")
    parser.add_argument("-r", "--random_mac", dest="random_new_mac", help="New MAC address")
    options = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac and not options.random_new_mac:
        parser.error("[-] Please specify a new mac mac, use --help for more info.")
    return  options


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + "to" + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def random_mac(interface):
    list1 = []
    list2 = []
    random_mac_address = ""
    for i in range(0, 6):
        letter_list = ["a", "b", "c", "d", "e", "f"]
        number_random = random.randint(0, 9)
        letter_random = random.choice(letter_list)
        list1.append(number_random)
        list2.append(letter_random)
    for k in range(0, 6):
        random_mac_address += str(list1[k]) + str(list2[k]) + ":"

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", random_mac_address])
    subprocess.call(["ifconfig", interface, "up"])
    subprocess.check_output(["ifconfig", interface, "hw", "ether", random_mac_address])
    print("[+] Changing MAC address for  " + interface + " to " + "{}".format(random_mac_address[:len(random_mac_address) - 1]))



os.system("clear")
options = get_arguments()
if options.interface and options.new_mac:
    change_mac(options.interface, options.new_mac)
elif options.interface and options.random_new_mac:
    try:
        random_mac(options.interface)
    except:
        subprocess.call(["clear"])
        subprocess.call(["python", "mac_changer.py", "-i", options.interface, "-r", "{}".format(options.interface)])
