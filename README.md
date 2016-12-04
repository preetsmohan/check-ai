# check-ai
UofM EECS 441: Mobile App Development for Entrepreneurs Project


#How to Deploy
If you're Sarthak, Brandon or Preeti, you can deploy the site. Instructions adapted from https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04

1. SSH into the DigitalOcean server
2. Ensure the following system files are as follows:


/etc/systemd/system/checkai.service

```[Unit]
Description=Gunicorn instance to serve myproject
After=network.target

[Service]
User=bwaggone
Group=www-data
WorkingDirectory=/home/bwaggone/checkai
Environment="PATH=/home/bwaggone/check-ai/venv/bin"
ExecStart=/home/bwaggone/check-ai/venv/bin/gunicorn --workers 3 --bind unix:myproject.sock -m 007 wsgi:app

[Install]
WantedBy=multi-user.target
```

/etc/nginx/sites-available/checkai
```
server {
    listen 80;
    server_name 138.197.40.0;

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/bwaggone/check-ai/checkai.sock;
    }
}
```
