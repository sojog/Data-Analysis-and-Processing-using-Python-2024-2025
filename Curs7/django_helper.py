"""## Set comenzi pentru automatizare de Django
## 1. Adaugare applicatie/aplicatii
## 2. Adaugare in settings
## 3. Creare folder templates
## 4. Creare fisier urls.pt pt fiecare aplicatie
## 5. Creare perechi view+template  
"""

import os
import subprocess
import time
import shutil

# Verifica sistemul de operare este Windows
if os.name == "nt":
    python_command = "python"
# In caz contrar (Mac/Linux)
else:
    python_command = "python3"


def create_project(project_name="test_project", *applications, should_create_default_superuser=False):
    CREATE_PROJECT_CMD = f"{python_command} -m django startproject {project_name}"
    subprocess.call(CREATE_PROJECT_CMD, shell=True)
    time.sleep(3)

    for app_name in applications:
        create_application(app_name=app_name, project_name=project_name)

    if should_create_default_superuser:
        make_migrations(project_name)
        create_superuser(project_name)

def delete_project(project_name="test_project"):
    shutil.rmtree(project_name)


def project_path(project_name="test_project"):
    return os.path.join(os.getcwd(), project_name)

def inner_project_path(project_name="test_project"):
    return os.path.join(os.getcwd(), project_name, project_name)

def app_path(app_name="test_app", project_name="test_project"):
    return os.path.join(os.getcwd(), project_name, app_name)

def create_application(app_name="test_app", project_name="test_project"):
    # Schimbăm directorul de lucru la proiect înainte de a crea aplicația
    cwd = os.getcwd()
    proj_path = project_path(project_name)
    os.chdir(proj_path)
    
    CREATE_APP_CMD = f"{python_command} manage.py startapp {app_name}"
    subprocess.call(CREATE_APP_CMD, shell=True)
    time.sleep(0.5)
    
    # Apelăm setup dar rămânem în directorul proiectului
    setup_application(app_name, project_name)
    
    # Revertim directorul de lucru
    os.chdir(cwd)

def make_migrations(project_name="test_project"):
     # Schimbăm directorul de lucru la proiect înainte de a crea aplicația
    cwd = os.getcwd()
    proj_path = project_path(project_name)
    os.chdir(proj_path)

    MAKE_MIGRATIONS_CMD = f"{python_command} manage.py makemigrations"
    MIGRATE_CMD = f"{python_command} manage.py migrate"
    subprocess.call(MAKE_MIGRATIONS_CMD, shell=True)
    time.sleep(0.5)
    subprocess.call(MIGRATE_CMD, shell=True)
    time.sleep(0.5)

    # Revertim directorul de lucru
    os.chdir(cwd)

def create_superuser(project_name="test_project", username="admin", email="email@email.com"):
       # Schimbăm directorul de lucru la proiect înainte de a crea aplicația
    cwd = os.getcwd()
    proj_path = project_path(project_name)
    os.chdir(proj_path)

    CREATE_SUPERUSER_CMD = f"{python_command} manage.py createsuperuser"
    CREATE_SUPERUSER_CMD += f" --username {username} --email {email}"
    subprocess.call(CREATE_SUPERUSER_CMD, shell=True)
    time.sleep(0.5)

    # Revertim directorul de lucru
    os.chdir(cwd)

def setup_application(app_name="test_app", project_name="test_project"):
    # Funcțiile de setup sunt apelate din directorul proiectului (din create_application)
    _add_app_to_installed_apps(app_name, project_name)
    _create_templates_folder(app_name, project_name)
    _create_app_url_file(app_name, project_name)
    _link_app_in_project_url_file(app_name, project_name)

def _add_app_to_installed_apps(app_name="test_app", project_name="test_project"):
    # Calea către settings.py este în folderul intern al proiectului
    settings_path = os.path.join(project_name, "settings.py")
    
    with open(settings_path, "r") as freader:
        settings_content = freader.readlines()

    has_encounter_installed_apps = False
    for index, line in enumerate(settings_content):
        if "INSTALLED_APPS = [" in line:
            has_encounter_installed_apps = True
        elif has_encounter_installed_apps and ("]" in line):
            # print("inserted")
            settings_content.insert(index, f"\t'{app_name}',\n")
            break
    
    with open(settings_path, "w") as fwriter:
        fwriter.writelines(settings_content)

