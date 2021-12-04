#!/usr/bin/zsh

cd /home/aadi/linux && git pull origin main

# update config
rsync --update -raz --progress /home/aadi/linux/.config/qtile/ /home/aadi/.config/
rsync --update -raz --progress /home/aadi/linux/.config/alacritty/ /home/aadi/.config/alacritty/
# rsync --update -raz --progress "/home/aadi/.config/Code - Insiders/User/settings.json" /home/aadi/linux/.config/Code/User/

# update .zshrc
rsync --update -raz --progress /home/aadi/linux/.zshrc  /home/aadi/

# update emacs
rsync --update -raz --progress  /home/aadi/linux/.doom.d/  /home/aadi/.doom.d/
