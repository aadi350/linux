#!/usr/bin/bash




echo "Enter commit message"
read MSG

# update config
rsync --update -raz --progress /home/aadi/.config/qtile/ /home/aadi/linux/home/aadi/.config/qtile/
rsync --update -raz --progress /home/aadi/.config/alacritty/ /home/aadi/linux/home/aadi/.config/alacritty/
rsync --update -raz --progress "/home/aadi/.config/Code - Insiders/User/settings.json" /home/aadi/linux/home/aadi/.config/Code/User/

# update .zshrc
rsync --update -raz --progress /home/aadi/.zshrc /home/aadi/linux/home/aadi/

# update emacs
rsync --update -raz --progress /home/aadi/.doom.d/ /home/aadi/linux/home/aadi/doom.d/


cd /home/aadi/linux && git add . && git commit -m "$MSG" && git push origin main
