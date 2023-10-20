import unittest
from unittest.mock import patch, Mock
from main import get_user_data, get_user_repositories, create_report

class TestRelatorioGithub(unittest.TestCase):
    
    def setUp(self):
        self.username = 'MateusSanchesRodriguez'
    
    def test_get_user_data(self):
        expected_result = {'name': 'Mateus Sanches', 'html_url': 'https://github.com/MateusSanchesRodriguez', 'public_repos': 28, 'followers': 0, 'following': 0}
        mock_response = Mock()
        mock_response.json.return_value = expected_result
        with patch('requests.get', return_value=mock_response):
            result = get_user_data(self.username)
        self.assertEqual(result, expected_result)
    
    def test_get_user_repositories(self):
        # Define o resultado esperado da chamada à API
        expected_result = [{'name': 'Agenda_EBAC'},{'name': 'aprendendo_pull_request'},{'name': 'base_exercicio_css_in_js'},{'name': 'boostratp-avancado'},{'name': 'Bot-EP7'},{'name': 'Calculadora-Basica-JS'},{'name': 'Calculadora_aritmetica'},{'name': 'curso_ebac_frontend'},{'name': 'ebac_exercicio_rtl'},{'name': 'ebac_sports_redux'},{'name': 'efood'},{'name': 'Gerador-de-Senha'},{'name': 'Gerador_de_senha_API'},{'name': 'IMC_React'},{'name': 'Jogo-da-Velha'},{'name': 'landpage_evento'},{'name': 'landpage_V-F.'},{'name': 'Meu_Site_Python'},{'name': 'MS_store'},{'name': 'Portfolio'},{'name': 'Portfolio-main'},{'name': 'Sagex3-Syntax-Highlight-and-Auto-Complete'},{'name': 'Site_Ms_info'},{'name': 'Site_para_gi'},{'name': 'Site_python'},{'name': 'Space_lol'},{'name': 'Todo_List'},{'name': 'Todo_list_contatos'}]
        mock_response = Mock()
        mock_response.json.return_value = expected_result
        with patch('requests.get', return_value=mock_response):
            result = get_user_repositories(self.username)
        self.assertEqual(result, expected_result)
    
    def test_create_report(self):
        expected_result = "Nome: Mateus Sanches\nPerfil: https://github.com/MateusSanchesRodriguez\nNúmero de repositórios públicos: 28\nNúmero de seguidores: 0\nNúmero de usuários seguidos: 0\nLista de Repositórios:\n- Agenda_EBAC\n- aprendendo_pull_request\n- base_exercicio_css_in_js\n- boostratp-avancado\n- Bot-EP7\n- Calculadora-Basica-JS\n- Calculadora_aritmetica\n- curso_ebac_frontend\n- ebac_exercicio_rtl\n- ebac_sports_redux\n- efood\n- Gerador-de-Senha\n- Gerador_de_senha_API\n- IMC_React\n- Jogo-da-Velha\n- landpage_evento\n- landpage_V-F.\n- Meu_Site_Python\n- MS_store\n- Portfolio\n- Portfolio-main\n- Sagex3-Syntax-Highlight-and-Auto-Complete\n- Site_Ms_info\n- Site_para_gi\n- Site_python\n- Space_lol\n- Todo_List\n- Todo_list_contatos\n"
        mock_get_user_data = Mock(return_value={'name': 'Mateus Sanches', 'html_url': 'https://github.com/MateusSanchesRodriguez', 'public_repos': 28, 'followers': 0, 'following': 0})
        mock_get_user_repositories = Mock(return_value=[{'name': 'Agenda_EBAC'},{'name': 'aprendendo_pull_request'},{'name': 'base_exercicio_css_in_js'},{'name': 'boostratp-avancado'},{'name': 'Bot-EP7'},{'name': 'Calculadora-Basica-JS'},{'name': 'Calculadora_aritmetica'},{'name': 'curso_ebac_frontend'},{'name': 'ebac_exercicio_rtl'},{'name': 'ebac_sports_redux'},{'name': 'efood'},{'name': 'Gerador-de-Senha'},{'name': 'Gerador_de_senha_API'},{'name': 'IMC_React'},{'name': 'Jogo-da-Velha'},{'name': 'landpage_evento'},{'name': 'landpage_V-F.'},{'name': 'Meu_Site_Python'},{'name': 'MS_store'},{'name': 'Portfolio'},{'name': 'Portfolio-main'},{'name': 'Sagex3-Syntax-Highlight-and-Auto-Complete'},{'name': 'Site_Ms_info'},{'name': 'Site_para_gi'},{'name': 'Site_python'},{'name': 'Space_lol'},{'name': 'Todo_List'},{'name': 'Todo_list_contatos'}])
        with patch('main.get_user_data', return_value=mock_get_user_data):
            with patch('main.get_user_repositories', return_value=mock_get_user_repositories):
                result = create_report(self.username)

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()