#!/usr/bin/python3
""" Modul for test the Review class"""
from models.base_model import BaseModel
from models.review import Review
import unittest


class TestReviewClass(unittest.TestCase):
    """Unittest for Review class"""
    def test_inheritance(self):
        ReviewTest = Review()
        self.assertIsInstance(ReviewTest, BaseModel)

    def test_place_idAttribute(self):
        ReviewTest = Review()
        self.assertEqual(ReviewTest.place_id, "")
        self.assertIsInstance(ReviewTest.place_id, str)

    def test_user_idAttribute(self):
        ReviewTest = Review()
        self.assertEqual(ReviewTest.user_id, "")
        self.assertIsInstance(ReviewTest.user_id, str)

    def test_textAttribute(self):
        ReviewTest = Review()
        self.assertEqual(ReviewTest.text, "")
        self.assertIsInstance(ReviewTest.text, str)


if __name__ == '__main__':
    unittest.main()
