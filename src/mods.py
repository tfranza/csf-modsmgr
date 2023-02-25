"""Module for handling mods."""

import os
from pathlib import Path

from .backup import recover
from .paths import PATH
from .logs import LOG

def set_cfg_orig():
    """
    Reset config files to originals.
    
    Args:
        None

    Returns: 
        None

    """
    __set_config__(PATH.CFG_ORIG.value)

def set_cfg_demo():
    """
    Reset config files to demo (decyphered).
    
    Args:
        None

    Returns: 
        None

    """
    __set_config__(PATH.CFG_DEMO.value)

def set_wsfix():
    """
    Apply widescreen fix mod.

    Args:
        None
    
    Returns: 
        None

    """
    __set_config__(PATH.CFG_WSFIX.value)

def set_noextview():
    """
    Apply no-external-view mod.

    Args:
        None
    
    Returns: 
        None

    """
    __set_config__(PATH.CFG_EXTV.value)

def run_game(
    ws_fix: bool = True
):
    """
    Run the executable game file that corresponds to the widescreen fix, if active.
    
    Args:
        ws_fix (bool) : True if the widescreen fix mod is active

    Raises:
        FileNotFoundError: missing exe file to run the game

    """
    exe_path = None
    if ws_fix:
        print('> Running widescreen executable.')
        exe_path = PATH.HOME.value / PATH.EXE_16_9.value
    else:
        print('> Running original executable.')
        exe_path = PATH.HOME.value / PATH.EXE_4_3.value

    if Path.exists(exe_path):
        os.startfile(exe_path)
    else:
        raise FileNotFoundError(LOG.ERR_RUN_GAME.value)


####################          Utility functions          ####################

def __set_config__(
    src_folder: str,
    dest_folder: str = PATH.CFG.value
):
    """
    Update files in the config folder.
    
    Args:
        src_folder  (str) : path of the source folder
        dest_folder (str) : path of the config folder

    Returns: 
        None

    Raises:
        FileNotFoundError: missing folder or config files to be set 

    """
    if src_folder.is_dir():
        for filename in os.listdir(src_folder):
            from_path = Path(src_folder) / filename
            to_path   = Path(dest_folder) / filename
            recover(from_path=from_path, to_path=to_path)
    else:
        raise FileNotFoundError(LOG.ERR_CFG_NO_DIR.value)
