# GameOfLife-Freezable
Conway's Game of Life with freezable/fixable cells

![screenshot](https://github.com/tannerbohn/GameOfLife-Freezable/blob/master/example_1.png)

## Usage
To run the code, `python main.py`

Inside main.py, you can set the following values:
* n: grid side length (be careful with large values due to updating inefficiency)
* dt: refresh/update speed (# seconds between frames)

Inside Cell.py, you can set the following values:
* `on_colour`: colour of living cells
  * note: The colours are stored as RGB lists, where 0 is min, and 1 is max
* `off_colour`: colour of dead cells
* `fixed_colour`: tint of fixed cells
* `border_width`: with of rectangle border (probably want either 0 or 1)


* `alive_to_dead_change_rate`
  * how quickly the colour for a cell changes from on colour to off colour
  * (0.5 means that every fram, the colour moves half-way from current colour to target colour)
  * for normal GOL colours, set this to 1

* `dead_to_alive_change_rate`
  * how quickly the colour for a cell changes from off colour to on colour
  * for normal GOL colours, set this to 1



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
* resizing the window is VERY slow 
