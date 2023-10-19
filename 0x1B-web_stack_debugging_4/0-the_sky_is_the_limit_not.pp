# A script that increases the amount of traffic nginx server can handle

# increase the limit for open files
exec { 'increase limit for open files':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
}

# restart nginx
exec { 'restart nginx':
  command => '/usr/sbin/service nginx restart',
}
