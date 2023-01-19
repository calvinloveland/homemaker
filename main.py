import multiprocessing
import software
import time
import importlib
import distro
import software
import getpass
import inspect
import subprocess

from pyfiglet import Figlet
from tqdm import tqdm

def run_command(command, failures):
    if subprocess.run(command, shell=True, stdout=subprocess.DEVNULL).check_returncode != 0:
        failures.append(command)

if __name__ == "__main__":

    f = Figlet(font="slant")
    print(f.renderText("Homemaker"))
    # print current distro
    print("Current distro: " + distro.name())
    # get all the modules in the software directory
    # and import them
    # then run the main function in each module
    # and store the results in a list

    pre_pre_apt_packages = []
    pre_apt_commands = []
    apt_packages = []
    post_apt_commands = []
    default_tags = ["work"]
    tags = default_tags

    for module in software.__all__:
        module = importlib.import_module("software." + module)
        software_classes = inspect.getmembers(module, inspect.isclass)
        for software_class in software_classes:
            software_class = software_class[1]
            if len(set(tags) & set(software_class.tags)) > 0:
                if software_class.check_if_installed():
                    print(software_class.__name__ + " is already installed")
                    continue
                pre_pre_apt_packages += software_class.pre_pre_apt_packages()
                pre_apt_commands += software_class.pre_apt()
                apt_packages += software_class.apt_packages()
                post_apt_commands += software_class.post_apt()

    pre_pre_apt_packages = list(set(pre_pre_apt_packages))
    apt_packages = list(set(apt_packages))

    print("Collected " + str(len(pre_pre_apt_packages)) + " pre_pre_apt_packages")
    print("Collected " + str(len(pre_apt_commands)) + " pre_apt_commands")
    print("Collected " + str(len(apt_packages)) + " apt_packages")
    print("Collected " + str(len(post_apt_commands)) + " post_apt_commands")


    failing_commands = []
    run_command("sudo apt-get update", failing_commands)
    pre_pre_apt_command = "sudo apt-get install -y " + " ".join(pre_pre_apt_packages)
    run_command(pre_pre_apt_command, failing_commands)

    for pre_apt_command in tqdm(
        pre_apt_commands, desc="Pre apt", unit="command", ncols=88
    ):
        run_command(pre_apt_command, failing_commands)

    run_command("sudo apt-get update", failing_commands)
    apt_command = "sudo apt-get install -y " + " ".join(apt_packages)
    run_command(apt_command, failing_commands)

    for post_apt_command in tqdm(
        post_apt_commands, desc="Post apt", unit="command", ncols=88
    ):
        run_command(post_apt_command, failing_commands)
    
    print("======Failing commands!========")
    for command in failing_commands:
        print(command)

    print("Done")
