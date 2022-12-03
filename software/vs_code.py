import distro
import subprocess

def install_vscode(current_distro, password):
    """Install vscode on a linux machine."""
    if current_distro == "Ubuntu":
        commands = [
            "sudo -S apt install software-properties-common apt-transport-https wget",
            "wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo -S apt-key add -",
            "sudo -S add-apt-repository \"deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main\"",
            "sudo -S apt update",
            "sudo -S apt install code",
        ]
        for command in commands:
            subprocess.run("echo {} | {}".format(password, command), shell=True)
        return True
    else:
        print("Distro not supported yet.")
        return False

def main(password):
    """Run the program."""
    current_distro = distro.name()
    return install_vscode(current_distro, password)
