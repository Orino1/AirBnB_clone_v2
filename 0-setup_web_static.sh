#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static.
if ! dpkg -l | grep -q nginx; then
    apt-get -y update
    apt-get -y upgrade
    apt-get -y install nginx
fi
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
echo "<html>
  <head>
  </head>
  <body>
    Oh im working :)
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -hR ubuntu:ubuntu /data/
sed -i '51 i \\n\tlocation /hbnb_static {\n\talias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default
service nginx restart