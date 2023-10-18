# A script that increases the amount of traffic nginx server can handle

# increase the limit for open files
exec { 'increase limit for open files':
  command => 'sed -i "s/15/2000/" /etc/default/nginx',
  path    => '/usr/bin/env'
}

# restart nginx
exec { 'restart nginx':
  command => 'service nginx restart',
  path    => '/usr/bin/env'
}
