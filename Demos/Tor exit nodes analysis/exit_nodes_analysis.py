import os
import csv
import subprocess

os.system("wget https://torstatus.blutmagie.de/ip_list_exit.php/Tor_ip_list_EXIT.csv")
with open("Tor_ip_list_EXIT.csv", "rb") as exit_list:
    exit_list_reader = csv.reader(exit_list, delimiter=' ', quotechar='|')
    for linea in exit_list_reader:
        print(linea)

os.system("rm Tor_ip_list_EXIT.csv")

