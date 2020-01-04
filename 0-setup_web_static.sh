#!/usr/bin/env bash
#
# Set up Holberton web servers for the deployment of web_static

apt update
apt -y install nginx

mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test

cat - >| /data/web_static/releases/test/index.html << 'EOF'
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

ln -f -n -s releases/test /data/web_static/current
chown -h -R ubuntu:ubuntu /data

sed -E -i '
\@^\tlocation\s+/\s+\{$@!b
i location /hbnb_static { alias /data/web_static/current; }
: done
n
b done
' /etc/nginx/sites-available/default

service nginx restart

ufw allow 'Nginx HTTP'
