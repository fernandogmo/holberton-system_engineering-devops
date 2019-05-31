# https://www.puppetcookbook.com/posts/restart-a-service-when-a-file-changes.html
exec { 'fix-ULIMIT':
  command => 'echo "ULIMIT=\'-n 4096\'" > /etc/default/nginx &&  /etc/init.d/nginx restart',
  path    => '/bin',
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}

file { '/etc/default/nginx':
  notify  => Service['nginx'],  # this sets up the relationship
  mode    => '0600',
  owner   => 'root',
  group   => 'root',
  require => Package['nginx'],
}
