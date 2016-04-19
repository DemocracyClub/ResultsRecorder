from resultsrecorder.utils.test import TestCase

class SmokeTest(TestCase):
    def test_login(self):
        self.assertGET(200, 'account:login')

class LogoutTest(TestCase):
    def test_post(self):
        self.assertPOST({}, 'account:logout')

    def test_get_logged_out(self):
        self.assertGET(200, 'account:logout', login=True)

    def test_get_logged_out(self):
        self.assertGET(302, 'account:logout')

    def test_post_logged_out(self):
        self.assertPOST({}, 'account:logout')
