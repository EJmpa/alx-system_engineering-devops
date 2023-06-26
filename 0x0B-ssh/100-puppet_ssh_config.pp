# puppet script - configure ssh authentication:

file_line { 'Turn off passwd auth':
<<<<<<< HEAD
  ensure => 'present',
  path   => '/etc/ssh/config',
  line   => 'PasswordAuthentication no',
}

file_line { 'Declare identity file':
  ensure => 'present',
  path   => '/etc/ssh/config',
  line   => 'IdentityFile ~/.ssh/school',
=======
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}

file_line { 'Declare identity file':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
}

service { 'ssh':
  ensure => running,
  enable => true,
>>>>>>> 60b42c05b8f0c47ba1c08d25d5604d77a7d0a2ec
}
