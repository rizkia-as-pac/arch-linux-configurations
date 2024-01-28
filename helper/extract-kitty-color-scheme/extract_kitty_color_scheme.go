package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"
	"strings"
)

type ColorSchemeV2 struct {
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
	Color9     string `json:"color9"`
	Color10    string `json:"color10"`
	Color11    string `json:"color11"`
	Color12    string `json:"color12"`
	Color13    string `json:"color13"`
	Color14    string `json:"color14"`
	Color15    string `json:"color15"`
}

func main() {
	homeDir, err := os.UserHomeDir()
	if err != nil {
		fmt.Println("Error get home directory:", err)
		return
	}

	configFilePath := fmt.Sprintf("%s/.cache/wal/colors-kitty.conf", homeDir)

	config, err := readConfig(configFilePath)
	if err != nil {
		fmt.Println("Error reading config file:", err)
		return
	}

	jsonData, err := json.MarshalIndent(config, "", "  ")
	if err != nil {
		fmt.Println("Error marshalling to JSON:", err)
		return
	}

	outputFilePath := fmt.Sprintf("%s/.config/colors-kitty.json", homeDir)

	err = writeJSON(outputFilePath, jsonData)
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

func readConfig(filePath string) (*KittyColorScheme, error) {
	file, err := os.Open(filePath)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	colors := make(map[string]string)

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		if len(line) > 0 && !strings.HasPrefix(line, "#") {
			parts := strings.Fields(line)
			if len(parts) == 2 {
				colors[parts[0]] = parts[1]
			}
		}
	}

	if err := scanner.Err(); err != nil {
		return nil, err
	}
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

	return cs, nil
}

func writeJSON(filePath string, jsonData []byte) error {
	file, err := os.Create(filePath)
	if err != nil {
		return err
	}
	defer file.Close()

	_, err = file.Write(jsonData)
	if err != nil {
		return err
	}

	return nil
}
