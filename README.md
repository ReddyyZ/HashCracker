<h1 align="center">HashCracker</h1>

<p align="center">A simple Hash Cracking tool developed in Python 3</p>

> For educational purposes

## Libraries

- hashid >= 3.1.4
- bcrypt >= 3.2.0

[hashID](https://github.com/psypanda/hashID) used for hash identification

[bcrypt](https://pypi.org/project/bcrypt/) used for bcrypt hashs creation

## OS Support

- Windows
- Linux
- Mac? - Not tested

## Installation

- Clone the repo and cd into directory
```bash
git clone https://github.com/ReddyyZ/HashCracker.git && cd HashCracker
```

- Set permissions
```bash
chmod +x install.sh
```

- Execute installation script
```bash
sudo ./install.sh
```

- Happy Hacking!
```bash
hashcracker -h
```

## How to use

OPTIONS | EXPLANATION
------- | -----------
-w,  --wordlist | Wordlist path
-m, --mode | Specify the hash type
-t, --threads | Threads count
---

- Try to identify the hash
```bash
hashcracker -w rockyou.txt 5f4dcc3b5aa765d61d8327deb882cf99
```

- Specify the hash to crack
```bash
hashcracker -w rockyou.txt -m md5 5f4dcc3b5aa765d61d8327deb882cf99
```

---

<h2 align="center">&lt;/&gt; by <a href="https://github.com/ReddyyZ">ReddyyZ</a></h2>