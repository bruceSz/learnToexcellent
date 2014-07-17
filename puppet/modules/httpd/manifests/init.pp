# package , file, service pattern

class httpd {
    package {
        'httpd':ensure => installed,
        before => Exec['change_port.sh']
    }
    package {'mod_wsgi':ensure => installed,}

    package {'mysql-server':
    ensure=>installed,
    }

    file { '/tmp/change_port.sh':
        ensure => file,
        owner => 'vagrant',
        group => 'vagrant',
        mode => '0711',
        source =>"puppet:///modules/httpd/change_port.sh",
        before => Exec['change_port.sh'],
    }

    exec{ "change_port.sh":
        command=>"bash  /tmp/change_port.sh",
        path => '/bin',
    }

    #service {'httpd':ensure => running,}
    exec {'httpd service start':
        command => 'sudo service httpd start',
        path => ["/sbin","/usr/bin"],
    }
    service {'mysqld':ensure=>running,}
}
