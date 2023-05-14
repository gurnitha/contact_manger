# BUILDING A CONTACT MANAGER
Building A Contact Manager like a Platform using Django


## 01. SETUP


#### 01.1 Create django project and apps

        modified:   .gitignore
        modified:   README.md
        new file:   apps/contact/__init__.py
        new file:   apps/contact/admin.py
        new file:   apps/contact/apps.py
        new file:   apps/contact/migrations/__init__.py
        new file:   apps/contact/models.py
        new file:   apps/contact/tests.py
        new file:   apps/contact/urls.py
        new file:   apps/contact/views.py
        new file:   apps/home/__init__.py
        new file:   apps/home/admin.py
        new file:   apps/home/apps.py
        new file:   apps/home/migrations/__init__.py
        new file:   apps/home/models.py
        new file:   apps/home/tests.py
        new file:   apps/home/urls.py
        new file:   apps/home/views.py
        new file:   apps/task/__init__.py
        new file:   apps/task/admin.py
        new file:   apps/task/apps.py
        new file:   apps/task/migrations/__init__.py
        new file:   apps/task/models.py
        new file:   apps/task/tests.py
        new file:   apps/task/urls.py
        new file:   apps/task/views.py
        new file:   apps/team/__init__.py
        new file:   apps/team/admin.py
        new file:   apps/team/apps.py
        new file:   apps/team/migrations/__init__.py
        new file:   apps/team/models.py
        new file:   apps/team/tests.py
        new file:   apps/team/urls.py
        new file:   apps/team/views.py
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/static/assets/img/165.png
        ...
        new file:   config/static/assets/vendor_assets/js/wickedpicker.min.js
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py
        new file:   requirements.txt
        new file:   templates/apps/contact/add_contact.html
        new file:   templates/apps/contact/contact_profile.html
        new file:   templates/apps/contact/contacts.html
        new file:   templates/apps/contact/contacts_list.html
        new file:   templates/apps/home/home.html
        new file:   templates/apps/task/tasks_list.html
        new file:   templates/apps/team/teams_add.html
        new file:   templates/apps/team/teams_home.html
        new file:   templates/apps/team/teams_local.html
        new file:   templates/apps/team/teams_table.html
        new file:   templates/base.html
        new file:   templates/partials/aside.html
        new file:   templates/partials/footer.html
        new file:   templates/partials/header.html


#### 01.2 Modifikasi files naming

        renamed:    apps/contact/__init__.py -> app/contact/__init__.py
        renamed:    apps/contact/admin.py -> app/contact/admin.py
        renamed:    apps/contact/apps.py -> app/contact/apps.py
        ...
        renamed:    templates/apps/team/teams_local.html -> templates/app/team/teams_local.html
        renamed:    templates/apps/team/teams_table.html -> templates/app/team/teams_table.html
