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

if __name__ == "__main__":
    # print(os.getcwd())


    # create_project()
    # time.sleep(3)
    # create_application()
    _add_app_to_installed_apps()

    # delete_project()
