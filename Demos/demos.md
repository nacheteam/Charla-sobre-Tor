**Demostraciones de Tor**
=====================================================================================================

1. Ejecutar curl a través de Tor:
```bash
curl --socks5-hostname localhost:9050 https://check.torproject.org/ | grep 'Tor\.'
```
