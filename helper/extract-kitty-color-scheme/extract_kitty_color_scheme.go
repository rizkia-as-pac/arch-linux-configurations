package main

import (
	"encoding/json"
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

	cs := buildColorSchemeJSON(colors)

	jsonData, err := json.MarshalIndent(cs, "", "  ")
	if err != nil {
		fmt.Println("Error marshalling to JSON:", err)
		return
	}

	outputFilePath := fmt.Sprintf("%s/.config/colors-kitty.json", homeDir)

	err = helper.WriteJSON(outputFilePath, jsonData)
	if err != nil {
		fmt.Println("Error writing JSON file:", err)
		return
	}
}

type KittyColorScheme struct {
	Cursor            string `json:"Cursor"`
	Cursor_text_color string `json:"Cursor_text_color"`
	Url_color         string `json:"Url_color"`
	Bell_border_color string `json:"Bell_border_color"`
	Mark1_foreground  string `json:"Mark1_foreground"`
	Mark2_foreground  string `json:"Mark2_foreground"`
	Mark3_foreground  string `json:"Mark3_foreground"`
	Color0            string `json:"Color0"`
	Color1            string `json:"Color1"`
	Color2            string `json:"Color2"`
	Color3            string `json:"Color3"`
	Color4            string `json:"Color4"`
	Color5            string `json:"Color5"`
	Color6            string `json:"Color6"`
	Color7            string `json:"Color7"`
	Color8            string `json:"Color8"`
	Color9            string `json:"Color9"`
	Color10           string `json:"Color10"`
	Color11           string `json:"Color11"`
	Color12           string `json:"Color12"`
	Color13           string `json:"Color13"`
	Color14           string `json:"Color14"`
	Color15           string `json:"Color15"`
}

func buildColorSchemeJSON(colors map[string]string) *KittyColorScheme {
	cs := &KittyColorScheme{
		Cursor:            colors["cursor"],
		Cursor_text_color: colors["background"],
		Url_color:         colors["cursor"],
		Bell_border_color: colors["color3"],
		Mark1_foreground:  colors["background"],
		Mark2_foreground:  colors["background"],
		Mark3_foreground:  colors["background"],
		Color0:            colors["color0"],
		Color1:            colors["color1"],
		Color2:            colors["color2"],
		Color3:            colors["color3"],
		Color4:            colors["color4"],
		Color5:            colors["color5"],
		Color6:            colors["color6"],
		Color7:            colors["color7"],
		Color8:            colors["color8"],
		Color9:            colors["color9"],
		Color10:           colors["color10"],
		Color11:           colors["color11"],
		Color12:           colors["color12"],
		Color13:           colors["color13"],
		Color14:           colors["color14"],
		Color15:           colors["color15"],
	}

	return cs
}