import unittest
import validador_cpf_python

class RoteiroTesteParticionamento(unittest.TestCase):

    def test_ct01(self):
        res = validador_cpf_python.cpf_validate("98601567002")
        self.assertEqual(res, 'valido')

    def test_ct02(self):
        res = validador_cpf_python.cpf_validate("76360980048")
        self.assertEqual(res, 'invalido')

    def test_ct03(self):
        res = validador_cpf_python.cpf_validate("58071132092")
        self.assertEqual(res, 'invalido')

    def test_ct04(self):
        res = validador_cpf_python.cpf_validate("6495654032")
        self.assertEqual(res, 'invalido')

    def test_ct05(self):
        res = validador_cpf_python.cpf_validate("526997370702")
        self.assertEqual(res, 'invalido')

    def test_ct06(self):
        res = validador_cpf_python.cpf_validate("22119007")
        self.assertEqual(res, 'invalido')

    def test_ct07(self):
        res = validador_cpf_python.cpf_validate("11111111111")
        self.assertEqual(res, 'invalido')

class RoteiroTesteEstrutural(unittest.TestCase):

    def test_ct01(self):
        res = validador_cpf_python.cpf_validate("98601567002")
        self.assertEqual(res, 'valido')

    def test_ct02(self):
        res = validador_cpf_python.cpf_validate("76360980048")
        self.assertEqual(res, 'invalido')

    def test_ct03(self):
        res = validador_cpf_python.cpf_validate("22119007")
        self.assertEqual(res, 'invalido')

    def test_ct04(self):
        res = validador_cpf_python.cpf_validate("11111111111")
        self.assertEqual(res, 'invalido')

if __name__ == "__main__":
    unittest.main()