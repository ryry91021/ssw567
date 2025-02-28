import unittest
from unittest.mock import patch, MagicMock
import gitRepos

class TestGitHubAPI(unittest.TestCase):

    @patch("gitRepos.requests.get")
    def test_get_repositories_success(self, mock_get):
        """Mock GitHub API to retrieve repositories for a known user."""
        
        mock_response = MagicMock()
        mock_response.json.return_value = [
            {"name": "Repo1", "full_name": "user/Repo1"},
            {"name": "Repo2", "full_name": "user/Repo2"},
            {"name": "Repo3", "full_name": "user/Repo3"}
        ]
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        
        user = "ryry91021"
        result = gitRepos.main(user)

        self.assertIsInstance(result, dict)
        self.assertGreater(len(result), 0)
        self.assertIn("Repo1", result)
        self.assertIn("Repo2", result)
        self.assertIn("Repo3", result)

    @patch("gitRepos.requests.get")
    def test_get_commit_count_success(self, mock_get):
        """Mock commit count retrieval from a repository."""

        mock_repo_response = MagicMock()
        mock_repo_response.json.return_value = [
            {"name": "TestRepo", "full_name": "user/TestRepo"}
        ]
        mock_repo_response.status_code = 200

        mock_commit_response = MagicMock()
        mock_commit_response.json.return_value = [{"sha": "commit1"}, {"sha": "commit2"}]
        mock_commit_response.status_code = 200

        mock_get.side_effect = [mock_repo_response, mock_commit_response]

        user = "ryry91021"
        result = gitRepos.main(user)

        self.assertIn("TestRepo", result)
        self.assertEqual(result["TestRepo"], 2)

    @patch("gitRepos.requests.get")
    def test_invalid_user(self, mock_get):
        """Mock an invalid user request returning an error."""
        mock_response = MagicMock()
        mock_response.status_code = 404 
        mock_response.json.return_value = {"message": "Not Found"}
        mock_get.return_value = mock_response

        with self.assertRaises(Exception) as context:
            gitRepos.main("thisuserdoesnotexist123456")

        self.assertIn("Failed to retrieve repositories", str(context.exception))

if __name__ == "__main__":
    unittest.main()
