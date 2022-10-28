import distro

def install_vscode(distro):
    """Install vscode on a linux machine."""
    if distro == "ubuntu":
        commands = [
            "sudo apt install software-properties-common apt-transport-https wget",
            "wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -",
            "sudo add-apt-repository \"deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main\"",
            "sudo apt update",
            "sudo apt install code",
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
    install_vscode(distro)