import requests



token = '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'

def get_user_data(username):
    headers = {'Authorization': f'token {token}'}
    response = requests.get(f"https://api.github.com/users/{username}", headers=headers)
    user_data = response.json()
    return user_data

def get_user_repositories(username):
    headers = {'Authorization': f'token {token}'}
    response = requests.get(f"https://api.github.com/users/{username}/repos", headers=headers)
    repositories = response.json()
    return repositories

def create_report(username,get_user_data_func=get_user_data, get_user_repositories_func=get_user_repositories):
    user_data = get_user_data_func(username)
    name = user_data["name"]
    profile = user_data["html_url"]
    public_repos = user_data["public_repos"]
    followers = user_data["followers"]
    following = user_data["following"]

    repositories = get_user_repositories_func(username)
    repo_list = [repo["name"] for repo in repositories]

    report = f"Nome: {name}\n"
    report += f"Perfil: {profile}\n"
    report += f"Número de repositórios públicos: {public_repos}\n"
    report += f"Número de seguidores: {followers}\n"
    report += f"Número de usuários seguidos: {following}\n"
    report += "Lista de Repositórios:\n"
    for repo in repo_list:
        report += f"- {repo}\n"

    with open(f"{username}.txt", "w") as file:
        file.write(report)
    
    return report

create_report("MateusSanchesRodriguez")