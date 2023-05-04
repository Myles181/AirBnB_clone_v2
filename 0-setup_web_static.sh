#!/usr/bin/env bash
# A bash script that sets up web servers for deployment

#install nginx if it's not already installed
if [! -d /etc/nginx ]; then
	sudo apt update
	sudo apt install nginx
	sudo ufw allow "Nginx HTTP"
	echo "server {
	 listen 80 default_server;
	 listen [::]:80 default_server;
	 add_header X-Server-By $HOSTNAME;
	 root /var/www/html;
	 index index.html index.htm index.nginx-debian.html;
	 server_name _;
	 location /redirect_me {
	 	return 301 https://javascript.info;
	}
	location / {
		try_files \$uri \$uri/ =404;
	}
	error_page 404 /error_page.html;
	location = /error_page/html {
		root /var/www/html;
		internal;
	}
}" | sudo tee /etc/nginx/sites_available/default
	echo "Hello World!" | sudo tee /var/www/html/error_page.html
	echo "Ceci n'est pas une page" | sudo tee /var/www/html/error_page.html
	sudo service nginx start
fi

	#create directories if they don't exist
	mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
	#create the file /data/web_static/releases/test/index.html if doesn't exist
	echo "
	<!DOCTYPE html>
	<html>
	    <head>
        	<!-- head definitions go here -->
		Website
	    </head>
	    <body>
	        <!-- the content goes here -->
		<p>Hello World!</p>
	    </body>
	</html>" > sudo tee /data/web_static/releases/test/index.html

	# delete the directory /data/web_static/current if it exists
	if [[ -L /data/web_static/current ]]; then
		    sudo rm -rf /data/web_static/current
	fi

	#create a symbolic link file /current to the /test/ directory
	ln -s /data/web_static/releases/test/" "/data/web_static/current

	#Give ownership of the /data/ folder to the ubuntu user AND group
	sudo chown -R ubuntu:ubuntu /data/

	# update nginx to serve the content of /data/web_static/current to hbnb_static

	sudo sed -i "s/server_name _;/server_name _;\n\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t\ttry_files index.html 0-index.html =404;\n\t}/" /etc/nginx/sites-available/default

	sudo service nginx restart
