import os
import sys
import time
import socket
os.system('clear')
Wl  = '\33[0m'
R  = '\33[1;31m'
G  = '\033[1;32m'
O  = '\33[1;33m'
B  = '\33[1;34m'
P  = '\33[1;35m'
C  = '\33[1;36m'
GR = '\33[1;37m'
W="\033[0;37m"
msg=input(R+f"[-]{G} do you update Termux y/n :")
if msg=="y":
    print(W)
    os.system('pkg update -y')
    os.system('pkg upgrade -y')
    os.system('pkg install python -y')
    os.system('pkg install python2 -y')
    os.system('pkg install python3 -y')
    os.system('pkg install ruby -y')
    os.system('pkg install git -y')
    os.system('pkg install php -y')
    os.system('pkg install java -y')
    os.system('pkg install google -y')
    os.system('pkg install bash -y')
    os.system('pkg install perl -y')
    os.system('pkg install nmap -y')
    os.system('pkg install clang -y')
    os.system('pkg install macchanger -y')
    os.system('pkg install nano -y')
    os.system('pkg install cowsay -y')
    os.system('pkg install curl -y')
    os.system('pkg install tar -y')
    os.system('pkg install zip -y')
    os.system('pkg install unzip -y')
    os.system('pkg install tor -y')
    os.system('pkg install sudo -y')
    os.system('pkg install wget -y')
    os.system('pkg install wcalc -y')
    os.system('pkg install openssl -y')
    os.system('pkg install bmon -y')
else:
    print(R+"[!] ERROR ")

def iso():
    try:
        os.system("clear")
        print(f"""
{O}+{P}————————————————————————————————{O}+
{P}|{R}[*]{G} NAME: ISSAM ISO       {P}      |
{P}|{R}[*]{G} GITHUB: issamiso      {P}      |
{P}|{R}[*]{G} KALI LIUNX IN TERMUX  {P}      |
{O}+{P}————————————————————————————————{O}+   	""")
        iso=socket.gethostname()
        ss=socket.gethostbyname(iso)
        print(R+"\33[1;31m[-]\33[1;35m welcome \33[1;33m{}".format(iso))
        print(G+"[0] black arch        [+{}root{}]".format(R,G))
        print("[1] ubuntu            [+{}root{}]".format(R,G))
        print("[2] debian            [+{}root{}]".format(R,G))          
        print("[3] kali              [+{}root{}]".format(R,G))
        print("[4] kali nathunter    [+{}root{}]".format(R,G))
        print("[5] parrot securit    [+{}root{}]".format(R,G))
        print("[6] backbox           [+{}root{}]".format(R,G))
        print("[7] fedora            [+{}root{}]".format(R,G))
        print("[8] centos            [+{}root{}]".format(R,G))
        print("[9] opensuseleap      [+{}root{}]".format(R,G))
        un=input(R+"[+]{} {} namber: ".format(W,iso))
        if un == "0":
            os.system("pacman-key --init && pacman-key --populate archlinuxarm && pacman -Sy --noconfirm curl && curl -O https://blackarch.org/strap.sh && chmod +x strap.sh && ./strap.sh")
        if un =="1":
            os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Ubuntu/ubuntu.sh && bash ubuntu.sh")
        if un =="2":
            os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Debian/debian.sh && bash debian.sh")
        if un =="3":
            os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh && bash kali.sh")
        if un =="4":
            os.system("clear")
            os.system("termux-setup-storage")
            os.system("pkg install wget")
            os.system("wget -O install-nethunter-termux https://offs.ec/2MceZWr")
            os.system("chmod +x install-nethunter-termux")
            os.system("./install-nethunter-termux")
        if un =="5":
            os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Parrot/parrot.sh && bash parrot.sh")
        if un =="6":
            os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/BackBox/backbox.sh && bash backbox.sh")
        if un =="7":
            os.system("pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Fedora/fedora.sh && bash fedora.sh")
        if un =="8":
            os.system("pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/CentOS/centos.sh && bash centos.sh")
        if un =="9":
            os.system("pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/openSUSE/Leap/opensuse-leap.sh && bash opensuse-leap.sh")
        else:
            time.sleep(1)
            print(R+"[!] ERROR")
    except:
        print(R+"[!] ERROR")
iso()
