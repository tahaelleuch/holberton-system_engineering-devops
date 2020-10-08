# Using Puppet, fix nginx ulimiz

exec { 'fix':
command  => 'sudo sed -i 's/15/4096/g' /etc/default/nginx
service nginx restart',
provider => 'shell',
}
