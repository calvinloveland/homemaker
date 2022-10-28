# make code directory in home directory
mkdir -p ~/code
# change to code directory
cd ~/code
# download the code
git clone https://github.com/calvinloveland/homemaker.git
# install python3
sudo apt-get install python3
# install pip3
sudo apt-get install python3-pip
# install virtualenv
sudo pip3 install virtualenv
# make virtual environment
virtualenv -p python3 venv
# activate virtual environment
source venv/bin/activate
# install requirements
pip3 install -r homemaker/requirements.txt
# run the program
python3 homemaker/main.py