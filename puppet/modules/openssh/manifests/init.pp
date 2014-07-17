# the package, file, service pattern

class openssh {
  
  package { 'openssh-server':
    ensure  => present,
    before  => File['/etc/ssh/sshd_config'],
  }
  
  file { '/etc/ssh/sshd_config':
    ensure  => file,
    owner   => 'root',
    group   => 'root',
    mode    => '0600',
    source  => "puppet:///modules/openssh/sshd_config",
  }
  
  service { 'sshd':
    ensure     => running,
    enable     => true,
    subscribe  => File['/etc/ssh/sshd_config'],
  }

}
