#!/bin/bash

# Specify the file path
file_path="$HOME/.config/wpg/wp_init.sh"

# Use sed to extract file names inside single quotes
file_names=$(sed -n "s/wpg -rs '\([^']*\)' '\([^']*\)'/\1 \2/p" "$file_path")

# Use cat to concatenate the files
echo $file_names > $HOME/.config/active_wp.txt
