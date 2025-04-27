import unittest

class TestPaginaHtml(unittest.TestCase):
    def test_hola_mundo_en_html(self):
        with open("index.html", "r", encoding="utf-8") as f:
            contenido = f.read()
        self.assertIn("¡Hola Mundo!", contenido)

if __name__ == "__main__":
    unittest.main()
