# Inky E-Paper Display Project

A comprehensive Python application for displaying various types of dynamic content on Pimoroni Inky WHAT e-paper displays. This project randomly selects and displays content from multiple sources including news, weather, quotes, artwork, and more.

## Overview

This project transforms a Raspberry Pi with a Pimoroni Inky WHAT e-paper display into an intelligent information dashboard. The system randomly selects from various content modules to display fresh information each time it runs, making it perfect for a desk accessory, digital picture frame, or information kiosk.

## Features

- **Weather Information**: Current conditions, forecasts, sunrise/sunset times, moon phases, and air quality data
- **News Display**: Latest headlines from CNBC RSS feeds across multiple categories
- **Word of the Day**: Daily vocabulary with pronunciation and definitions from Dictionary.com
- **Quote Display**: Inspirational quotes from famous scientists via WikiQuotes
- **DeviantArt Integration**: Displays curated artwork from DeviantArt
- **USB Slideshow**: Shows images from connected USB drives
- **XKCD Comics**: Displays XKCD webcomics
- **DareBee Exercises**: Daily fitness challenges from DareBee
- **Multi-color Support**: Works with black, red, and yellow Inky displays

## Hardware Requirements

- Raspberry Pi (any model compatible with GPIO)
- Pimoroni Inky WHAT e-paper display (2.13", 212×104 pixels)
- MicroSD card (8GB or larger recommended)
- Optional: USB drives for slideshow functionality

## Display Types Supported

- Inky WHAT Black
- Inky WHAT Red/Black/White  
- Inky WHAT Yellow/Black/White

## Project Structure

```
Inky/
├── __init__.py                 # Main application entry point
├── bin/                       # Shell scripts for automation
│   ├── config_inky.sh         # Black display runner
│   ├── config_red_inky.sh     # Red display runner
│   ├── config_yellow_inky.sh  # Yellow display runner
│   └── scrape_deviant_art.sh  # DeviantArt image scraper
├── weather/                   # Weather module
│   ├── config.ini            # Weather API configuration
│   ├── what_weather.py       # Weather display logic
│   └── open_weather_handler.py # OpenWeather API integration
├── news/                     # News module
│   └── what_news.py          # CNBC RSS news fetcher
├── word_of_the_day/          # Dictionary module
│   └── what_word_of_the_day.py # Dictionary.com integration
├── quotes/                   # Quotes module
│   └── what_quotes.py        # WikiQuotes integration
├── deviant_art/              # Artwork module
│   ├── deviant_art_scraper.py # Image scraper
│   ├── what_deviation.py     # Image display logic
│   └── images/               # Downloaded artwork storage
├── usb_slideshow/            # USB slideshow module
│   └── slideshow.py          # USB image display
├── xkcd/                     # XKCD module
│   ├── xkdc_scraper.py       # Comic scraper
│   ├── what_xkcd.py          # Comic display logic
│   └── comics/               # Downloaded comics storage
├── darebee/                  # Fitness module
│   ├── what_darebee.py       # Exercise display
│   └── proto.ipynb           # Development notebook
└── log/                      # Application logs
```

## Installation

### 1. System Dependencies

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python dependencies
sudo apt install python3-pip python3-lxml git -y

# Install required Python packages
pip3 install pillow requests beautifulsoup4 wikiquotes inky configparser
```

### 2. Pimoroni Inky Library

```bash
# Install the official Inky library
curl https://get.pimoroni.com/inky | bash
```

### 3. Font Dependencies

The project requires specific fonts. Install them via:

```bash
pip3 install font-source-serif-pro font-source-sans-pro font-fredoka-one
```

### 4. Clone and Setup

```bash
# Clone the repository
git clone <your-repo-url> /home/pi/Code/Inky
cd /home/pi/Code/Inky

# Make shell scripts executable
chmod +x bin/*.sh
```

### 5. Configuration

#### Weather Configuration

Edit `weather/config.ini`:

```ini
[OW_API]
key = your_openweather_api_key_here

[LOCATION]
long = your_longitude
lat = your_latitude
city = Your_City
country = Your_Country_Code
```

Get a free API key from [OpenWeatherMap](https://openweathermap.org/api).

## Usage

### Manual Execution

Run the main application with optional color specification:

```bash
# Default (black display)
python3 __init__.py

# Specify display color
python3 __init__.py --color black
python3 __init__.py --color red
python3 __init__.py --color yellow
```

### Automated Execution

Use the provided shell scripts for automated deployment:

```bash
# For black display
./bin/config_inky.sh

# For red display  
./bin/config_red_inky.sh

# For yellow display
./bin/config_yellow_inky.sh
```

These scripts will:
- Pull latest code from Git repository
- Execute the Python application
- Log all output with timestamps
- Handle errors gracefully

### Scheduled Execution

Add to crontab for automatic updates:

```bash
# Edit crontab
crontab -e

# Add entries (example: update every 30 minutes)
*/30 * * * * /home/pi/Code/Inky/bin/config_inky.sh
```

## Content Modules

### Weather Module
- **Source**: OpenWeatherMap API
- **Content**: Current conditions, temperature, humidity, wind, forecasts, air quality
- **Features**: Supports metric/imperial units, UV index, moon phases

### News Module  
- **Source**: CNBC RSS feeds
- **Categories**: Top News, World News, US News, Economics, Technology, Politics
- **Features**: Headline and description display with automatic text wrapping

### Word of the Day
- **Source**: Dictionary.com
- **Content**: Daily word, pronunciation, part of speech, definition
- **Features**: Formatted display with colored headers

### Quotes Module
- **Source**: WikiQuotes
- **Content**: Random quotes from famous scientists and thinkers
- **Features**: Automatic text reflow, decorative borders

### DeviantArt Module
- **Source**: DeviantArt daily challenges
- **Content**: Curated artwork images
- **Features**: Automatic image scraping, local storage management

### USB Slideshow
- **Source**: Connected USB drives
- **Content**: JPEG/PNG images from USB storage
- **Features**: Random image selection, automatic USB detection

### XKCD Module
- **Source**: XKCD webcomic API
- **Content**: Latest and archived comics
- **Features**: Image processing for e-paper optimization

### DareBee Module
- **Source**: DareBee.com
- **Content**: Daily fitness exercises and challenges
- **Features**: Exercise image display, challenge descriptions

## Technical Details

### Display Processing

All content modules follow a standardized pattern:
1. **Content Retrieval**: Fetch data from external sources
2. **Image Processing**: Resize and optimize for 400×300 e-paper display
3. **Color Optimization**: Convert to e-paper compatible palette
4. **Text Rendering**: Apply fonts and formatting
5. **Display Output**: Return processed PIL Image object

### Image Optimization

Images are automatically processed for optimal e-paper display:
- Resized to 400×300 pixels
- Cropped to maintain aspect ratio
- Converted to 3-color palette (Black, White, Red/Yellow)
- Dithered for better visual quality

### Error Handling

- Network timeouts and API failures are gracefully handled
- Missing content sources trigger fallback behavior
- All errors are logged with timestamps
- Application continues running even with module failures

### Logging

Comprehensive logging system:
- Parent process logs: `log/logfile_parent_YYYY-MM-DD--HH-MM.log`
- Application logs: `log/logfile_YYYY-MM-DD--HH-MM.log`  
- Error logs: `log/errfile_YYYY-MM-DD--HH-MM.log`

## Customization

### Adding New Content Modules

1. Create new module directory
2. Implement `create_image(inky_display, color)` function
3. Add module import to `__init__.py`
4. Add entry to choices dictionary
5. Create `__init__.py` with display function

### Modifying Content Sources

Each module can be customized by editing its respective source file:
- Weather: Modify API endpoints in `weather/what_weather.py`
- News: Change RSS feeds in `news/what_news.py`
- Quotes: Update person list in `quotes/what_quotes.py`

### Display Timing

Modify the main script to control how often different content types appear by adjusting the weights in the choices dictionary.

## Troubleshooting

### Common Issues

1. **"No module named 'inky'"**
   - Solution: Install Pimoroni Inky library: `curl https://get.pimoroni.com/inky | bash`

2. **Weather data not loading**
   - Check OpenWeatherMap API key in `weather/config.ini`
   - Verify internet connection
   - Check API usage limits

3. **Fonts not found**
   - Install font packages: `pip3 install font-source-serif-pro font-source-sans-pro font-fredoka-one`

4. **USB slideshow not working**
   - Ensure USB drive is mounted in `/media/pi/`
   - Check image file formats (JPG, PNG supported)
   - Verify read permissions

### Debug Mode

Run with Python's verbose flag for detailed error information:

```bash
python3 -v __init__.py --color black
```

### Log Analysis

Check recent logs for errors:

```bash
# View latest application log
tail -f log/logfile_$(date +'%Y-%m-%d')-*.log

# View error log
tail -f log/errfile_$(date +'%Y-%m-%d')-*.log
```

## Performance Considerations

- Content retrieval is cached where possible
- Images are processed once and reused
- Network requests include reasonable timeouts
- Old log files should be cleaned periodically
- DeviantArt images are automatically cleaned (7-day retention)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Implement your changes
4. Test with actual hardware
5. Submit a pull request

## API Keys and Rate Limits

- **OpenWeatherMap**: 1,000 calls/day (free tier)
- **Dictionary.com**: No API key required
- **WikiQuotes**: No API key required  
- **CNBC RSS**: No API key required
- **DeviantArt**: Web scraping (respect robots.txt)

## License

This project is open source. Please respect the terms of service of all integrated APIs and content sources.

## Acknowledgments

- Pimoroni for the excellent Inky display libraries
- OpenWeatherMap for weather data API
- All content providers (CNBC, Dictionary.com, WikiQuotes, etc.)
- Font creators and open source community

## Version History

- **v1.0**: Initial release with basic weather and news
- **v2.0**: Added quotes, word of the day, and DeviantArt integration
- **v3.0**: USB slideshow, XKCD, and DareBee modules
- **Current**: Multi-color display support and improved error handling
