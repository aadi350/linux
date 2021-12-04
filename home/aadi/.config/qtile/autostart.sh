#!/bin/sh
nitrogen --restore &
xset r rate 300 90 &
cd /home/aadi/.config/homepage && python -m http.server &
