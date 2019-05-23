# This file fixes a type in WP settings in a Holberton server
exec { 'fix-wordpress':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/bin',
}
