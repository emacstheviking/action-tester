from django.test import SimpleTestCase

class DeathOrGloryTest(SimpleTestCase):
    def test_always_fails(self):
        # failit: Test will fail
        self.assertEqual(0,1)

