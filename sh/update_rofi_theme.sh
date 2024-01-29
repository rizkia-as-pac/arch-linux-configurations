#!/bin/bash

# Define the path to your .rasi file and JSON file
rasi_file="$HOME/.config/rofi/theme.rasi"
json_file="$HOME/.config/colors-kitty.json"

foreground=$(jq -r '.foreground' "$json_file")
background=$(jq -r '.background' "$json_file")
cursor=$(jq -r '.cursor' "$json_file")
color0=$(jq -r '.color0' "$json_file")
color1=$(jq -r '.color1' "$json_file")
color2=$(jq -r '.color2' "$json_file")
color3=$(jq -r '.color3' "$json_file")
color4=$(jq -r '.color4' "$json_file")
color5=$(jq -r '.color5' "$json_file")
color6=$(jq -r '.color6' "$json_file")
color7=$(jq -r '.color7' "$json_file")
color8=$(jq -r '.color8' "$json_file")
color15=$(jq -r '.color15' "$json_file")


# Use sed to replace the specified line with the new content
sed -i "2s/.*/    foreground:                  $foreground;/" "$rasi_file"
sed -i "3s/.*/    background:                  $background;/" "$rasi_file"
sed -i "4s/.*/    red:                         $color6;/" "$rasi_file"
sed -i "5s/.*/    selected-bg:                 $color7;/" "$rasi_file"
sed -i "6s/.*/    selected-fg:                 $background;/" "$rasi_file"