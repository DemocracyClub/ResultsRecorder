from resultsrecorder.utils.test import TestCase

class SmokeTests(TestCase):
    def test_landing(self):
        self.assertGET(200, 'static:landing')
