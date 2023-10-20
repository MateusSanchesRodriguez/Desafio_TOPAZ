import unittest
from main import get_user_data, get_user_repositories, create_report

class TestGithubAPI(unittest.TestCase):

    def test_get_user_data(self):
        username = "MateusSanchesRodriguez"
        user_data = get_user_data(username)
        self.assertEqual(user_data["login"], "MateusSanchesRodriguez")

    def test_get_user_repositories(self):
        username = "MateusSanchesRodriguez"
        repositories = get_user_repositories(username)
        self.assertGreaterEqual(len(repositories), 0)

    def test_create_report(self):
        username = "MateusSanchesRodriguez"
        report = create_report(username)
        self.assertTrue(report.startswith("Nome:"))
        self.assertTrue(report.endswith("- Todo_list_contatos\n"))

if __name__ == '__main__':
    unittest.main()
