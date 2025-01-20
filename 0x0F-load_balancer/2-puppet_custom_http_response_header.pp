# This manifest configures brand new Ubuntu machine to install
# NGINX and make it return a X-Served-By response header with
# the value of the server's hostname.
exec { 'setup':
  command  => 'sudo apt update;
  sudo apt-get install -y nginx;
  sudo sed -i "/root \/var\/www\/html;/a add_header X-Served-By $HOSTNAME;\n" /etc/nginx/sites-available/default;
  sudo service nginx restart',
  provider => shell,
}
