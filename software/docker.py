"""A file to install docker on a linux machine."""

import subprocess
import distro
from .software import Software

class Docker(Software):
    tags = ["work"]
    @classmethod
    def pre_pre_apt_packages(cls):
        # "sudo -S apt-get install -y ca-certificates curl gnupg lsb-release",
        return ["ca-certificates", "curl", "gnupg", "lsb-release"]
    
    @classmethod
    def pre_apt(cls):
        return [
            "sudo -S mkdir -p /etc/apt/keyrings",
            "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo -S gpg --dearmor -o /etc/apt/keyrings/docker.gpg",
            "echo deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable | sudo -S tee /etc/apt/sources.list.d/docker.list > /dev/null",]

    @classmethod
    def apt_packages(cls):
        return ["docker-ce", "docker-ce-cli", "containerd.io", "docker-compose-plugin"]
    
    @classmethod
    def post_apt(cls):
        return ["sudo -S usermod -aG docker $USER",]

    @classmethod
    def check_if_installed(cls):
        """Check if Docker is installed."""
        return subprocess.run("docker --version", shell=True).returncode == 0