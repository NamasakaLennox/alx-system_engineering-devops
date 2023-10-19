# changed the soft and hard ulimit limitation

exec { 'comment out limit':
  command => '/bin/sed -i "s/holberton/#holberton/" /etc/security/limits.conf',
}
