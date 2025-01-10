# This manifest kills a process named killmenow.
exec { 'Kills killmenow':
  command => '/usr/bin/pkill killmenow',
}
