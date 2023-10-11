# fixes an error in container
exec { 'fix-php-config':
  command   =>  '/usr/bin/env sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
exec { 'restart-server':
  command   =>  '/usr/bin/env sudo service apache2 restart'
}
