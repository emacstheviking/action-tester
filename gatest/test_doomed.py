from django.test import SimpleTestCase

class DeathOrGloryTest(SimpleTestCase):
    def test_always_fails(self):
        # f3review: not only will this fail but it will need
        # manual reviewer intervention as the branch rule now
        # insists on minumum 1 reviewer.
        self.assertEqual(42,999)

