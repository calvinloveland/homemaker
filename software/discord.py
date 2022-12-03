import subprocess

def install_discord_on_ubuntu(password):
    """Install Discord on Ubuntu Linux distributions using apt."""
    commands = [
        "sudo -S apt-get update",
        "sudo -S apt-get install discord",
    ]
    for command in commands:
        subprocess.run("echo {} | {}".format(password, command), shell=True)
    return True

def main(password):
    """Run the program."""
    return install_discord_on_ubuntu(password)