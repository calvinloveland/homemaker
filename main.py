import just_installer
import subprocess

if __name__ == '__main__':
    # docker
    if not just_installer.is_installed('docker'):
        just_installer.just_install('docker')
    # vscode
    if not just_installer.is_installed('code'):
        just_installer.just_install('code')
    # neovim
    if not just_installer.is_installed('nvim'):
        just_installer.just_install('nvim')
    # fish
    if not just_installer.is_installed('fish'):
        just_installer.just_install('fish')
        # set fish as default shell
        subprocess.call(['chsh', '-s', '/usr/bin/fish'])