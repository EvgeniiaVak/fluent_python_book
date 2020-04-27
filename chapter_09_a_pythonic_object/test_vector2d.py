import unittest

from chapter_09_a_pythonic_object.vector2d import Vector2d


class Vector2dTestCase(unittest.TestCase):

    def test_frombytes(self):

        source_vector = Vector2d(4, 5)
        vector_bytes = bytes(source_vector)
        result_vector = Vector2d.frombytes(vector_bytes)

        self.assertEqual(result_vector, source_vector)


if __name__ == '__main__':
    unittest.main()
