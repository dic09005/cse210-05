# Cycle

Cycle is a game where the players try to cut each other off using cycles that leave a trail behind them.

## Getting Started

---

Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.

```
python3 -m pip install raylib
```

After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

python3 snake

```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the
project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```

cse210-05 (project root folder)
│ README.md (general info)

C │ **main**.py (entry point for program) (NEEDS CHANGED)
│ constants.py (don't change)
└───game (specific game folders)
└───casting
│ actor.py (good)
│ cast.py (good)
│ food.py (we don't need food)
C │ score.py (NEEDS CHANGED)
C │ snake.py (NEEDS CHANGED)
└───directing
│ director.py (don't change)
└───scripting
│ action.py (don't change)
C │ control_actors_action.py (NEEDS CHANGED)
C | control_actors_growing.py (NEEDS ADDED)
C │ draw_actors_action.py (NEEDS CHANGED)
C │ handle_collisions_action.py (NEEDS CHANGED)
│ move_actors_action.py (don't change)
│ script.py (don't change)
└───services
│ keyboard_service.py (don't change)
│ video_service.py (don't change)
└───shared (good)
│ color.py (don't change)
│ point.py (don't change)

```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors
---
* TODO: Add your name and email here
```
