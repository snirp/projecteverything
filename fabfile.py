# PYTHON 2 code
from fabric.api import *

FREEZE_FOLDER = 'gh-pages'
FREEZE_BRANCH = 'gh-pages'


def commit_source():
    local("git add -A")
    # Test for uncommited changes (avoid error or empty commit)
    if local("git diff-index --quiet HEAD"):
        message = raw_input("Enter a source commit message:  ")
        local("git commit -m \"%s\"" % message)
        local("git push origin master")



def freeze():
    with prefix("source venv/bin/activate"):
        local("python freeze.py")


def commit_static():
    with lcd(FREEZE_FOLDER):
        local("git add -A")
        # Test for uncommited changes (avoid error or empty commit)
        if local("git diff-index --quiet HEAD"):
            message = raw_input("Enter a webpage commit message:  ")
            local("git commit -m \"%s\"" % message)
            local("git push origin %s" % FREEZE_BRANCH)


def deploy():
    commit_source()
    freeze()
    commit_static()