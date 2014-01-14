#from os import environ as env
from config import ENV as env
import keystoneclient.v2_0.client as ksclient

def get_keystone():
    keystone=ksclient.Client(auth_url=env['OS_AUTH_URL'],
                            username=env['OS_USERNAME'],
                            password=env['OS_PASSWORD'],
                            tenant_name=env['OS_TENANT_NAME'],
                            region_name=env['OS_REGION_NAME'])
    return keystone

KEYSTONE=get_keystone()

if __name__ == '__main__':
    ks = get_keystone()
    for k,v in ks.__dict__.items():
        print k,v
