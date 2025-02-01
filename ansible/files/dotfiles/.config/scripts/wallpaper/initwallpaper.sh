#!/bin/bash

setimg () {
  nitrogen $1 --set-zoom-fill
}

if [ -e "${HOME}/.cache/wal/colors" ]; then
    wal -e -R --cols16

    echo "Cached colors exist. Using existing colors."
else
    DIR=$HOME/.config/wallpapers
    PICS=($(ls ${DIR}))

    RANDOMPICS=${PICS[ $RANDOM % ${#PICS[@]} ]}

    setimg ${DIR}/${RANDOMPICS}
    wal -e -i ${DIR}/${RANDOMPICS} --cols16 -b "#131521" --backend colorz

    echo "Successfully set a new wallpaper and generated colors from it."
fi
