#!/bin/sh
nitrogen --restore &
xinput --set-prop 10 "libinput Natural Scrolling Enabled" 1 &
xset r rate 300 90 &
cd /home/aadi/.config/homepage && python -m http.server &
