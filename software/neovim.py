import distro
import subprocess

def install_neovim(current_distro, sudo_password):
    """Install neovim on a linux machine."""
    if current_distro == "Ubuntu":
        commands = [
            "echo " + sudo_password + " | sudo -S apt-get update",
            "echo " + sudo_password + " | sudo -S apt-get install neovim",
        ]
        for command in commands:
            subprocess.run(command, shell=True)
        return True
    else:
        print("current_distro not supported yet.")
        return False


def main(sudo_password):
    """Run the program."""
    current_distro = distro.name()
    return install_neovim(current_distro, sudo_password)
