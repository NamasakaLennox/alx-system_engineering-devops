# changed the soft and hard ulimit limitation

exec { 'comment out limit':
  command => 'sed -i "s/holberton/#holberton/" /etc/security/limits.conf',
  path    => '/usr/bin/env'
}
