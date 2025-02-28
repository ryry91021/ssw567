import unittest
import gitRepos

import unittest
from unittest.mock import patch, MagicMock
import gitRepos

class TestGitHubAPI(unittest.TestCase):
    @patch("gitRepos.requests.get")
    def test_get_repositories_success(self, mock_get):
        """Test get_repositories"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"name": "Repo1", "full_name": "user/Repo1"},
            {"name": "Repo2", "full_name": "user/Repo2"}
        ]
        mock_get.return_value = mock_response

        headers = {"Authorization": "token FAKE_TOKEN"}
        repos = gitRepos.get_repositories("user", headers)

        self.assertEqual(len(repos), 2)
        self.assertEqual(repos[0]["name"], "Repo1")
        self.assertEqual(repos[1]["full_name"], "user/Repo2")

    @patch("gitRepos.requests.get")
    def test_get_repositories_failure(self, mock_get):
        """Repo fetch failure"""
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.json.return_value = {}
        mock_get.return_value = mock_response

        headers = {"Authorization": "token FAKE_TOKEN"}
        
        with self.assertRaises(Exception) as context:
            gitRepos.get_repositories("invalid_user", headers)
        
        self.assertIn("Failed to retrieve repositories", str(context.exception))

    @patch("gitRepos.requests.get")
    def test_get_commitCount_success(self, mock_get):
        """Test count commits"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{"sha": "abc123"}, {"sha": "def456"}]
        mock_get.return_value = mock_response

        headers = {"Authorization": "token FAKE_TOKEN"}
        commit_count = gitRepos.get_commitCount("user/Repo1", headers)

        self.assertEqual(commit_count, 2)

    @patch("gitRepos.requests.get")
    def test_get_commitCount_empty_repo(self, mock_get):
        """Test empty repo (409 error)"""
        mock_response = MagicMock()
        mock_response.status_code = 409
        mock_get.return_value = mock_response

        headers = {"Authorization": "token FAKE_TOKEN"}
        commit_count = gitRepos.get_commitCount("user/EmptyRepo", headers)

        self.assertEqual(commit_count, 0)

    @patch("gitRepos.requests.get")
    def test_get_commitCount_failure(self, mock_get):
        """Test API failure on commits"""
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        headers = {"Authorization": "token FAKE_TOKEN"}

        with self.assertRaises(Exception) as context:
            gitRepos.get_commitCount("user/RepoError", headers)

        self.assertIn("Failed to retrieve commits", str(context.exception))

    @patch("requests.get")
    def test_correct_api_call(self, mock_get):
        """Test API url request"""
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{"name": "Repo1"}]

        headers = {"Authorization": "token FAKE_TOKEN"}
        gitRepos.get_repositories("ryry91021", headers)

        mock_get.assert_called_once_with("https://api.github.com/users/ryry91021/repos", headers=headers)




    @patch("gitRepos.get_repositories")
    @patch("gitRepos.get_commitCount")
    def test_main(self, mock_get_commitCount, mock_get_repositories):
        """Test main function that returns repo listing and commit counters"""
        mock_get_repositories.return_value = [
            {"name": "Repo1", "full_name": "user/Repo1"},
            {"name": "Repo2", "full_name": "user/Repo2"}
        ]
        mock_get_commitCount.side_effect = [5, 3]

        result = gitRepos.main("user")

        self.assertEqual(result["Repo1"], 5)
        self.assertEqual(result["Repo2"], 3)

if __name__ == "__main__":
    unittest.main()

