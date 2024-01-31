#!/bin/sh

terminal_emulator="kitty"

$terminal_emulator -e sh -c "wpg -s \$(wpg -l |fzf)" &&

~/.config/helper/extract-kitty-color-scheme/extract-kitty-color-scheme &&

~/.config/helper/extract-kitty-color-conf/extract-kitty-color-conf &&

~/.config/sh/gen_active_wp.sh &&

~/.config/sh/update_rofi_theme.sh &&


qtile cmd-obj -o cmd -f reload_config
