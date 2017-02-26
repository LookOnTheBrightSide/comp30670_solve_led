import sys
from nose.tools import *
from solve_led.main import *

def test_create_board():
	eq_(len(create_board(20)),20)
	eq_(len(create_board(10)),10)
	eq_(len(create_board(2)),2)

def test_create_board_values():
	eq_(create_board(2),[[False, False],[False, False]])
	eq_(create_board(3),[ [False, False,False],
												[False, False, False],
												[False, False, False]])

def test_clean_up_input_file():
	eq_(clean_up_input_file(['turn off 660,55 through 986,197', 'turn off 341,304 through 638,850']), [["off",660,55,986,197],["off",341,304,638,850]])
	eq_(clean_up_input_file(['turn off 444,66 through 333,888', 'turn off 341,304 through 777,850']), [["off",444,66,333,888],["off",341,304,777,850]])
	eq_(clean_up_input_file(['turn off 660,300 through 400,500', 'turn off 500,222 through 333,555']), [["off",660,300,400,500],["off",500,222,333,555]])

def test_board_plotter():
	eq_(board_plotter([['on', 0, 0, 2, 2]], [[False, False],[False, False]]), [[True, True],[True, True]])
	eq_(board_plotter([['off', 0, 0, 2, 2]], [[True, True],[True, True]]), [[False, False],[False, False]])
	eq_(board_plotter([['switch', 0, 0, 2, 2]], [[False, True],[True, False]]), [[True, False],[False, True]])

def test_print_lights_totals():
	eq_(print_lights_totals([[False, False],[False, False]]), ('On count is : ', 0))
	eq_(print_lights_totals([[False, True],[True, False]]), ('On count is : ', 2))
	eq_(print_lights_totals([[True, True],[True, False]]), ('On count is : ', 3))

def test_version():
	eq_(sys.version_info[0], 3, "Python is not in version 3")