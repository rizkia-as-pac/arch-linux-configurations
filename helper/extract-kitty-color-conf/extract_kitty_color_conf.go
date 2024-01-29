package main

import (
	"fmt"
	"os"

	"github.com/rizkia-as-actmp/arch-linux-config-helper/helper"
)

func main() {
	homeDir, err := os.UserHomeDir()
	if err != nil {
		fmt.Println("Error get home directory:", err)
		return
	}

	configFilePath := fmt.Sprintf("%s/.cache/wal/colors-kitty.conf", homeDir)

	colors, err := helper.ReadConfig(configFilePath)
	if err != nil {
		fmt.Println("Error reading config file:", err)
		return
	}

	// colors["background"] = "#1e1e2e" // $UNKNOWN VAR fix
	// colors["foreground"] = "#ffffff" // blocked foreground fix

	sb := fmt.Sprintf(`
foreground              %s
inactive_tab_foreground %s
		
background              %s
inactive_tab_background %s
cursor_text_color       %s
mark1_foreground 		%s
mark2_foreground 		%s
mark3_foreground 		%s
active_tab_foreground   %s
tab_bar_background      %s
		
cursor                  %s
url_color               %s

color0 					%s
selection_foreground    %s

color8 					%s
inactive_border_color   %s
		
bell_border_color       %s
color3  				%s
color11 				%s

active_border_color     %s
mark1_background 		%s
color4  				%s
color12 				%s

color5  				%s
color13 				%s
active_tab_background   %s
mark2_background 		%s
		
mark3_background 		%s
color6  				%s
color14 				%s
		
color1 					%s
color9 					%s

color2  				%s
color10 				%s

color7  				%s
color15 				%s

	`,
		colors["foreground"], // foreground
		colors["foreground"], // inactive_tab_foreground

		colors["background"], // background
		colors["background"], // inactive_tab_background
		colors["background"], // cursor_text_color
		colors["background"], // mark1_foreground
		colors["background"], // mark2_foreground
		colors["background"], // mark3_foreground
		colors["background"], // active_tab_foreground
		colors["background"], // tab_bar_background

		colors["cursor"], // cursor
		colors["cursor"], // url_color

		colors["color0"], // color0
		colors["color0"], // selection_foreground

		colors["color8"], // color8
		colors["color8"], // inactive_border_color

		colors["color3"], // bell_border_color
		colors["color3"], // color3
		colors["color3"], // color11

		colors["color4"], // active_border_color
		colors["color4"], // mark1_background
		colors["color4"], // color4
		colors["color4"], // color12

		colors["color5"], // color5
		colors["color5"], // color13
		colors["color5"], // active_tab_background
		colors["color5"], // mark2_background

		colors["color6"], // mark3_background
		colors["color6"], // color6
		colors["color6"], // color14

		colors["color1"], // color1
		colors["color1"], // color9

		colors["color2"], // color10
		colors["color2"], // color2

		colors["color7"],  // color7
		colors["color15"], // color15
	)

	outputFilePath := fmt.Sprintf("%s/.config/kitty/generated-theme.conf", homeDir)

	err = os.WriteFile(outputFilePath, []byte(sb), 0644)
	if err != nil {
		fmt.Println("Error writing to color.conf:", err)
		return
	}

}
