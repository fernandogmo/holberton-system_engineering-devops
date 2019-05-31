# puppet file to change ulimit for holberton user 

file {'/etc/security/limits.conf' :
    ensure =>  present
}
-> exec { 'change_hardLimit' :
    path    =>  '/bin',
    command =>  'sed -i --follow-symlinks s/5/10000/ /etc/security/limits.conf'
}
-> exec { 'change_softLimit' :
    path    =>  '/bin',
    command =>  'sed -i --follow-symlinks s/4/200/ /etc/security/limits.conf'
}

