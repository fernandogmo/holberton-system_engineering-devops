# Change the OS configuration so that it is possible to
# login with the holberton user and open a file without any error message.
file {'/etc/security/limits.conf' :
    ensure =>  present
}
-> exec { 'increase-hard-limit' :
    command =>  'sed -i "/holberton hard/s/5/20000/" /etc/security/limits.conf',
    path    =>  '/bin'
}
-> exec { 'increase-soft-limit' :
    command =>  'sed -i "/holberton soft/s/4/10000/" /etc/security/limits.conf',
    path    =>  '/bin'
}

