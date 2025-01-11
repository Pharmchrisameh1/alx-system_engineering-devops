# This puppet script make changes to the local
# ssh client configuration file.
file { "ssh_config":
  path => "/etc/ssh/ssh_config",
  ensure => 'present',
  content => "Host *\n\tIdentityFile ~/.ssh/school\t\nPasswordAuthentication no",
}
