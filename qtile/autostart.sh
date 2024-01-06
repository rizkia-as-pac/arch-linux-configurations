#!/bin/bash

# Update screens
autorandr --change

# Set wallpaper
# ~/.fehbg &
nitrogen --restore

# Send welcome notification
notify-send "Welcome"