# Setup git
import subprocess

def setup_git():
    # Setup git
    commands = ["git config --global user.name 'Calvin Loveland'",
                "git config --global user.email 'calvin@loveland.dev'"
                "git config --global pull.rebase false",
                "git config --global core.editor 'nvim'",
                ]
    for command in commands:
        if subprocess.call(command, shell=True) != 0:
            print("Error running command: " + command)

def main(sudo_password):
    """Run the program."""
    setup_git()
