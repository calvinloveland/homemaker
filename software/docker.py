"""A file to install docker on a linux machine."""

import subprocess
import distro

def install_docker(current_distro, password):
    if current_distro == "Ubuntu":
        commands = [
            "sudo -S apt-get remove docker docker-engine docker.io containerd runc",
            "sudo -S apt-get update",
            "sudo -S apt-get install -y ca-certificates curl gnupg lsb-release",
            "sudo -S mkdir -p /etc/apt/keyrings",
            "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo -S gpg --dearmor -o /etc/apt/keyrings/docker.gpg",
            "echo deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable | sudo -S tee /etc/apt/sources.list.d/docker.list > /dev/null",
            "sudo -S apt-get update",
            "sudo -S apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin",
            "sudo -S usermod -aG docker $USER",
        ]
        for command in commands:
            subprocess.run("echo {} | {}".format(password, command), shell=True)
        return True
    else:
        print("current_distro not supported yet.")
        return False

def check_if_installed():
    """Check if docker is installed."""
    return subprocess.run("docker --version", shell=True).returncode == 0

def main(password):
    """Run the program."""
    if check_if_installed():
        print("Docker is already installed.")
    else:
        current_distro = distro.name()
        return install_docker(current_distro,password)

if __name__ == "__main__":
    input_password = input("Enter your password: ")
    main(input_password)