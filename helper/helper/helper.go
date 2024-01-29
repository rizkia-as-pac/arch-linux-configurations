package helper

import (
	"bufio"
	"os"
	"strings"
)

func ReadConfig(filePath string) (map[string]string, error) {
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

	return colors, nil
}


func WriteJSON(filePath string, jsonData []byte) error {
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
