# fixed the Apache 500 typo error in wordpress
exec { 'fix typo':
  onlyif  => 'test -e /var/www/html/wp-settings.php',
    command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
      path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
      }
