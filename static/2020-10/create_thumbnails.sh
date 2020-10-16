#!/usr/bin/env bash
for file in *.jpg
do
    convert "$file" -auto-orient -thumbnail 800x600 -unsharp 0x.5 "${file%.jpg}.thumb.jpg"
done
