import glanceclient.v2.client as glclient
from get_token import KEYSTONE as keystone
def get_glance():
    glance_endpoint = keystone.service_catalog.url_for(service_type='image')
    glance = glclient.Client(glance_endpoint,token=keystone.auth_token) 
    return glance

if __name__ == '__main__':
    gl = get_glance()
    images = gl.images.list()
    for  img  in images:
        print img
