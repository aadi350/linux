#!/usr/bin/bash

cd /home/aadi/linux && git pull origin main

# update config
rsync --update -raz --progress /home/aadi/linux/home/aadi/.config/qtile/ /home/aadi/.config/qtile
rsync --update -raz --progress /home/aadi/linux/home/aadi/.config/alacritty/ /home/aadi/.config/alacritty/
# rsync --update -raz --progress "/home/aadi/.config/Code - Insiders/User/settings.json" /home/aadi/linux/.config/Code/User/

# update .zshrc
rsync --update -raz --progress /home/aadi/linux/home/aadi/.zshrc  /home/aadi/

# update emacs
rsync --update -raz --progress  /home/aadi/linux/home/aadi/.doom.d/  /home/aadi/.doom.d/

sudo rsync --update -raz --progress  /home/aadi/linux/usr/bin/homepage /usr/bin/
sudo rsync --update -raz --progress  /home/aadi/linux/usr/local/bin/ /usr/local/bin/
