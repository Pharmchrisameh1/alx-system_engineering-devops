# This manifest fixes the webstack debugging task #1 containter
file { 'change_holberton_limits':
  ensure  => file,
  path    => '/etc/security/limits.conf',
  content => 'holberton hard nofile 4096
holberton soft nofile 1024',
}
