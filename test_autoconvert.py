from unittest import TestCase

from autoconvert import from_string, to_string

class Test(TestCase):
    def test(self):
        for value in (
            'a',
            '1',
            '1.5',
            '2009-11-29T23:45:33',
            'False',
            ):
            self.assertEqual(to_string(from_string(value)), value)
