# Using Puppet, change-os-configuration-for-holberton-user

exec { 'fix os':
command  => "sudo sed -i 's/holberton hard nofile 5/holberton hard nofile 6000/g' /etc/security/limits.conf
sudo sed -i 's/holberton soft nofile 4/holberton soft nofile 6000/g' /etc/security/limits.conf",
provider => 'shell',
}
