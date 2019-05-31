# https://www.puppetcookbook.com/posts/restart-a-service-when-a-file-changes.html
exec { 'fix-ULIMIT':
  command => 'echo "ULIMIT=\'-n 4096\'" > /etc/default/nginx && /etc/init.d/nginx restart',
  path    => '/bin',
}
