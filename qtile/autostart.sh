#!/bin/bash

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

# this will start the daemon
flameshot &
# this will select a 300 by 200 pixel area, and immediately pin it
flameshot gui --region 300x200+300+300 --pin --accept-on-select c