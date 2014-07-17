class motd {

    file { "/etc/motd":
      ensure => present,
      owner  => 'root',
      group  => 'root',
      mode   => '0644',
      source => "puppet:///modules/motd/motd",
    }

}