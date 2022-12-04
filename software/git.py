# Setup git
import subprocess

def setup_git():
    # Setup git
    commands = ["git config --global user.name 'Calvin Loveland'",
                "git config --global user.email 'calvin@loveland.dev'"]
    for command in commands:
        subprocess.call(command, shell=True)

def main():
