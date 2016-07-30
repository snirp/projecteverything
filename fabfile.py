# PYTHON 2 code
from fabric.api import *

FREEZE_FOLDER = 'gh-pages'
FREEZE_BRANCH = 'gh-pages'


def commit_source():
    source_message = raw_input("Enter a source commit message:  ")
    local("git add -A && git commit -m \"%s\"" % source_message)
    local("git push origin master")


def freeze():
    with prefix("source venv/bin/activate"):
        local("python freeze.py")


def commit_static():
    with lcd(freeze_folder):
        static_message = raw_input("Enter a webpage commit message:  ")
        local("git add -A && git commit -m \"%s\"" % static_message)
        local("git push origin %s" % freeze_branch)


def deploy():
    commit_source()
    freeze()
    commit_static()