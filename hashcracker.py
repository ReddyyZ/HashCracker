import argparse, textwrap, hashlib, threading, os, sys, time
import hashid, bcrypt

__clear__   = lambda : os.system("cls" if os.name == "nt" else "clear")
__version__ = "v1.0.0"

hashs_ = {
    "md5": lambda text : hashlib.md5(text.encode()).hexdigest(),
    "sha1": lambda text : hashlib.sha1(text.encode()).hexdigest(),
    "sha224": lambda text : hashlib.sha224(text.encode()).hexdigest(),
    "sha256": lambda text : hashlib.sha256(text.encode()).hexdigest(),
    "sha384": lambda text : hashlib.sha384(text.encode()).hexdigest(),
    "sha512": lambda text : hashlib.sha512(text.encode()).hexdigest(),
    "bcrypt": lambda text, salt : bcrypt.hashpw(text.encode(), salt.encode()),
}

salts_ = {
    "bcrypt": lambda _hash : _hash[0:29]
}

def arguments():
    parser = argparse.ArgumentParser(
        prog="HashCracker",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
            Script for hash cracking
            Github: https://github.com/ReddyyZ/HashCracker
            '''))

    parser.add_argument('-w','--wordlist',metavar="PATH",help="Path to wordlist (Default: rockyou.txt)",default="wordlists/rockyou.txt",type=str)
    parser.add_argument('-m','--mode',help="Hash type (None for identify)",default=None,type=str)
    parser.add_argument('-t','--threads',metavar=16,help="Threads count (Default: 16)",default=16,type=int)
    parser.add_argument('hash',help="File with hashs to crack (Separated by lines) or hash",type=str)

    args = parser.parse_args()

    return (args.wordlist, args.threads, args.mode, args.hash)

def identify_hash(_hash):
    identifier = hashid.HashID()
    result     = identifier.identifyHash(_hash)

    hash_type  = (max(result).name).split('(')[0]

    return hash_type

def brute(_hash,passwd,hash_type, t_num, salt=None):
    print(f"[Thread: {t_num}] Testing: {_hash}:{passwd}")

    if not salt:
        result = hashs_[hash_type](passwd).decode()
    else:
        result = hashs_[hash_type](passwd,salt).decode()

    if _hash == result:
        print(f"Hash founded: {_hash}:{passwd}")
        os._exit(1)

def main():
    wordlist, threads, mode, _hash = arguments()
    __clear__()
    fd = open(wordlist, "r")
    if not mode:
        mode = identify_hash(_hash)

    try:
        salt = salts_[mode](_hash)
    except:
        salt = None

    print(textwrap.dedent(f"""
        888    888                888      .d8888b.                        888                     
        888    888                888     d88P  Y88b                       888                     
        888    888                888     888    888                       888                     
        8888888888 8888b. .d8888b 88888b. 888       888d888 8888b.  .d8888b888  888 .d88b. 888d888 
        888    888    "88b88K     888 "88b888       888P"      "88bd88P"   888 .88Pd8P  Y8b888P"   
        888    888.d888888"Y8888b.888  888888    888888    .d888888888     888888K 88888888888     
        888    888888  888     X88888  888Y88b  d88P888    888  888Y88b.   888 "88bY8b.    888     
        888    888"Y888888 88888P'888  888 "Y8888P" 888    "Y888888 "Y8888P888  888 "Y8888 888

        Github: https://github.com/ReddyyZ/HashCracker
        By: ReddyyZ
        Version: {__version__}

        [+]Hash: {_hash}
        [+]Threads: {threads}
        [+]Hash Type: {mode}
        [+]Salt: {salt}
        [+]Wordlist: {wordlist}

        [*]Starting...
    """))

    try:
        time.sleep(5)
    except KeyboardInterrupt:
        pass

    while True:
        try:
            thread_list = [None] * threads

            for i in range(threads):
                passwd = fd.readline().replace("\n","")
                if not passwd: break

                thread_list[i] = threading.Thread(target=brute,args=(_hash, passwd, mode, i, salt))
                thread_list[i].start()

            for i in thread_list:
                try:
                    i.join()
                except:
                    pass
        except KeyboardInterrupt:
            for i in thread_list:
                try:
                    i._stop()
                except:
                    pass
            break

if __name__ == "__main__":
    main()