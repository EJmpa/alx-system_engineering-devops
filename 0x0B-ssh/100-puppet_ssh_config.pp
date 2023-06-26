# Create ssh congig file using puppet
file_line { 'Turn off passwd auth':
  ensure => 'present',
  path   => '/etc/ssh/config',
  line   => 'PasswordAuthentication no',
}

file_line { 'Declare identity file':
  ensure => 'present',
  path   => '/etc/ssh/config',
  line   => 'IdentityFile ~/.ssh/school',
}
