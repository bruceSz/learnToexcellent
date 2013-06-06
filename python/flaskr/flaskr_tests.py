import os
import flaskr
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd,flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        flaskr.app.config['TESTING'] = True
        self.app = flaskr.app.test_client()
        flaskr.init_db()
    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskr.app.config['DATABASE'])

    def test_empty_db(self):
        rv = self.app.get('/')
        assert 'no entries here so far' in rv.data

    def login(self,username,password):
        return self.app.post('/login',data=dict(
                username=username,
                password=password
                ),follow_redirects=True)
    
    def logout(self):
        return self.app.get('/logout',follow_redirects=True)

    def test_login_logout(self):
        rv = self.login('admin','default')
        assert 'you are logged in' in rv.data
        rv = self.logout()
        assert 'you were logged out' in rv.data
        rv = self.login('dd','default')
        assert 'invalid username' in rv.data
        rv = self.login('admin','dd')
        assert 'invalid password' in rv.data


if __name__ == '__main__':
    unittest.main()
