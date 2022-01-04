#!/usr/bin/bash


DMBROWSER="vivaldi-stable"

declare -a options=(
    "arxiv - https://arxiv.org/search/?searchtype=all&source=header&query="
    "google - https://www.google.com/search?q="
    "scholar - https://scholar.google.com/scholar?q="
)

while [ -z "$engine" ]; do
    enginelist=$(printf '%s\n' "${options[@]}" | dmenu -i -l 20 -p 'Choose search engine:') || exit
    engineurl=$(echo "$enginelist" | awk '{print $NF}')
    engine=$(echo "$enginelist" | awk '{print $1}')
done

while [ -z "$query" ]; do
    query=$(dmenu -i -l 20 -p "Searching:") || exit
done

vivaldi-stable "$engineurl""$query"
