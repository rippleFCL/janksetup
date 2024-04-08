#!/bin/bash

dir="$HOME/.config/rofi/launchers/type-1"
theme='style-3'

setimg () {
  nitrogen $1 --set-zoom-fill
}

wallpapers=$HOME/.config/wallpapers
image="$(ls $wallpapers | rofi -dmenu -i -p "  Select wallpaper: " -theme ${dir}/${theme}.rasi -dpi 1)"
if [[ ! $image == "" ]]; then
    setimg ${wallpapers}/${image}
    wal -i ${wallpapers}/${image} --cols16 -e
    $HOME/.config/polybar/launch.sh
    echo "Successfully set a new wallpaper and generated colors from it."
fi
