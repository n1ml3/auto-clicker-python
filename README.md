# Auto Clicker

A simple auto clicker application built with Python and Tkinter.

## Description

Auto Clicker is a lightweight desktop application that allows you to automate mouse clicks at specified intervals. This tool is useful for tasks that require repetitive clicking.

## Features

- Customizable click intervals
- Simple and intuitive user interface
- Start/Stop functionality
- Built with Python and Tkinter

## Installation

### Pre-built Executable
1. Download the latest release from the `build/autoClicker` folder
2. Run `autoClicker.exe`

### From Source
1. Make sure you have Python 3.11 or later installed
2. Clone this repository:
```bash
git clone https://github.com/yourusername/auto-clicker.git
cd auto-clicker
```
3. Run the program:
```bash
python autoClicker.py
```

## Building from Source

To create your own executable:

1. Install PyInstaller:
```bash
pip install pyinstaller
```

2. Build the executable:
```bash
pyinstaller --onefile --windowed autoClicker.py
```

The executable will be created in the `dist` folder.

## Project Structure

```
├── autoClicker.py        # Main application source code
├── autoClicker.spec      # PyInstaller specification file
├── build/               # Build files
└── README.md            # This file
```

## Requirements

- Python 3.11 or later
- Tkinter (included with Python)

## License
Made by Namle <3
This project is open source and available under the MIT License.