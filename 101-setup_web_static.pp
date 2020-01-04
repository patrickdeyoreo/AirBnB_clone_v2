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
	listen 80 default_server;

	location /hbnb_static/ {
		alias /data/web_static/current/;
	}
"
$data_dirs =  [ '/data',
                '/data/web_static',
                '/data/web_static/releases',
                '/data/web_static/releases/test',
                '/data/web_static/shared',
]

package { 'nginx':
  ensure  => 'installed',
}

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

file_line { 'hbnb_static':
  ensure  => 'present',
  line    => $hbnb_static_line,
  match   => $hbnb_static_match,
  require => Package['nginx'],
  notify  => Service['nginx'],
}

exec { "ufw allow 'Nginx HTTP'":
  path    => '/usr/sbin:/usr/bin:/sbin:/bin',
  require => Package['nginx'],
}
