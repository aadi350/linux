#!/usr/bin/zsh

mkdir ~/.install
git clone https://aur.archlinux.org/zoom.git ~/.install
makepkg -si ~/.install/zoom

wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh ~/.install
sh ~/.install/install.sh

pacman -S git base-devel
pacman -S qtile
pacman -S dmenu
pamac build flameshot
pamac install slack-desktop --noconfirm
pamac install inotify-tools --noconfirm

sudo cp -r ~/linux/usr/local/bin/* /usr/local/bin/
