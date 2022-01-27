# pyspotify

### Install mongodb
- Windows:
https://fastdl.mongodb.org/win32/mongodb-win32-x86_64-2012plus-4.2.7-signed.msi

- Linux:
https://repo.mongodb.org/apt/debian/dists/buster/mongodb-org/4.2/main/binary-amd64/mongodb-org-server_4.2.7_amd64.deb

Get a token
https://developer.spotify.com/console/get-current-user/

### Instalação de pacotes necessários.

```bash
$ vim .env
```

```env
# copy and paste to .env file
# set values according to your configuration
TOKEN = 
MONGO_HOST = localhost
MONGO_PORT = 27017
```

```bash
$ pip install -r requirements.txt
```
