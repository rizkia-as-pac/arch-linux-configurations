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
	Foreground string `json:"foreground"`
	Background string `json:"background"`
	Cursor     string `json:"cursor"`
	Color0     string `json:"color0"`
	Color1     string `json:"color1"`
	Color2     string `json:"color2"`
	Color3     string `json:"color3"`
	Color4     string `json:"color4"`
	Color5     string `json:"color5"`
	Color6     string `json:"color6"`
	Color7     string `json:"color7"`
	Color8     string `json:"color8"`
	Color15    string `json:"color15"`
}

func buildColorSchemeJSON(colors map[string]string) *KittyColorScheme {
	cs := &KittyColorScheme{
		Foreground: colors["foreground"],
		Background: colors["background"],
		Cursor:     colors["cursor"],
		Color0:     colors["color0"],
		Color1:     colors["color1"],
		Color2:     colors["color2"],
		Color3:     colors["color3"],
		Color4:     colors["color4"],
		Color5:     colors["color5"],
		Color6:     colors["color6"],
		Color7:     colors["color7"],
		Color8:     colors["color8"],
		Color15:    colors["color15"],
	}

	return cs
}
