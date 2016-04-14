from fabric.api import local


def run_manage(command):
    local('/home/vagrant/.virtualenvs/le-code-test/bin/python /vagrant/testsite/manage.py %s' % command)


def web():
    run_manage('runserver 0.0.0.0:8888')


def migrate():
    run_manage('migrate')


def make_migrations():
    run_manage('makemigrations')


def test():
    run_manage('test stream.tests')


def reset():
    run_manage('flush')
    fixtures = ['admin_account', 'streams', 'items']
    for fixture in fixtures:
        run_manage('loaddata %s.json' % fixture)


def requirements():
    local('/home/vagrant/.virtualenvs/le-code-test/bin/pip install -r requirements.txt ')
