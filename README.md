# Python Mongodb Example

Example how to use mongodb in python

## Prerequisite
</br>

### **Python 3** 
to install please see following link 

Windows  [Download](https://www.python.org/downloads/release/python-3100/)

Linux   [Download](https://www.python.org/downloads/source/)

MacOs [Download](https://www.python.org/downloads/macos/)

</br>

### **Mongodb** 

#### **Docker version**

if you wish to install via docker please make sure you already install docker in your system by invoking following command in your terminal / console

```bash
docker version
```

you should see following information if you have it

```bash

Client: Docker Engine - Community
 Version:           20.10.10
 API version:       1.41
 Go version:        go1.16.9
 Git commit:        b485636
 Built:             Mon Oct 25 07:42:59 2021
 OS/Arch:           linux/amd64
 Context:           default
 Experimental:      true

Server: Docker Engine - Community
 Engine:
  Version:          20.10.10
  API version:      1.41 (minimum version 1.12)
  Go version:       go1.16.9
  Git commit:       e2f740d
  Built:            Mon Oct 25 07:41:08 2021
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.4.11
  GitCommit:        5b46e404f6b9f661a205e28d59c982d3634148f8
 runc:
  Version:          1.0.2
  GitCommit:        v1.0.2-0-g52b36a2
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0
```

if **not** have docker in youir machine  please see in following link to install docker [Docker Installation Link](https://docs.docker.com/get-docker/)

install mongodb via docker

```bash
docker run --name mongodb -p 27017:27017  -d mongo:latest
```

this command will expose your mongodb port to host machine

</br>

#### **Native version**

Please see following link to install mongodb natively in your machine [Mongodb Installation](https://docs.mongodb.com/manual/installation/)

</br>

## Run the example

Make sure you already installed venv as package manager in your python environment

Windows

```bash
py -m pip install --user virtualenv
```

OSX/Linux

```bash
python3 -m pip install --user virtualenv
```

Activate your venv

Windows

```bash
.\env\Scripts\activate
```

OSX/Linux

```bash
source env/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install -r requirements.txtpip install foobar
```

## Usage

```bash

python3 filename.py
```
