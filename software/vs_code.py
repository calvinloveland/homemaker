import distro
import subprocess

from .software import Software

class VSCode(Software):
    tags = ["vscode", "code", "text editor", "work"]

    @classmethod
    def pre_pre_apt_packages(cls):
        return ["software-properties-common", "apt-transport-https", "wget"]

    @classmethod
    def pre_apt(cls):
        return [
            "wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -",
            "sudo add-apt-repository \"deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main\"",
        ]
    
    @classmethod
    def apt_packages(cls):
        return ["code"]
    
    @classmethod
    def check_if_installed(cls):
        """Check if vscode is installed."""
        return subprocess.run("code --version", shell=True).returncode == 0


