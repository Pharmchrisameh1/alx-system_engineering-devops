This manifest solves the Web Stack Debugging 03
exec { 'Fix Typo':
  provider => shell,
  command  => "sudo sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
}
