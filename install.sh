echo -e "Installing Hash Cracker...\n"

sudo apt-get install python3 python3-dev python3-pip
python3 -m pip install -r requirements.txt
mkdir -p /usr/share/hashcracker/
cp hashcracker.py /usr/share/hashcracker/hashcracker.py
ln -s /usr/share/hashcracker/hashcracker.py /usr/bin/hashcracker

echo "Hash Cracker installed!"