import os
import csv
import subprocess

ips_nodos_salida = []

print("Obteniendo fichero con información de nodos de salida.")
os.system("sleep 3")
os.system("wget https://torstatus.blutmagie.de/ip_list_exit.php/Tor_ip_list_EXIT.csv > /dev/null")
with open("Tor_ip_list_EXIT.csv", 'r') as exit_list:
    exit_list_reader = csv.reader(exit_list, delimiter=' ', quotechar='|')
    for linea in exit_list_reader:
        ips_nodos_salida.append(str(linea)[2:-2])

os.system("rm Tor_ip_list_EXIT.csv > /dev/null")
contador = 0
total = len(ips_nodos_salida)
os.system("rm -rf ./Resultados/")
os.system("mkdir Resultados")
for ip in ips_nodos_salida:
    os.system("clear")
    contador += 1
    print(ip)
    print("Realizando analisis " + str(contador) + "/" + str(total))
    comando = "nmap -v -O -T5 " + ip + " >> ./Resultados/" + ip + ".txt"
    nmap_nodo = subprocess.Popen(['/bin/sh', '-c', comando], stdout=subprocess.PIPE)
    nmap_nodo.communicate()

os.system("chmod -R a+rw Resultados")
