import os
import subprocess
import time
import shutil

# verificăm dacă suntem pe Windows sau Linux
if os.name == 'nt':
    python_command = 'python'
else:
    python_command = 'python3'
print(f"Folosim comanda: {python_command}")

## Set comenzi 

## 1. Adaugare applicatie/aplicatii
## 2. Adaugare in settings

def _add_app_to_installed_apps(project_name , app_name):
    file_path = os.path.join(project_name, 'settings.py')
    with open(file_path, 'r') as file:
        lines = file.readlines()
    # Caută locul unde e secțiunea INSTALLED_APPS
    # Adaugăm o nouă aplicație la finalul listei INSTALLED_APPS
    installed_apps_found = False
    for i, line in enumerate(lines):
        if 'INSTALLED_APPS = [' in line:
            installed_apps_found = True
        if installed_apps_found and line.strip() == ']':
            # Adaugă noua aplicație imediat după INSTALLED_APPS și înainte de ]
            lines.insert(i , f"    '{app_name}',\n")
            break

    # Rescrie fișierul
    with open(file_path, 'w') as file:
        file.writelines(lines)

## 3. Creare folder templates
def _create_templates_folder_inside_app(app_name):
    if not os.path.exists(os.path.join(app_name, 'templates')):
        os.makedirs(os.path.join(app_name, 'templates'))
    else:
        print(f"Folderul templates există deja în {app_name}")

# create_templates_folder_inside_app(PROJECT_APP)
def _create_urls_file_inside_app(app_name):
    text_to_write = f"""from django.urls import path\n\nurlpatterns = [\npath('', views.index, name='index'),\n]"""
    if not os.path.exists(os.path.join(app_name, 'urls.py')):
        with open(os.path.join(app_name, 'urls.py'), 'w') as file:
            file.write(text_to_write)
    else:
        print(f"Fisierul urls.py există deja în {app_name}")

## 4. Creare fisier urls.pt pt fiecare aplicatie
def _link_urls_to_project_urls(project_name, app_name):
    with open(os.path.join(project_name, 'urls.py'), 'r') as file:
        lines = file.readlines()
    included_app_found = False
    for i, line in enumerate(lines):
        # from django.urls import path, include
        if 'from django.urls import path' in line and 'include' not in line:
            # trebuie sa adaugat ,include la finalul liniei
            lines[i] = line.replace('path', 'path, include')
            included_app_found = True
        if included_app_found and line.strip() == ']':
            lines.insert(i, f"    path('{app_name}/', include('{app_name}.urls')),\n")
            break
    with open(os.path.join(project_name, 'urls.py'), 'w') as file:
        file.writelines(lines)



def create_application(project_name, app_name):
    _add_app_to_installed_apps(project_name, app_name)
    _create_templates_folder_inside_app(app_name)
    _create_urls_file_inside_app(app_name)
    _link_urls_to_project_urls(project_name, app_name)



def create_project_and_apps(PROJECT_NAME = "testproject" , *applications)   :

    start_project = f"{python_command} -m django startproject {PROJECT_NAME} ."
    #start_application = f"{python_command} manage.py startapp  {PROJECT_APP}"

    command_list = [start_project]

    for app in applications:
        start_application = f"{python_command} manage.py startapp  {app}"
        command_list.append(start_application)

    for command in command_list:
        print(command)
        subprocess.run(command, shell=True)
        time.sleep(1)

    for app in applications:
        create_application(PROJECT_NAME, app)



# o functie de stergere a proiectului si a aplicatiei si a tuturor fisierelor sale
def delete_project_and_app(project_name, app_name):
    # continua in caz de eroare cu toate fisierelor
    # os.rmdir(project_name)
    shutil.rmtree(project_name, ignore_errors=False)
    shutil.rmtree(app_name, ignore_errors=False)
    # os.rmdir(app_name)
    os.remove('manage.py')
# delete_project_and_app(PROJECT_NAME, PROJECT_APP)


# create_urls_file_inside_app(PROJECT_APP)
# link_urls_to_project_urls(PROJECT_NAME, PROJECT_APP)




## 4. Creare perechi view+template

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


def create_view_and_template(app_name):
    view_name = input("Introdu numele view-ului: ") or "testing"
    template_name = input("Introdu numele template-ului: ") or "testing"
    create_view(view_name, template_name, app_name)
    create_template(template_name, app_name)


# create_view_and_template(PROJECT_APP)

options = {
    "1": "create project and apps",
    "2": "create application",
    "3": "create view and template"
}
# define main function
def main():
    # choose option 
    while True:
        option = input(f"Introdu optiunea:\n {options} ")
        if option == "1":
            option = input("Introdu numele proiectului: ")
            PROJECT_NAME = option
            applications = []
            while True:
                option = input("Introdu numele aplicatiei: ")
                if option == "":
                    break
                applications.append(option)
            create_project_and_apps(PROJECT_NAME, *applications)
        elif option == "2":
            PROJECT_NAME = input("Introdu numele proiectului: ")
            option = input("Introdu numele aplicatiei: ")
            create_application(PROJECT_NAME, option)
        elif option == "3":
            PROJECT_APP = input("Introdu numele aplicatiei: ")
            create_view_and_template(PROJECT_APP)
        elif option == "x":
            PROJECT_NAME = input("Introdu numele proiectului: ")
            PROJECT_APP = input("Introdu numele aplcatiei: ")
            delete_project_and_app(PROJECT_NAME, PROJECT_APP)

if __name__ == "__main__":
    main()