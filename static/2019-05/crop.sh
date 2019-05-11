#!/usr/bin/env bash

for file in *.png
do
    # 872 273
    # 3062 1787
    magick "$file" -crop 2190x1514+872+273 "cropped_$file"
done
