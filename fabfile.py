# PYTHON 2 code
from fabric.api import *

FREEZE_FOLDER = 'gh-pages'
FREEZE_BRANCH = 'gh-pages'


def commit_source(message):
    local("git add -A")
    if not message:
        message = raw_input("Enter a source commit message:  ")
    # Test for uncommited changes (avoid error or empty commit)
    local("git diff-index --quiet HEAD || git commit -m \"%s\" && git push origin master" % message)


def freeze():
    with prefix("source venv/bin/activate"):
        local("python freeze.py")


def commit_website(message):
    with lcd(FREEZE_FOLDER):
        local("git add -A")
        if not message:
            message = raw_input("Enter a webpage commit message:  ")
        # Test for uncommited changes (avoid error or empty commit)
        local("git diff-index --quiet HEAD || git commit -m \"%s\" && git push origin %s" % (message, FREEZE_BRANCH))

def deploy():
    message = raw_input("Enter a commit message:  ")
    commit_source(message)
    freeze()
    commit_website(message)