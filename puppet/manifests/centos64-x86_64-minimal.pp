# cd /vagrant/puppet/manifests/
# puppet apply -v centos64-x86_64-minimal.pp --modulepath=/vagrant/puppet/modules/ --noop
# puppet apply -v centos64-x86_64-minimal.pp --modulepath=/vagrant/puppet/modules/

# puppet examples
include selinux
include motd
include openssh
include httpd
