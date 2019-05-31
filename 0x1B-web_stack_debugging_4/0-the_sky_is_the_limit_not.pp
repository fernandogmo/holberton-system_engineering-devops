# https://www.puppetcookbook.com/posts/restart-a-service-when-a-file-changes.html
exec { 'fix-limit':
  command => 'sed -i s/15/1024/ /etc/default/nginx',
  path    => '/bin',
}

service { 'nginx-restart':
    ensure    => running,
    subscribe => Exec['fix-limit'],
}
