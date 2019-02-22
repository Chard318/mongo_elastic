# ECEN-403
Automatic Profile Generation Using Structured & Unstructured Data

## Overall Design
Ubuntu 18.04 VM
    Docker Containers
        NLP Tools
        MongoDB + Elasticsearch
        Django -> nginx + uWSGI

## Backend
Web Framework: Django
Web Server: NGINX
Web Server Gatway Interface: uWSGI
Database Connectors: Elasticsearch-dsl, Djongo, Pymongo

### apt-get install:
  nginx

### pip3 install:
  asn1crypto==0.24.0
  attrs==17.4.0
  Automat==0.6.0
  blinker==1.4
  certifi==2018.1.18
  chardet==3.0.4
  click==6.7
  cloud-init==18.3
  colorama==0.3.7
  command-not-found==0.3
  configobj==5.0.6
  constantly==15.1.0
  cryptography==2.1.4
  distro-info==0.18
  Django==2.1.5
  httplib2==0.9.2
  hyperlink==17.3.1
  idna==2.6
  incremental==16.10.1
  Jinja2==2.10
  jsonpatch==1.16
  jsonpointer==1.10
  jsonschema==2.6.0
  keyring==10.6.0
  keyrings.alt==3.0
  language-selector==0.1
  MarkupSafe==1.0
  netifaces==0.10.4
  oauthlib==2.0.6
  PAM==0.4.2
  Pillow==5.3.0
  pyasn1==0.4.2
  pyasn1-modules==0.2.1
  pycrypto==2.6.1
  pygobject==3.26.1
  PyJWT==1.5.3
  pyOpenSSL==17.5.0
  pyserial==3.4
  python-apt==1.6.2
  python-debian==0.1.32
  pytz==2018.9
  pyxdg==0.25
  PyYAML==3.12
  requests==2.18.4
  requests-unixsocket==0.1.5
  SecretStorage==2.3.1
  service-identity==16.0.0
  six==1.11.0
  ssh-import-id==5.7
  systemd-python==234
  Twisted==17.9.0
  ufw==0.35
  unattended-upgrades==0.1
  urllib3==1.22
  uWSGI==2.0.17.1
  WALinuxAgent==2.2.20
  zope.interface==4.3.2


## Django Details
App structure: searchsite
    models - Database Storage 
    templates - html templates for veiws
    static - CSS for templates, JS for templates, images, and documents stored
