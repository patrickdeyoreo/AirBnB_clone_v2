# Set up Holberton web servers for the deployment of web_static

$index_html = "\
<html>
  <head>
  </head>
  <body>
    Hello World
  </body>
</html>
"
$hbnb_static_match = '^\s*listen\s+80\s+default_server;\s*$'
$hbnb_static_line = "\
	location /hbnb_static/ {
		alias /data/web_static/current/;
	}
	listen 80 default_server;
"
$data_dirs =  [ '/data',
                '/data/web_static',
                '/data/web_static/releases',
                '/data/web_static/releases/test',
                '/data/web_static/shared',
]

package { 'nginx': }

service { 'nginx':
  ensure     => 'running',
  hasrestart => true,
  require    => Package['nginx'],
}

file { $data_dirs:
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/current':
  ensure  => 'link',
  replace => 'yes',
  target  => '/data/web_static/releases/test',
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  content => $index_html,
}

exec { "sed -i '/^\tlisten 80 default_server;$/a location /hbnb_static/ { alias /data/web_static/current/;":
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

exec { "ufw allow 'Nginx HTTP'":
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  require => Package['nginx'],
}