def _create_templates_folder(app_name="test_app", project_name="test_project"):
    # Creăm folderul templates în directorul aplicației
    app_templates_path = os.path.join(app_name, "templates", app_name)
    os.makedirs(app_templates_path, exist_ok=True)

def _create_app_url_file(app_name="test_app", project_name="test_project"):
    # Creăm urls.py în directorul aplicației
    app_urls_path = os.path.join(app_name, "urls.py")
    URLS_CONTENT = """from django.urls import path\n\nurlpatterns = [\n\n]\n"""
    
    with open(app_urls_path, "w") as fwriter:
        fwriter.write(URLS_CONTENT)

def _link_app_in_project_url_file(app_name="test_app", project_name="test_project"):
    # Calea către urls.py din folderul intern al proiectului
    project_urls_path = os.path.join(project_name, "urls.py")
    
    with open(project_urls_path, "r") as freader:
        urls_lines = freader.readlines()

    has_encounter_urlpatterns = False
    new_line = f"\tpath('{app_name}/', include('{app_name}.urls')),\n"
    if new_line in urls_lines:
        return

    for index, line in enumerate(urls_lines):
        if 'from django.urls import path' in line and 'include' not in line:
            urls_lines[index] = line.replace("path", "path, include")
        if "urlpatterns = [" in line:
            has_encounter_urlpatterns = True
        elif has_encounter_urlpatterns and "]" in line:
            urls_lines.insert(index, new_line)
            break

    with open(project_urls_path, "w") as fwriter:
        fwriter.writelines(urls_lines)


def create_view(view_name, template_name, app_name):
    view_text = f"""def {view_name}_view(request):\n\tcontext = {"{}"}\n\treturn render(request, '{template_name}.html', context)\n"""
    with open(os.path.join(app_name, 'views.py'), 'r') as filereader:
        existing_views = filereader.read()
    
    with open(os.path.join(app_name, 'views.py'), 'w') as file:
        file.write(existing_views + "\n" + view_text)

def create_template(template_name, app_name):
    template_emmet = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{template_name}</title>
</head>
<body>
    <h1>{template_name}</h1>
</body>
</html>"""
    with open(os.path.join(app_name, 'templates', f'{template_name}.html'), 'w') as file:
        file.write(template_emmet)

def create_view_and_template(view_name, template_name, app_name, project_name):
    # Schimbăm directorul de lucru la proiect înainte de a crea aplicația
    cwd = os.getcwd()
    proj_path = project_path(project_name)
    os.chdir(proj_path)

    # view_name = input("Introdu numele view-ului: ") or "testing"
    # template_name = input("Introdu numele template-ului: ") or "testing"
    create_view(view_name, template_name, app_name)
    create_template(template_name, app_name)

    os.chdir(cwd)

def main():
    # choose option
    PROJECT_NAME = input("Introdu numele proiectului: ") 
    # check if folder exists with name in current 
    should_create_new_project = not os.path.exists(PROJECT_NAME)

    while True:
        applications = []
        view_templates_per_application = []
        while True:
            APP_NAME = input("Introdu numele aplicatiei (blank daca nu mai vrei sa adaugi): ")
            if APP_NAME == "":
                break
            applications.append(APP_NAME)
            while True:
                view_name = input(f"Introdu numele view-ului pt {APP_NAME} (blank daca nu mai vrei sa adaugi): ")
                if view_name == "":
                    break
                template_name = input(f"Introdu numele template-ului pt view-ul {view_name}: ")
                view_templates_per_application.append((view_name,template_name, APP_NAME))

        if should_create_new_project:
            create_project(PROJECT_NAME, *applications)
        elif applications:
            for app in applications:
                if not os.path.exists(os.path.join(os.getcwd(), PROJECT_NAME, app)):
                    create_application(app, PROJECT_NAME)

        for view, template, app in view_templates_per_application:
            create_view_and_template(view, template, app, PROJECT_NAME)
        print("Executie facuta cu succes \n")
        PROJECT_NAME = input(f"Alege un nou proiect? (blank pentru a ramane {PROJECT_NAME})") or PROJECT_NAME

if __name__ == "__main__":
    main()

    

