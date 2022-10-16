#!/usr/bin/env bash
for file in *.jpg
do
    convert "$file" -auto-orient -thumbnail 1920x1080 -quality 75 -unsharp 0x.5 "${file%.jpg}.thumb.jpg"
done
