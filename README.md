# Blumango's Table Tennis Scorekeeper

This is a program designed to allow user input to simulate a scoreboard that keeps track of the... well... scores.

## Features
- Defining he actual "t_tennis" function that contains everything for the code. [^1]
- Under the function itself is the following:
- Game type, players, and target score;
- Loop for during game input of scores
- And winner determination
- Then the function itself actually... functioning.

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
5. Declaration of independence... I mean... winner

## Requirements
- python 3.14.7(so far i've seen)

## Build Instructions
Ok I will do this

## Roadmap

- [x] Player Identification
- [x] Custom Target Score Selection
- [x] Manual score input
- [x] TUI coloring
- [ ] Proper TUI
- [ ] GUI basic setup
- [ ] GUI enhancement
- [ ] ball tracking
- [ ] Accurate switch between Open CU to BlurBall
- [ ] Table and House detection
- [ ] Ball altitude tracking
- [ ] Actual score tracking
- [ ] Manual fault input
- [ ] Finallization
## Background
This program was created, at first, as a "multi-sport" scorekeeper that would be used for multiple different sports and scoring systems in general. But eventually, just to keep it simple, we just began with table-tennis since most other sports required time tracking libraries and... yeah... it's a bit too much if we want anything to get done in time. So, the original creator I've decided to stick with table-tennis for a start. [^1]

Other sports and scoring systems are to be added to code in a future time.
[^1]: Originally intended to support multiple sports
[^2]: Step 4 loops until one person's/s' total points are equivalent to the Target Score
