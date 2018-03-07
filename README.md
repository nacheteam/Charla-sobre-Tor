**Tor, ¿la herramienta definitiva de anonimato?**
========================================================

**Charla en vídeo:** https://vimeo.com/214392014

En este repositorio se incluyen las diapositivas utilizadas en la charla, demos técnicas
sobre Tor y enlaces de interés para indagar más sobre el tema.  
Se incluye en la carpeta de información un fichero con enlaces de interés sobre Tor y un pdf con información sobre la charla publicado en meetup.  


Demos Técnicas
----------------------------------------------------------

* Tor exit nodes discovery:  

Para la ejecución de este programa se precisa que el sistema sea linux y que se tenga instalado Tor.  
En una distro debian:  
```bash
sudo apt -y install tor
```
Se precisa también la versión 3 de python:  
```bash
sudo apt -y install python3
```
Para la ejecución del programa para descubrir nodos de salida en Tor se debe aplicar el siguiente comando:  
```bash
sudo python3 tor_exit_discovery.py
```

Con este script se genera un txt con las ips de los nodos de salida que se descubran. Si el programa es matado antes de que acabe el número de iteraciones programado no ocurre nada,
los datos serán guardados igualmente en el fichero de salida.


* Tor exit nodes analysis:

Para la ejecución de este programa se necesita que el sistema sea linux, tener acceso a internet y nmap.  
La forma de ejecutar el script es:  
```bash
sudo python3 exit_nodes_analysis.py
```

El programa genera una carpeta con los resultados de la ejecución. En la misma se encontrará un fichero por cada ip de los nodos de salida con los resultados obtenidos por nmap.
