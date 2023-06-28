# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => '
    server {
      listen 80 default_server;
      listen [::]:80 default_server;
      root /var/www/html;
      index index.html;
      location / {
        echo "Hello World!";
      }
      location /redirect_me {
        return 301 https://www.example.com/;
      }
    }
  ',
  notify  => Service['nginx'],
}

# Remove default Nginx configuration
file { '/etc/nginx/sites-enabled/default':
  ensure => absent,
}

# Enable Nginx default site
file { '/etc/nginx/sites-enabled/default':
  ensure  => link,
  target  => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
  notify  => Service['nginx'],
}

# Restart Nginx service
service { 'nginx':
  ensure    => running,
  enable    => true,
  hasstatus => true,
  require   => Package['nginx'],
}
