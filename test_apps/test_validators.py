import unittest

from ..apps.validators import Validators


class TesteIdentfValidatord(unittest.TestCase):

    def test_validator_min_limit(self):
        result = Validators.check_valid_identifier(self, "aaa")
        self.assertTrue(result)

    def test_validator_over_min_limit(self):
        result = Validators.check_valid_identifier(self, "aa")
        self.assertFalse(result)

    def test_validator_max_limit(self):
        result = Validators.check_valid_identifier(self, "aaaaaaaaa")
        self.assertTrue(result)

    def test_validator_over_max_limit(self):
        result = Validators.check_valid_identifier(self, "aaaaaaaaaaa")
        self.assertFalse(result)

    def test_validator_sublinhado(self):
        result = Validators.check_valid_identifier(self, "_inicio")
        self.assertTrue(result)

    def test_validator_sublinhado_meio(self):
        result = Validators.check_valid_identifier(self, "meio_")
        self.assertTrue(result)

    def test_validator_especial_caractere(self):
        result = Validators.check_valid_identifier(self, "ddd@")
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
