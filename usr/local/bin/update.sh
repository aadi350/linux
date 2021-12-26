#!/usr/bin/bash




echo "Enter commit message"
read MSG

# update config
rsync --update -raz --progress /home/aadi/.config/qtile/ /home/aadi/linux/home/aadi/.config/qtile/
rsync --update -raz --progress /home/aadi/.config/alacritty/ /home/aadi/linux/home/aadi/.config/alacritty/
# rsync --update -raz --progress "/home/aadi/.config/Code - Insiders/User/settings.json" /home/aadi/linux/.config/Code/User/

# update .zshrc
rsync --update -raz --progress /home/aadi/.zshrc /home/aadi/linux/home/aadi/

# update emacs
rsync --update -raz --progress /home/aadi/.doom.d/ /home/aadi/linux/home/aadi/.doom.d/

# update PATH files
sudo rsync --update -raz --progress /usr/bin/homepage /home/aadi/linux/usr/bin/
sudo rsync --update -raz --progress /usr/local/bin/update.sh /home/aadi/linux/usr/local/bin/update.sh
sudo rsync --update -raz --progress /usr/local/bin/pull-update.sh /home/aadi/linux/usr/local/bin/pull-update.sh
sudo rsync --update -raz --progress /usr/local/bin/search.sh /home/aadi/linux/usr/local/bin/search.sh

cd /home/aadi/linux && git add . && git commit -m "$MSG" && git push origin main
