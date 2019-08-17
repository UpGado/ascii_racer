# ASCII RACER

[![PyPI version](https://badge.fury.io/py/asciiracer.svg)](https://badge.fury.io/py/asciiracer)
[![Build Status](https://travis-ci.com/UpGado/ascii_racer.svg?branch=master)](https://travis-ci.com/UpGado/ascii_racer)
![GitHub last commit](https://img.shields.io/github/last-commit/UpGado/ascii_racer)
[![Downloads](https://pepy.tech/badge/asciiracer)](https://pepy.tech/project/asciiracer)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

A racing game that runs in Terminal. 100% Python

<p align="center"><img src="https://raw.githubusercontent.com/UpGado/ascii_racer/master/docs/gameplay.gif" alt="ascii-racer"/></p>

## Instructions

Collect as many alcoholic drinks as possible, while avoiding the `Beer` drinks. The game is only key-based.

| Keys | Role        |
|------|-------------|
| a    | Move Left   |
| d    | Move Right  |
| w    | Accelerate  |
| s    |  Decelerate |
| q    |  Quit game  |

### Installation

> ```diff
> + Please report issues if you try to install and run into problems!
> ```

Make sure you are running at least Python 3.6.0

Install using pip:
```bash
pip3 install asciiracer
```
or clone the repository and install manually:

```bash
$ git clone https://github.com/UpGado/ascii_racer.git
$ cd ascii_racer && python3 setup.py install
```

### Start Game
To start the game, run either:
```bash
$ asciiracer
$ python -m asciiracer
```

### Scoring
There are four different types of drinks that you can collect on the racetrack. 
* Vodka - 10 Points
* Gin - 5 Points
* $ - 1 Point
* Beer - Negative 20 points

### Contributions
If you encounter any problem or have any suggestions, please [open an issue](https://github.com/UpGado/ascii_racer/issues/new) or [send a PR](https://github.com/UpGado/ascii_racer/pulls).

ASCII-RACER is still new. If you are interested, contributions are highly welcome!
