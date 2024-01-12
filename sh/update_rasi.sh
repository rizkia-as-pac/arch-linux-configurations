#!/bin/bash

# Define the path to your .rasi file and JSON file
rasi_file="$HOME/.config/rofi/theme.rasi"
json_file="$HOME/.config/color_scheme.json"


c_0=$(jq -r '.c_0' "$json_file")
c_1=$(jq -r '.c_1' "$json_file")
c_2=$(jq -r '.c_2' "$json_file")
c_3=$(jq -r '.c_3' "$json_file")
c_4=$(jq -r '.c_4' "$json_file")
c_5=$(jq -r '.c_5' "$json_file")
c_6=$(jq -r '.c_6' "$json_file")
c_7=$(jq -r '.c_7' "$json_file")
c_8=$(jq -r '.c_8' "$json_file")

# Specify the line number you want to change
line_number=5

# Specify the new content
new_content="This is the new content for line $line_number"

# Use sed to replace the specified line with the new content
sed -i "2s/.*/    foreground:                  $c_2;/" "$rasi_file"
sed -i "3s/.*/    background:                  $c_0;/" "$rasi_file"
sed -i "4s/.*/    red:                         $c_6;/" "$rasi_file"
sed -i "5s/.*/    selected-bg:                 $c_3;/" "$rasi_file"
sed -i "6s/.*/    selected-fg:                 $c_0;/" "$rasi_file"