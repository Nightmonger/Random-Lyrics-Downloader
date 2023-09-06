# Random Lyrics Downloader

## Table of Contents

- [Random Lyrics Downloader](#random-lyrics-downloader)
  - [Table of Contents](#table-of-contents)
  - [About ](#about-)
    - [Prerequisites](#prerequisites)
    - [Installing](#installing)
  - [Usage ](#usage-)
    - [API Used](#api-used)
    - [Acknowledgments](#acknowledgments)

## About <a name = "about"></a>

This is a simple Python script that downloads random song lyrics from a [Genius API](ttps://github.com/johnwmillr/LyricsGenius) and save them to txt file. It's a fun way to discover new song lyrics or just have a random musical quote for your day!



### Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.8 installed on your system.
- The following Python libraries installed:
  - requests
  - lyricsgenius

You can install the required libraries using pip:
```
pip install lyricsgenius
```

### Installing 

1. First, ensure that you have the script available on your system. If you haven't already, you can clone the repository or download the script from GitHub.
2. Open your terminal and edit your shell profile configuration file. Depending on your default shell, you might be using either Bash or Zsh. Here are the commands to open the respective configuration files: 

```bash 
nano ~/.bash_profile #For Bash
```

```bash
nano ~/.zshrc #For Zsh
```
3. **Create an alias:**
Add the following line at the end of your profile file to create an alias for your script:
```bash
alias download-lyrics='python /path/to/lyrics_downloader.py'
```

Replace /path/to/lyrics_downloader.py with the actual path to your lyrics_downloader.py script. Also, choose a suitable alias name (download-lyrics in this example) that you'd like to use to run the script.

4. **Save and Exit:**
    After adding the alias, save the changes and exit the text editor. In Nano, you can press Ctrl + O to save and Ctrl + X to exit.

5. **Reload Your Shell Profile:**
   ```bash
   source ~/.bash_profile  # For Bash
   ```
   ```bash
   source ~/.zshrc  # For Zsh
   ```
## Usage <a name = "usage"></a>

1. Clone this repository to your local machine:
```git
git clone https://github.com/yourusername/random-lyrics-downloader.git
```
2. Change to the project directory (in case you didnt make alias):
```
cd random-lyrics-downloader
```
3. Run the script:
```
python lyrics_downloader.py
```

### API Used
This script uses the Random [Genius API](ttps://github.com/johnwmillr/LyricsGenius) to fetch random song lyrics. You can learn more about the API by visiting their website.

### Acknowledgments
1. Thanks to [Genius API](ttps://github.com/johnwmillr/LyricsGenius) for providing the lyrics data.
2. make sure you change to your TOKEN in the code