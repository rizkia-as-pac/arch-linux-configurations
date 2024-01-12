#!/bin/sh

terminal_emulator="kitty"

# Options
ctbw='Change theme based on wallpaper'
ant='Add new theme'
delt='Delete theme'
rlq='Reload qtile config'


# Rofi CMD
rofi_cmd() {
	rofi \
	    -dmenu -p "Utility Options" -config $HOME/.config/rofi/utilmenu/config.rasi
}

# Pass variables to rofi dmenu
run_rofi() {
	echo -e "$ctbw\n$ant\n$delt\n$rlq" | rofi_cmd
}

# Actions
chosen="$(run_rofi)"
case ${chosen} in
    $ctbw)
		~/.config/sh/change_theme.sh
        ;;
	$rlq)
		qtile cmd-obj -o cmd -f reload_config
        ;;
	$ant)
		$terminal_emulator -e sh -c "wpg -a \$(fzf)"
        ;;
	$delt)
		$terminal_emulator -e sh -c "wpg -d \$(wpg -l | fzf)"
        ;;
esac

