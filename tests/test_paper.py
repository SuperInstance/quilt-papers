import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import unittest

from quilt_papers.paper import canon_to_paper, canon_to_bibtex


class TestPaper(unittest.TestCase):

    def test_basic_paper(self):
        lore = "Sentence one. Sentence two.\n\nSecond paragraph here."
        paper = canon_to_paper("Test Title", lore)
        self.assertEqual(paper["title"], "Test Title")
        self.assertIn("Sentence one", paper["abstract"])
        self.assertIn("Second paragraph", paper["body"])
        self.assertEqual(paper["n_paragraphs"], 2)

    def test_default_authors(self):
        lore = "Test."
        paper = canon_to_paper("Title", lore)
        self.assertIn("Casey", paper["authors"][0])

    def test_custom_authors(self):
        lore = "Test."
        paper = canon_to_paper("Title", lore, authors=["Alice", "Bob"])
        self.assertEqual(paper["authors"], ["Alice", "Bob"])

    def test_bibtex(self):
        bib = canon_to_bibtex("My Paper")
        self.assertIn("@misc", bib)
        self.assertIn("My Paper", bib)
        self.assertIn("Casey", bib)


if __name__ == "__main__":
    unittest.main()
