# Install required packages (if not already installed)
package { 'apache2':
  ensure => 'installed',
}

# Ensure the configuration directory exists
file { '/etc/apache2/conf.d':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
  mode   => '0755',
}

# Add the missing configuration file for custom PHP module
file { '/etc/apache2/conf.d/mod_custom_php.conf':
  ensure  => 'present',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "# Load custom PHP module\nLoadModule custom_php_module /usr/lib/apache2/modules/mod_custom_php.so\n\n<IfModule custom_php_module>\n,
  require => File['/etc/apache2/conf.d'],
}

# Stop the Apache service (if running)
service { 'apache2':
  ensure => 'stopped',
  enable => false,
}

# Start the Apache service
service { 'apache2':
  ensure => 'running',
  enable => true,
  require => File['/etc/apache2/conf.d/mod_custom_php.conf'],
}
