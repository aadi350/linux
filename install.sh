#!/usr/bin/zsh

mkdir ~/.install
git clone https://aur.archlinux.org/zoom.git ~/.install
makepkg -si ~/.install/zoom

mkdir ~/.install/zoom
wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh ~/.install/zoom
sh ~/.install/zoom/install.sh

pacman -S git base-devel
pacman -S qtile
pacman -S dmenu
pamac build flameshot
pamac install slack-desktop --noconfirm
pamac install inotify-tools --noconfirm
pamac install nitrogen --noconfirm
pacman install emacs --noconfirm

mkdir ~/.install/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-py38_4.10.3-Linux-x86_64.sh ~/.install/miniconda3
sh ~/.install/anaconda3/Miniconda3-latest-Linux-x86_64.sh

git clone --depth 1 https://github.com/hlissner/doom-emacs ~/.emacs.d
~/.emacs.d/bin/doom install

echo "~/.emacs.d/bin:$PATH"

sudo cp -r ./.doom.d/* ~/.doom.d/
sudo cp -r ./home/aadi/* ~/
sudo cp -r ./usr/ /usr/
sudo cp -r ~/linux/usr/local/bin/* /usr/local/bin/

sudo doom sync
