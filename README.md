#SSB - Super Space Blog
SSB is the blog project that goes like 
thesis in Hillel course Python Advanced, made by student Kertsman Kostiantyn.

#Install all requirements.
You need to install all requirements for project, using package manager [pip](https://pip.pypa.io/en/stable/).
```bash
$ pip install -r requirements.txt
```

#Start project DEBUG-MODE.
First you have to configure ./src/Django1/setting.py 
```python
DEBUG = False
```
For local start use command from Makefile, previously being in the project root directory (Django1) :
```bash
$ make run
```

#Start project in uWSGI & NGiNX localy :
Step 1:
Firstly you need to get NGiNX in your computer environment.
```bash
$ sudo brew install nginx
```

Step 2: You need to configure nginx.conf
```bash
$ cd /usr/local/etc/nginx/
$ nano nginx.conf
```
Delete all content and Paste that code:
```bash
events{}

http{
  server {
    listen 80;
    listen [::]:80;

    server_name 127.0.0.1 ssb.com;
    location /static/ {
      root /Users/user/wks/srs/githubb.com/kokakerze/Django1/static_content/;
}

    location / {
      proxy_pass http://127.0.0.1:8081;
}
}
}
```

*For starting and restarting NGiNX:
```bash
$ sudo brew services restart nginx
```

Step 4: Turn on GUNICORN workers:
Previously being in the project root directory (Django1) 
```bash
$ gunicorn-run
```

