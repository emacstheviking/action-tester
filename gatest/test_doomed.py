from django.test import SimpleTestCase

class DeathOrGloryTest(SimpleTestCase):
    def test_always_fails(self):
        # main: Test will pass
        # failit: Test will fail
        self.assertTrue(True)

