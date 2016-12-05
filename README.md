# GameOfLife-Freezable
Conway's Game of Life with freezable/fixable cells

## Usage
To run the code, `python main.py`

Inside main.py, you can set the following values:
* n: grid side length (be careful with large values due to updating inefficiency)
* dt: refresh/update speed (# seconds between frames)


When using the program, the following operations are available:
* p: play/pause
* f: faster
* s: slower
* c: soft clear (kills normal cells)
* C: hard clear (soft clear + resets fixed cells)
* left click on cell: toggles cell state (alive/dead)
* right click on cell: toggles cell fixed state (fixed/not fixed)
  * can then left click on cell to toggle alive/dead state

## Tips
* If you want to change the on/off/fixed colours, go to the top of the Cell class. The colours are stored as RGB lists, where 0 is min, and 1 is max.
* resizing the window is VERY slow 
