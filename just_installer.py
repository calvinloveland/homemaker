import subprocess
import distro


def get_distro():
    return distro.id()


def just_install(package_name):
    distro = get_distro()
    if distro == 'ubuntu':
        subprocess.call(['sudo', 'apt-get', 'install', package_name])
    elif distro == 'fedora':
        subprocess.call(['sudo', 'dnf', 'install', package_name])
    elif distro == 'arch':
        subprocess.call(['sudo', 'pacman', '-S', package_name])
    else:
        print("Can't figure out how to install for distro: {}".format(distro))

def is_installed(package_name):
    distro = get_distro()
    if distro == 'ubuntu':
        return subprocess.call(['dpkg', '-s', package_name]) == 0
    elif distro == 'fedora':
        return subprocess.call(['rpm', '-q', package_name]) == 0
    elif distro == 'arch':
        return subprocess.call(['pacman', '-Q', package_name]) == 0
    else:
        print("Can't figure out how to install for distro: {}".format(distro))
        return False
