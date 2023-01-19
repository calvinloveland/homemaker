import subprocess
import os
import distro

from .software import Software


class Fish(Software):
    tags = ["fish", "shell", "work"]

    @classmethod
    def pre_pre_apt_packages(cls):
        return ["software-properties-common", "apt-transport-https", "ca-certificates", "curl"]

    @classmethod
    def pre_apt(cls):
        if distro.name() == "Ubuntu":
            return [
                "sudo apt-add-repository ppa:fish-shell/release-3 -y",
                "sudo apt update",
            ]
        if distro.name() == "Debian":
            version = distro.version()
            return [
                "echo 'deb http://download.opensuse.org/repositories/shells:/fish:/release:/3/Debian_{}/ /' | sudo tee /etc/apt/sources.list.d/shells:fish:release:3.list".format(version),
                "curl -fsSL https://download.opensuse.org/repositories/shells:fish:release:3/Debian_{}/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/shells_fish_release_3.gpg > /dev/null".format(version),]

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
