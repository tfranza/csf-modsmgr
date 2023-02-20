"""Module storing the current state of the applied mods."""

import os
import pickle as pk

class State:

	state = {
		'cfg_orig'		: 1,
		'ws_fix'	 	: 0,
		'no_ext_view'	: 0
	}

	def __init__(self):
        """
        Constructor method to initialize gui root reference, frames and widgets
        
        Args:
            gui_title (str) : text that will appear in the title bar
            gui_size  (str) : size of the window application

        Returns: 
            None
        
        """
		self.load_state()

	def save_state(self, 
		path: str = ''
	) -> str:
		"""
		Saves the current state of active mods and relevant variables 
		in the specified path.

		Args:
			path (str) : relative path where to store the state

		Returns:
			str: failure message

		"""
		return None

	def load_state(self, 
		path: str
	) -> str:
		"""
		Loads the current state of active mods and relevant variables 
		from the file stored in specified path.

		Args:
			path (str) : relative path where the state is stored

		Returns:
			str: failure message

		"""
		return None
