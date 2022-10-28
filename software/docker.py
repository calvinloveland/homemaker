"""A file to install docker on a linux machine."""

import subprocess
import distro

def install_docker(distro):
    """Install docker on a linux machine."""
    # sudo apt-get remove docker docker-engine docker.io containerd runc
    # sudo apt-get update
    # sudo apt-get install \
    # ca-certificates \
    # curl \
    # gnupg \
    # lsb-release
    # sudo mkdir -p /etc/apt/keyrings
    # curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    # echo \
    #     "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
    #     $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    # sudo apt-get update
    # sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
    # sudo usermod -aG docker $USER
    if distro == "ubuntu":
        commands = [
            "sudo apt-get remove docker docker-engine docker.io containerd runc",
            "sudo apt-get update",
            "sudo apt-get install ca-certificates curl gnupg lsb-release",
            "sudo mkdir -p /etc/apt/keyrings",
            "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg",
            "echo deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null",
            "sudo apt-get update",
            "sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin",
            "sudo usermod -aG docker $USER",
        ]
        for command in commands:
            subprocess.run(command, shell=True)
        exit(0)
    else:
        print("Distro not supported yet.")
        exit(1)

def main():
    """Run the program."""
    distro = distro.linux_distribution()[0]
    install_docker(distro)
