import unittest
import gitRepos

class TestGitHubAPI(unittest.TestCase):

    def test_get_repositories_success(self):
        """Test that GitHub API retrieves real repositories for a known user."""
        user = "ryry91021"
        result = gitRepos.main(user)

        self.assertIsInstance(result, dict)
        self.assertGreater(len(result), 0)

    def test_get_commit_count_success(self):
        """Test commit count retrieval from an actual repository."""
        user = "ryry91021"
        result = gitRepos.main(user)

        first_repo = next(iter(result), None)
        self.assertIsNotNone(first_repo)
        self.assertGreaterEqual(result[first_repo], 0)

    def test_invalid_user(self):
        """Test that an invalid user returns an error."""
        with self.assertRaises(Exception) as context:
            gitRepos.main("thisuserdoesnotexist123456")

        self.assertIn("Failed to retrieve repositories", str(context.exception))

 
if __name__ == "__main__":
    unittest.main()