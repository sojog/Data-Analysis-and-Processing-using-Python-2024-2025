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


def create_project(project_name="test_project"):
    CREATE_PROJECT_CMD = f"{python_command} -m django startproject {project_name}"
    subprocess.call(CREATE_PROJECT_CMD, shell=True)

def delete_project(project_name="test_project"):
    shutil.rmtree(project_name)


def create_application(app_name="test_app", project_name="test_project"):
    # Current working directory
    cwd = os.getcwd()
    print("Inainte de a schimba path-ul", cwd)
    ## imi schimba path-ul
    os.chdir( os.path.join(cwd, project_name))
    print("Dupa schimbarea path-ului", os.getcwd())

    CREATE_APP_CMD  = f"{python_command} manage.py startapp {app_name}"
    subprocess.call(CREATE_APP_CMD, shell=True)

def _add_app_to_installed_apps(app_name="test_app", project_name="test_project"):
    # Current working directory
    cwd = os.getcwd()
    print("Inainte de a schimba path-ul", cwd)
    ## imi schimba path-ul
    os.chdir( os.path.join(cwd, project_name))
    print("Dupa schimbarea path-ului", os.getcwd())

    cwd = os.getcwd()
    os.chdir( os.path.join(cwd, project_name))
    print("Dupa schimbarea path-ului", os.getcwd())

    with open("settings.py", "r") as freader:
        settings_content = freader.readlines()
        # print(settings_content)

    has_encounter_installed_apps = False
    for index, line in enumerate(settings_content):
        if "INSTALLED_APPS = [" in line:
            has_encounter_installed_apps = True
            print("has encounter")
        elif has_encounter_installed_apps and ("]" in line):
            # print("inserted")
            settings_content.insert(index, f"\t'{app_name}',\n")
            break

    print("\n".join(settings_content))
    
    with open("settings.py", "w") as fwriter:
        fwriter.writelines(settings_content)

def _create_templates_folder(app_name="test_app", project_name="test_project"):
    cwd = os.getcwd()
    os.chdir(os.path.join(cwd, project_name, app_name))
    TEMPLATES = "templates"
    os.makedirs(TEMPLATES, exist_ok=True)

def _create_app_url_file(app_name="test_app", project_name="test_project"):
    cwd = os.getcwd()
    os.chdir(os.path.join(cwd, project_name, app_name))
    URLS_FILE_NAME = "urls.py"
    URLS_CONTENT = """from django.urls import path\n\nurlpatterns = [\n\n]\n"""
    with open(URLS_FILE_NAME, "w") as fwriter:
        fwriter.write(URLS_CONTENT)

def _link_app_in_project_url_file(app_name="test_app", project_name="test_project"):
    cwd = os.getcwd()
    os.chdir(os.path.join(cwd, project_name, project_name))
    with open("urls.py", "r") as freader:
        urls_lines = freader.readlines()

    print(urls_lines)
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

    with open("urls.py", "w") as fwriter:
        fwriter.writelines(urls_lines)


def demo_enumerate():
    lista_mea = ["Maria", "Ion", "Gheorghe", "Vasile"]
    for index, element in enumerate(lista_mea):
        print(index, element)
        if element == "Gheorghe":
            lista_mea.insert(index, "Florina")
            break
    print(lista_mea)

if __name__ == "__main__":
    # print(os.getcwd())
    # _link_app_in_project_url_file()

    # create_project("ecommerce")
    # create_application("blog", "ecommerce")
    # _add_app_to_installed_apps("blog", "ecommerce")

    _create_app_url_file("blog", "ecommerce")

    # 
    # time.sleep(3)
    # create_application()
    # _add_app_to_installed_apps()

    # delete_project()