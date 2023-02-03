**on hold, getting lyrics is harder than it's worth**

<!--<p align="center">
<img src="src/logo.png" width="250"/>
</p>-->

<br />
<div align="center">
  <h1 align="center">Discord Lyric-Bot</h3>

  <p align="center">
    [In Progress] Discord bot that sends lyrics of the day
    <br />
    <a href="#">No Link :[</a>
  </p>
</div>

## Table of Contents

- [Description](#description)
  - [Features](#features)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
- [Technical Stuff](#technical-stuff)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

---

# Description

Discord bot that sends lyrics of the day made with python.

This is just a temporary project I don't plan on continually maintaining it.

> Using LyricsGenius to search and scrape Genius pages for lyrics. Couldn't find a free lyric api and musixmatch was geared towards companies requiring too much personal info to sign up for free testing plan.

**_For Education Purposes Only_** or whatever jargon to not get sued by the evil copyright people killing creativity.

## Features

- `/lyric` - get random lyric

# Getting Started

### Prerequisites

- Python
- Discord Token (**TODO** add required permissions)
- Genius API Token

### Installation

1. Run `pip install src/requirements.txt`
2. Add tokens to production environment or `src/.env` (see `sample.env` for reference).
3. Run `python src/main.py` to start bot

# Technical Stuff

Built with <3

- Python
  - LyricsGenius
  - pycord
- Genius API
- Discord

---

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments

- [pycord](https://github.com/Pycord-Development/pycord)
- [LyricsGenius](https://github.com/johnwmillr/LyricsGenius)
- [Genius API](https://genius.com/developers)
