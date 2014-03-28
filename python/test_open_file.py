uniq_name='/opt/stack/horizon/openstack_dashboard/local/localhost.localdomain'
try:
    open(uniq_name,'wb').close()
except IOError:
    print "error!!!"


