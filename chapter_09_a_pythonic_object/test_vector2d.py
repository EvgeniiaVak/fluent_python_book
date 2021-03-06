import unittest

from chapter_09_a_pythonic_object.vector2d import Vector2d


class Vector2dTestCase(unittest.TestCase):

    def test_private_attributes(self):
        v = Vector2d(5, 9)
        v._Vector2d__x = 4
        self.assertEqual(v.x, 4)

    def test_hashable(self):
        v = Vector2d(2, 1)
        self.assertEqual(hash(v), 3)

    def test_immutability(self):
        v = Vector2d(1, 1)
        with self.assertRaises(AttributeError):
            v.x = 3

    def test_format_polar(self):
        v = Vector2d(-3, 4)
        self.assertEqual(f'{v:.2fp}', '(5.00, 2.21)')

    def test_format_regular(self):
        v = Vector2d(2, 17)
        self.assertEqual(f'{v:.2f}', '(2.00, 17.00)')

    def test_frombytes(self):

        source_vector = Vector2d(4, 5)
        vector_bytes = bytes(source_vector)
        result_vector = Vector2d.frombytes(vector_bytes)

        self.assertEqual(result_vector, source_vector)


if __name__ == '__main__':
    unittest.main()
