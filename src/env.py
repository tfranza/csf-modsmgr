"""Module storing the current state of the applied mods."""

import pickle as pk

from .logs import LOG
from .paths import PATH

class Environment:
    """Environment used from the Mod Manager to update GUI elements."""

	# state reference
    state: dict

    def __init__(self):
        """
        Constructor method to initialize gui root reference, frames and widgets
        
        Args:
            gui_title (str) : text that will appear in the title bar
            gui_size  (str) : size of the window application

        Returns: 
            None
        
        """
        self.state = {
            'cfg_orig'      : 1,
            'mod_wsfix'     : 0,
            'mod_noextv'    : 0
        }

    # change state functions
    def __update_state__(self,
    	state_key: str,
    	enabled  : int
    ):
        """
        Change state by assigning 0 or 1, to the corresponding state key, 
        according to the value of enabled.

        Args:
            state_key (str) : state key to be changed
            enabled (int)   : next state to be assigned to the state key

        Returns:
            None

        Raises:
            KeyError: missing key for specific state

        """
        print('> Updating environment...')

        if state_key in self.state.keys():
            self.state[state_key] = enabled
        else:
            raise KeyError(LOG.ERR_STATE_KEY.value)

    def enable(self,
        state_key: str
    ):
        """
        Update state by assigning 1 to the corresponding state key.

        Args:
            state_key (str) : state key to be enabled

        Returns:
            None

        """
        self.__update_state__(state_key, 1)

    def disable(self,
        state_key: str
    ):
        """
        Update state by assigning 0 to the corresponding state key.

        Args:
            state_key (str) : state key to be disabled

        Returns:
            None

        """
        self.__update_state__(state_key, 0)

    ## serialization functions
    def save_state(self,
        path: str = PATH.RES_STATE.value
    ):
        """
        Saves the current state of active mods and relevant variables
        in the specified path.

        Args:
            path (str) : relative path where to store the state

        Returns:
            None

        Raises:
            KeyError: missing key for specific state

        """
        print('> Saving environment...')

        try:
            with open(path, 'wb') as handle:
                pk.dump(self.state, handle, protocol=pk.HIGHEST_PROTOCOL)
        except FileNotFoundError as err:
            raise FileNotFoundError(LOG.ERR_STATE_SAVE.value) from err

    def load_state(self,
        path: str = PATH.RES_STATE.value
    ):
        """
        Loads the current state of active mods and relevant variables 
        from the file stored in specified path.

        Args:
            path (str) : relative path where the state is stored

        Returns:
            None

        Raises:
            FileNotFoundError: missing environment file

        """
        print('> Loading environment...')

        try:
            with open(path, 'rb') as handle:
                self.state = pk.load(handle)
        except FileNotFoundError as err:
            raise FileNotFoundError(LOG.ERR_STATE_LOAD.value) from err

    # getters
    def __get_state__(self,
        state_key: str
    ) -> int:
        """
        Gets the value for the corresponding state key.

        Args:
            state_key (str) : state key for which the status is retrieved

        Returns:
            int: the state value

        """
        return self.state[state_key]

    # getters
    def cfg_orig(self) -> int:
        """
        Gets the value for original config files presence.

        Args:
            None

        Returns:
            int: cfg_orig state value

        """
        return self.__get_state__('cfg_orig')

    def wsfix(self) -> int:
        """
        Gets the value for widescreen fix mod active.

        Args:
            None

        Returns:
            int: cfg_orig state value

        """
        return self.__get_state__('mod_wsfix')

    def noextv(self) -> int:
        """
        Gets the value for no-external-view mod active.

        Args:
            None

        Returns:
            int: cfg_orig state value

        """
        return self.__get_state__('mod_noextv')
