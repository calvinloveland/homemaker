import subprocess
import os

from .software import Software


class Fish(Software):
    tags = ["fish", "shell", "work"]

    @classmethod
    def pre_apt(cls):
        return [
            "sudo apt-add-repository ppa:fish-shell/release-3 -y",
            "sudo apt update",
        ]

    @classmethod
    def apt_packages(cls):
        return ["fish", "neofetch", "fonts-firacode"]

    @classmethod
    def post_apt(cls):
        neofetch_config = os.path.join(os.path.dirname(__file__), "neofetch_config")
        return [
            "chsh -s /usr/bin/fish",
            "mkdir -p ~/.config/neofetch",
            "mkdir -p ~/.config/fish",
            "cp " + neofetch_config + " ~/.config/neofetch/config.conf",
            "echo 'neofetch' >> ~/.config/fish/config.fish",
        ]

    @classmethod
    def check_if_installed(cls):
        """Check if fish is installed."""
        return subprocess.run("fish --version", shell=True).returncode == 0
