# Django_base

###installation
```
sudo apt-get install postgresql-9.4
pip install -r requirements.txt
```

###config
```
cd django_base/settings
cp production.py local_settings.py
```

###Usage
```
fab deploy_local
```
or 
```
fab deploy_prod
```
