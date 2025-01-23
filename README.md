# Google Form Mass Submission Bot

An automated tool for submitting Google Forms multiple times with randomized radio button selections. Features multi-threading for parallel submissions and human-like interaction delays.

## Features

- Multi-threaded form submissions
- Random radio button selection
- Human-like interaction delays
- Configurable number of threads and submissions
- Error handling and automatic retry
- Chrome WebDriver integration

## Requirements

```
selenium==4.11.2
webdriver-manager==4.0.0
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/riyadmondol2006/google-form-submitter.git
cd google-form-submitter
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the script:
```bash
python form_submitter.py
```

2. Enter the requested information:
   - Number of parallel windows
   - Number of submissions per window

## ⚠️ Disclaimer

This tool is for educational purposes only. Use responsibly and in accordance with Google's terms of service.

## Author

Riyad M. ([@riyadmondol2006](https://github.com/riyadmondol2006))

## License

MIT License
