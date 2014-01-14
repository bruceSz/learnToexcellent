def get_env():
    env={}
    env['OS_AUTH_URL']='http://9.111.114.77:5000/v2.0/'
    env['OS_USERNAME']='sceagent'
    env['OS_PASSWORD']='openstack1'
    env['OS_TENANT_NAME']='Public'
    env['OS_REGION_NAME']='regionOne'
    return env

ENV=get_env()
