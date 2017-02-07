import os
import subprocess

os.system("rm ips.txt ; touch ips.txt ; chmod a+wr ips.txt")
comando_inicial = "sudo /etc/init.d/tor start"
inicio_tor = subprocess.Popen(['/bin/bash', '-c', comando_inicial])
ips_nodos_salida = []
fichero_salida = open("ips.txt", 'r+')

for i in range(1,1000000):
    os.system("clear")
    print("Iteración: " + str(i))
    comando = "curl --socks5 localhost:9050 ipinfo.io/ip ; sudo /etc/init.d/tor restart"
    busqueda_ips = subprocess.Popen(['/bin/sh', '-c', comando], stdout=subprocess.PIPE)

    for line in busqueda_ips.stdout:
        linea = str(line)
        if not linea[2:-3] in ips_nodos_salida and not "tor" in linea:
            ips_nodos_salida.append(linea[2:-3])
            fichero_salida.write(linea[2:-3]+"\n")

contador=1
for ip in ips_nodos_salida:
    print("[X] IP-" + str(contador) + ": " + ip)
    contador+=1
    
fichero_salida.close()
