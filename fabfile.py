from fabric.api import local

def test_local():
    local('python manage.py test --settings=django_base.settings.base')

def deploy_prod():
    local('python manage.py collectstatic --noinput')

def deploy_local():
    local('python manage.py runserver --settings=django_base.settings.base')

