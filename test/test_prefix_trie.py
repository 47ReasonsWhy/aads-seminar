import os
import unittest

from trie.prefix import PrefixTrie


class TestPrefixTrie(unittest.TestCase):

	def setUp(self):
		"""Set up a new PrefixTrie for each test."""
		self.trie = PrefixTrie()

	def test_insert_and_search(self):
		"""Test inserting and searching for strings."""
		self.trie.insert("hello")
		self.trie.insert("world")
		self.trie.insert("help")

		# Search for exact strings
		self.assertIsNotNone(self.trie.search("hello"))
		self.assertIsNotNone(self.trie.search("world"))
		self.assertIsNotNone(self.trie.search("help"))

		# Search for prefixes (should not exist unless explicitly inserted)
		self.assertIsNone(self.trie.search("hel"))
		self.assertIsNone(self.trie.search("worl"))

		# Search for a string not in the trie
		self.assertIsNone(self.trie.search("notinthetrie"))

	def test_remove(self):
		"""Test removing strings from the prefix trie."""
		self.trie.insert("hello")
		self.trie.insert("help")

		# Verify strings exist before removal
		self.assertIsNotNone(self.trie.search("hello"))
		self.assertIsNotNone(self.trie.search("help"))

		# Remove one string and verify the other still exists
		self.trie.remove("hello")
		self.assertIsNone(self.trie.search("hello"))
		self.assertIsNotNone(self.trie.search("help"))

		# Remove the other string
		self.trie.remove("help")
		self.assertIsNone(self.trie.search("help"))

		# Attempt to remove a string not in the trie
		self.assertFalse(self.trie.remove("nonexistent"))

	def test_empty_string(self):
		"""Test handling of empty strings."""
		self.trie.insert("")
		self.assertIsNotNone(self.trie.search(""))
		self.trie.remove("")
		self.assertIsNone(self.trie.search(""))

	def test_common_prefixes(self):
		"""Test inserting strings with common prefixes."""
		self.trie.insert("prefix")
		self.trie.insert("prefecture")
		self.trie.insert("pref")

		# Verify all strings exist
		self.assertIsNotNone(self.trie.search("prefix"))
		self.assertIsNotNone(self.trie.search("prefecture"))
		self.assertIsNotNone(self.trie.search("pref"))

		# Verify removing one does not affect others
		self.trie.remove("prefix")
		self.assertIsNone(self.trie.search("prefix"))
		self.assertIsNotNone(self.trie.search("prefecture"))
		self.assertIsNotNone(self.trie.search("pref"))

	def test_is_leaf(self):
		"""Test the is_leaf method of PrefixTrieNode."""
		root = self.trie.root
		self.assertTrue(root.is_leaf())  # Root is initially a leaf

		# Add a child and check again
		child = root.insert("a")
		self.assertFalse(root.is_leaf())
		self.assertTrue(child.is_leaf())

	def test_visualize(self):
		"""Test that visualize runs without errors."""
		self.trie.insert("test")
		self.trie.insert("testing")
		self.trie.insert("tester")

		try:
			self.trie.visualize(file_name="test_prefix_trie", directory_name=".", view=False)
		except Exception as e:
			self.fail(f"Visualization failed with exception: {e}")
		finally:
			os.remove("test_prefix_trie")
			os.remove("test_prefix_trie.png")


if __name__ == "__main__":
	unittest.main()
