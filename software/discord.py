import subprocess

def install_discord_on_ubuntu(password):
    """Install Discord on Ubuntu Linux distributions."""
    commands = [
        "sudo -S apt-get update",
        "sudo -S apt-get install libc++1 libc++abi1 libssl1.0.0 libssl-dev",
        "wget -O discord.deb https://discordapp.com/api/download?platform=linux&format=deb",
        "sudo -S dpkg -i discord.deb",
    ]
    for command in commands:
        subprocess.run("echo {} | {}".format(password, command), shell=True)
    return True

def check_if_installed():
    """Check if Discord is installed."""
    return subprocess.run("dpkg -s discord", shell=True).returncode == 0

def main(password):
    """Run the program."""
    if check_if_installed():
        print("Discord is already installed.")
    else:
        return install_discord_on_ubuntu(password)

if __name__ == "__main__":
    input_password = input("Enter your password: ")
    main(input_password)