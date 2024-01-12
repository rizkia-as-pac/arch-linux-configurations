#!/bin/sh

terminal_emulator="kitty"

$terminal_emulator -e sh -c "wpg -s \$(wpg -l |fzf)" &&

~/.config/sh/extract_color_scheme.sh &&

~/.config/sh/gen_active_wp.sh &&

~/.config/sh/update_rasi.sh &&


qtile cmd-obj -o cmd -f reload_config
