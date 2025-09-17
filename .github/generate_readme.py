import os
import requests

ORG_NAME = "repositorio-code"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

def get_repos():
    """Busca todos os repositórios da organização usando a API do GitHub."""
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
    }
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/orgs/{ORG_NAME}/repos?per_page=100&page={page}"
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Erro na API do GitHub: {response.status_code} - {response.text}")
        
        data = response.json()
        if not data:
            break
        
        repos.extend(data)
        page += 1
    return repos

def format_readme(repos):
    """Formata os dados dos repositórios em um texto para o README."""
    sorted_repos = sorted(repos, key=lambda r: r['name'], reverse=True)
    
    content = "# Acervo de Projetos de Engenharia de Computação\n\n"
    content += "Este README é gerado automaticamente a partir dos repositórios da organização.\n\n"
    content += "## Padrão de Nomenclatura\n\n"
    content += "Os repositórios seguem o padrão: `SEMESTRE_MATERIA_NOME-PROJETO`\n\n"
    content += "Exemplo: `2025.1_DEC0021_Monitoramento-Zabbix-ESP32`\n\n"
    
    projects_by_semester = {}
    excluded_repos = []

    for repo in sorted_repos:
        name = repo['name']
        description = repo['description'] or "Nenhuma descrição fornecida."
        
        # Verifica se o repositório segue o padrão SEMESTRE_MATERIA_NOME-PROJETO
        if "_" in name and name.count('_') >= 2:
            parts = name.split('_', 2)
            if len(parts) == 3:
                semester = parts[0]
                course_code = parts[1]
                project_name = parts[2].replace('-', ' ').title()
                
                # Validação adicional: semestre deve ter formato YYYY.N
                if '.' in semester and len(semester.split('.')) == 2:
                    year, period = semester.split('.')
                    if year.isdigit() and period.isdigit():
                        if semester not in projects_by_semester:
                            projects_by_semester[semester] = {}
                        if course_code not in projects_by_semester[semester]:
                            projects_by_semester[semester][course_code] = []
                        
                        projects_by_semester[semester][course_code].append({
                            "name": project_name,
                            "url": repo['html_url'],
                            "description": description,
                            "repo_name": name
                        })
                        continue
        
        # Repositório não segue o padrão
        excluded_repos.append(name)

    # Gera seções por semestre
    for semester, courses in sorted(projects_by_semester.items(), reverse=True):
        content += f"## Projetos do Semestre {semester}\n\n"
        for course_code, projects in sorted(courses.items()):
            content += f"### {course_code}\n\n"
            for project in projects:
                content += f"- **[{project['name']}]({project['url']})** (`{project['repo_name']}`)\n"
                content += f"  {project['description']}\n\n"
            content += "\n"
    
    # Adiciona seção com repositórios que não seguem o padrão (opcional)
    if excluded_repos:
        content += "## Outros Repositórios\n\n"
        content += "Os seguintes repositórios não seguem o padrão de nomenclatura estabelecido:\n\n"
        for repo_name in sorted(excluded_repos):
            content += f"- `{repo_name}`\n"
        content += "\n"
    
    content += f"\n---\n\n*Última atualização: {__import__('datetime').datetime.now().strftime('%d/%m/%Y às %H:%M:%S')} UTC*\n"
    
    return content

def main():
    """Função principal para gerar e salvar o README."""
    try:
        print("Buscando repositórios da organização...")
        repos = get_repos()
        print(f"Encontrados {len(repos)} repositórios na organização '{ORG_NAME}'")
        
        print("Gerando conteúdo do README...")
        new_readme_content = format_readme(repos)
        
        print("Salvando arquivo PROJECTS_HUB.md...")
        with open("PROJECTS_HUB.md", "w", encoding="utf-8") as f:
            f.write(new_readme_content)
        
        print("PROJECTS_HUB.md atualizado com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        exit(1)

if __name__ == "__main__":
    try:
        import requests
    except ImportError:
        print("A biblioteca 'requests' não está instalada. Execute: pip install requests")
        exit(1)
        
    main()
