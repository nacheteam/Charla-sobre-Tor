import os
import csv
import subprocess

ips_nodos_salida = []

os.system("wget https://torstatus.blutmagie.de/ip_list_exit.php/Tor_ip_list_EXIT.csv")
with open("Tor_ip_list_EXIT.csv", 'r') as exit_list:
    exit_list_reader = csv.reader(exit_list, delimiter=' ', quotechar='|')
    for linea in exit_list_reader:
        ips_nodos_salida.append(linea)

os.system("rm Tor_ip_list_EXIT.csv")
for ip in ips_nodos_salida:
    comando = "nmap -vv -A --reason " + ip
    nmap_nodo = subprocess.Popen(['/bin/sh', '-c', comando], stdout=subprocess.PIPE)
