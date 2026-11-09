import unittest
from unittest.mock import patch, mock_open
import sys
import os

# Add the root directory to the system path to import main.py
sys.path.insert(0, os.path.abspath(".."))

import main

class TestCaesarCipher(unittest.TestCase):

    def test_shiftCharacter(self):
        self.assertEqual(main.shiftCharacter('a', main.LOWER_ALPHABETS), 'n')
        self.assertEqual(main.shiftCharacter('Z', main.UPPER_ALPHABETS), 'M')

    def test_rot13(self):
        self.assertEqual(main.rot13("Simple test.\n"), "Fvzcyr grfg.\n")

    @patch("builtins.open", new_callable=mock_open)
    def test_writeFile(self, mock_file):
        content = "Fvzcy rfgf.\n"
        filename = "test_output.txt"
        main.writeFile(filename, content)
        mock_file.assert_called_with(filename, 'w', encoding="UTF-8")
        mock_file().write.assert_called_once_with(content)

if __name__ == '__main__':
    unittest.main()
