# Set up Holberton web servers for the deployment of web_static

$index_html = "\
<html>
  <head></head>
  <body>Hello World</body>
</html>
"

$hbnb_static_match = '^\tlocation\s+/\s+\{$'
$hbnb_static_line = "\
	location /hbnb_static {
		alias /data/web_static/current;
	}
	location / {
"

package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure     => running,
  hasrestart => true,
  require    => Package['nginx'],
}

file { 'data':
  ensure => directory,
  path   => '/data',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { 'web_static':
  ensure  => directory,
  path    => '/data/web_static',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => File['data'],
}

file { 'current':
  ensure  => link,
  replace => true,
  path    => '/data/web_static/current',
  target  => '/data/web_static/releases/test',
  require => File['web_static'],
}

file { 'releases':
  ensure  => directory,
  path    => '/data/web_static/releases',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => File['web_static'],
}

file { 'shared':
  ensure  => directory,
  path    => '/data/web_static/shared',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => File['web_static'],
}

file { 'test':
  ensure  => directory,
  path    => '/data/web_static/releases/test',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => File['releases'],
}

file { 'index_html':
  ensure  => file,
  path    => '/data/web_static/releases/test/index.html',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  content => $index_html,
  require => File['test'],
}

file_line { 'hbnb_static':
  ensure  => present,
  line    => $hbnb_static_line,
  match   => $hbnb_static_match,
  require => Package['nginx'],
  notify  => Service['nginx'],
}

exec { 'ufw':
  command => "ufw allow 'Nginx HTTP'",
  path    => '/usr/sbin:/usr/bin:/sbin:/bin',
  require => Package['nginx'],
}
