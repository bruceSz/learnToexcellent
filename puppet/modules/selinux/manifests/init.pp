class selinux {

    file { "/etc/selinux/config":
      ensure => present,
      owner  => 'root',
      group  => 'root',
      mode   => '0644',
      source => "puppet:///modules/selinux/selinux",
    }

}
