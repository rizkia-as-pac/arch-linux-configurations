#!/bin/bash

file_path="$HOME/.config/wpg/sequences"

# Extract color codes with "#" using grep
color_matches=$(grep -o '#[0-9a-fA-F]\{6\}' "$file_path")

# Construct a JSON-formatted string
json_result="{"
i=0
for color in $color_matches; do
    json_result+="\"c_$i\":\"$color\","
    ((i++))
done
json_result="${json_result%,}"  # Remove the trailing comma
json_result+="}"

# Save the JSON result to a file
echo "$json_result" > ~/.config/color_scheme.json