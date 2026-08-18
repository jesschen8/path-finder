# path-finder

An interactive pathfinding visualiser built with Pygame. Currently finds the path using A* algorithm.
To use, place a start and end point on the grid and draw in obstacles. Press the space key to start the visualisation and the c key to clear the grid.

## Movement model
Currently the paths move in four directions only, up, down, left and right. Diagonal movement is not permitted. The heuristic is Manhattan distance due to the 4-connected grid.

## Colours
 
| Colour | Meaning |
| --- | --- |
| Light blue | Start node |
| Dark blue | End node |
| Black | Wall |
| Light Green | Open set — discovered, not yet expanded |
| Red | Closed set — expanded, cost finalised |
| Green | Final path |

## Running it
 
```bash
git clone https://github.com/jesschen8/path-finder.git
cd path-finder
 
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install pygame
 
python src/main.py
```

## Credits

The project was inspired by
[Tech With Tim's A\* pathfinding visualiser](https://github.com/techwithtim/A-Path-Finding-Visualization),
but diverges in structure and code.
