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


def create_project(project_name="test_project", *applications):
    CREATE_PROJECT_CMD = f"{python_command} -m django startproject {project_name}"
    subprocess.call(CREATE_PROJECT_CMD, shell=True)
    time.sleep(1)

    for app_name in applications:
        create_application(app_name=app_name, project_name=project_name)

def delete_project(project_name="test_project"):
    shutil.rmtree(project_name)


def project_path(project_name="test_project"):
    return os.path.join(os.getcwd(), project_name)

def inner_project_path(project_name="test_project"):
    return os.path.join(os.getcwd(), project_name, project_name)

def app_path(app_name="test_app", project_name="test_project"):
    return os.path.join(os.getcwd(), project_name, app_name)


def change_cwd(path):
    def change_back_cwd(function):
        def inner_function(*args, **kwargs):
            cwd = os.getcwd()
            print(kwargs)
            if kwargs:
                result = function(*args, **kwargs)
            elif args:
                result = function(app_name=args[0],project_name= args[1])
            os.chdir(cwd)
            return result
        return inner_function
    return change_back_cwd


@change_cwd(project_path(project_name="test_project"))
def create_application(app_name="test_app", project_name="test_project"):

    os.chdir(project_path(project_name))
    
    CREATE_APP_CMD  = f"{python_command} {project_name}/manage.py startapp {app_name}"
    subprocess.call(CREATE_APP_CMD, shell=True)
    time.sleep(0.5)
    setup_application(app_name, project_name)


def setup_application(app_name="test_app", project_name="test_project"):
    _add_app_to_installed_apps(app_name, project_name)
    _create_templates_folder(app_name, project_name)
    _create_app_url_file(app_name, project_name)
    _link_app_in_project_url_file(app_name, project_name)

def _add_app_to_installed_apps(app_name="test_app", project_name="test_project"):

    with open(f"{inner_project_path(project_name)}/settings.py", "r") as freader:
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
    
    with open(f"{inner_project_path(project_name)}/settings.py", "w") as fwriter:
        fwriter.writelines(settings_content)

def _create_templates_folder(app_name="test_app", project_name="test_project"):
    TEMPLATES = f"{app_path(app_name, project_name)}/templates"
    os.makedirs(TEMPLATES, exist_ok=True)

def _create_app_url_file(app_name="test_app", project_name="test_project"):
    URLS_FILE_NAME = f"{app_path(app_name, project_name)}/urls.py"
    URLS_CONTENT = """from django.urls import path\n\nurlpatterns = [\n\n]\n"""
    with open(URLS_FILE_NAME, "w") as fwriter:
        fwriter.write(URLS_CONTENT)

def _link_app_in_project_url_file(app_name="test_app", project_name="test_project"):
    with open(f"{inner_project_path(project_name)}/urls.py", "r") as freader:
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

    with open(f"{inner_project_path(project_name)}/urls.py", "w") as fwriter:
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

    create_project("proiectulmeu", "app1", "app2")
    # create_application("app3", "proiectulmeu")
    # time.sleep(3)
    # create_application()
    # _add_app_to_installed_apps()

    # delete_project()
