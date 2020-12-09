# ssh configuration
exec { 'echo':
command  =>'echo "PasswordAuthentication no\nIdentityFile ~/.ssh/holberton"  >>  /etc/ssh/ssh_config',
path     => '/bin',
provider => 'shell',
}