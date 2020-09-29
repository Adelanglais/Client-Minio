# Client-Minio

L'objectif de ce code est d'initialiser un client **Minio** afin de pouvoir manipuler des objets sur le serveur.
Ici, après avoir lancé un container minio, on initialise un bucket dans lequel on place un fichier text. On retourne l'url de cet objet afin de pouvoir y accéder.

## Installation
_se placer dans le répertoire WORKDIR pour créer le container minio_
``` bash
./docker-entrypoint.sh
```
_se placer dans le répertoire minioConnect_
```bash 
source .venv_minio/bin/activate
pip install -r requirements.txt
```

## Utilisation
```python
python3 minio_script.py
```

## Quitter l'installation
```bash
deactivate
docker rm -f minio1
```
