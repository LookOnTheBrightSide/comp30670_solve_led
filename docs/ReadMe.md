To use this module you will need to install it from github.
You can then pass it an input argument in the following way

```solve_led --input path_to_instructions```

The module expects a http path/url

The instructions should be in the following format :

line 1 should be the size of the LED board
from line 2 onwards will be the instructions for the board

The following are the accepted formats

--action x y x y
	on off switch being the actions

x and y are the coodinates on the board.

