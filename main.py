import multiprocessing
import software
import time
import importlib
import distro
import software
import getpass

from pyfiglet import Figlet

if __name__ == '__main__':

    f = Figlet(font='slant')
    print(f.renderText('Homemaker'))
    # print current distro
    print("Current distro: " + distro.name())
    sudo_password = getpass.getpass(prompt='Enter sudo password: ')
    # get all the modules in the software directory
    # and import them
    # then run the main function in each module
    # and store the results in a list

    for module in software.__all__:
        module = importlib.import_module("software." + module)
        module.main() 
    