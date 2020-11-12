import unittest

from utils.prototype import Prototype, A


class TestPrototye(unittest.TestCase):
    def setUp(self):
        self.a = A(1)
        self.b = self.a.clone()
        self.c = self.b.clone()


class TestInitPrototype(TestPrototye):
    def test_A(self):
        self.assertTrue(isinstance(self.a, A))

    def test_A_is_a_Prototype(self):
        self.assertTrue(isinstance(self.a, Prototype))


class TestPrototypeClone(TestPrototye):
    def test_clone_b_is_an_A(self):
        self.assertTrue(isinstance(self.b, A))

    def test_clone_b_is_not_a(self):
        self.assertNotEqual(self.a, self.b)

    def test_can_clone_b_to_c(self):
        self.assertTrue(isinstance(self.c, A))


if __name__ == '__main__':
    unittest.main()
