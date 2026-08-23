# Blumango's Table Tennis Scorekeeper

This is a program designed to allow user input to simulate a scoreboard that keeps track of the... well... scores.

**We’re happy to announce that BlueMangoScoreKeeper is now on PyPI! Just install the program using** `pip install bluemangoscorekeeper` 

## Features
- Table tennis scoring
- Custom target scores
- Two-point advantage
- Singles and doubles support
- Custom player/team names
- Manual point input
- Live score display
- Input validation
- Colored terminal output
- Command-line interface
- Installable CLI
- Python 3.9+ support

## How It Works
When running the code immediately, for now, the code accepts manual user input from the user every time somebody scores. It does this during the game by using loop to continue until somebody reaches the target score.

## Usage
**Everything that will appear in the TUI in order**
1. Target score statement
2. Player/team input
3. Asking whether or not the game is singles or doubles
4. Beginning the game
   - Asking who scored the point
   - Stating current scores [^2]
5. Declaration of ~~independence~~... I mean... winner

## Requirements
- Python 3.9+

## Build Instructions
1. Clone the repo:
   `git clone https://github.com/BlumanGoesRouge786/BlueMangoScoreKeeper.git`

2. Enter the project directory:
   `cd BlueMangoScoreKeeper`

3. Install the build tool:
   `python -m pip install build`

4. Build the package:
   `python -m build`

The built packages will be placed in the `dist/` directory

## Roadmap

- [x] Player Identification
- [x] Custom Target Score Selection
- [x] Manual score input
- [x] TUI coloring
- [ ] Proper TUI
- [ ] GUI basic setup
- [ ] GUI enhancement
- [ ] ball tracking
- [ ] Accurate switch between Open CV and BlurBall
- [ ] Table and House detection
- [ ] Ball altitude tracking
- [ ] Actual score tracking
- [ ] Manual fault input
- [ ] Finallization
## Background
This program was created, at first, as a "multi-sport" scorekeeper that would be used for multiple different sports and scoring systems in general. But eventually, just to keep it simple, we just began with table-tennis since most other sports required time tracking libraries and... yeah... it's a bit too much if we want anything to get done in time. So, I've decided to stick with table-tennis for a start. [^1]

Other sports and scoring systems are to be added to code in a future time.
[^1]: Originally intended to support multiple sports
[^2]: Step 4 loops until one person's/s' total points are equivalent to the Target Score
