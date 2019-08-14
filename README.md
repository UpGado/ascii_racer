# ASCII RACER
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

### How to set up?
Make sure you are running at least Python 3.6.0

Only dependency is `curses` module. Depending on your platform:
- Linux or Mac: you're all set, as it will be installed by default.
- Windows: you might have to run the game in Cygwin or a Windows Subsytem for Linux (WSL). Or you can try running `pip install windows-curses`

Clone the repository

```bash
$ git clone https://github.com/UpGado/ascii_racer.git
```
or download it as a .zip file.

### Start Game
To start, run `python3 game.py` to begin the game

### Scoring
There are four different types of drinks that you can collect on the racetrack. 
* Vodka - 10 Points
* Gin - 5 Points
* $ - 1 Point
* Beer - Negative 20 points

### Contributions
If you encounter any problem or have any suggestions, please [open an issue](https://github.com/UpGado/ascii_racer/issues/new) or [send a PR](https://github.com/UpGado/ascii_racer/pulls).

ASCII-RACER is still in beta. If you are interested, contributions are highly welcome.
