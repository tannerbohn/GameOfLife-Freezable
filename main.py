from Game import *


if __name__ == "__main__":

	# p: play/pause
	# f: faster
	# s: slower
	# c: soft clear (kills normal cells)
	# C: hard clear (soft clear + resets fixed cells)

	# left click on cell: toggles cell state (alive/dead)
	# right click on cell: toggles cell fixed state (fixed/not fixed)
	#    - can then left click on cell to toggle alive/dead state


	# n = grid side length
	# dt = update time in seconds
	G = Game(n=55, dt=0.1)
	G.run()