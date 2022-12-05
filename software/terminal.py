import subprocess
import os


def install_fish(sudo_password):
    """Install fish."""
    commands = [
        "sudo -S apt-add-repository ppa:fish-shell/release-3 -y",
        "sudo -S apt update",
        "sudo -S apt install fish -y",
        "chsh -s /usr/bin/fish",
    ]
    for command in commands:
        subprocess.run("echo {} | {}".format(sudo_password, command), shell=True)

def install_byobu(sudo_password):
    """Install byobu."""
    commands = [
        "sudo -S apt install tmux byobu -y",
    ]
    for command in commands:
        subprocess.run("echo {} | {}".format(sudo_password, command), shell=True)

def install_and_config_neofetch(sudo_password):
    """Install neofetch."""
    neofetch_config = os.path.join(os.path.dirname(__file__), "neofetch_config")
    commands = [
        "sudo -S apt install neofetch -y",
        "sudo -S cp {} ~/.config/neofetch/config.conf".format(neofetch_config),
        "echo 'neofetch' >> ~/.config/fish/config.fish",
    ]

def install_firacode(sudo_password):
    """Install firacode."""
    commands = [
        "sudo -S apt install fonts-firacode -y",
    ]
    for command in commands:
        subprocess.run("echo {} | {}".format(sudo_password, command), shell=True)

def check_if_installed():
    """Check if fish is installed."""
    return subprocess.run("fish --version", shell=True).returncode == 0

def main(sudo_password):
    """Run the program."""
    if check_if_installed():
        print("Fish is already installed.")
    else:
        install_fish(sudo_password)
        install_byobu(sudo_password)
        install_and_config_neofetch(sudo_password)

if __name__ == "__main__":
    input_password = input("Enter your password: ")
    main(input_password)