"""Module for handling mods."""

import os
from pathlib import Path

from .backup import recover
from .paths import PATH

def set_cfg_orig() -> str:
    """
    Reset config files to originals.
    
    Args:
        None

    Returns: 
        str: Failure message

    """
    return __set_config__(PATH.CFG_ORIG.value)

def set_cfg_demo() -> str:
    """
    Reset config files to demo (decyphered).
    
    Args:
        None

    Returns: 
        str: Failure message

    """
    return __set_config__(PATH.CFG_DEMO.value)

def set_wsfix() -> str:
    """
    Apply widescreen fix mod.

    Args:
        None
    
    Returns: 
        str: Failure message

    """
    return __set_config__(PATH.CFG_WSFIX.value)

def set_no_ext_view() -> str:
    """
    Apply no-external-view mod.

    Args:
        None
    
    Returns: 
        str: Failure message

    """
    return __set_config__(PATH.CFG_EXTV.value)

def run_game(
    ws_fix: bool = True
) -> str:
    """
    Run the executable game file that corresponds to the widescreen fix, if active.
    
    Args:
        ws_fix (bool) : True if the widescreen fix mod is active

    Returns: 
        str: Failure message

    """
    exe_path = None
    if ws_fix:
        print('> Running widescreen executable.')
        exe_path = PATH.HOME.value / PATH.EXE_16_9.value
    else:
        print('> Running original executable.')
        exe_path = PATH.HOME.value / PATH.EXE_4_3.value

    error_msg = None
    print(exe_path)
    if exe_path.exists():
        os.startfile(exe_path)
    else:
        error_msg = 'Can\'t run the game. Exe not found in predefined path.'

    return error_msg


####################          Utility functions          ####################

def __set_config__(
    src_folder: str,
    dest_folder: str = PATH.CFG.value
) -> str:
    """
    Update files in the config folder.
    
    Args:
        src_folder  (str) : path of the source folder
        dest_folder (str) : path of the config folder

    Returns: 
        str: Failure message
    
    """
    error_msg = None
    if src_folder.is_dir():
        for filename in os.listdir(src_folder):
            from_path = Path(src_folder) / filename
            to_path   = Path(dest_folder) / filename
            error_msg = recover(from_path=from_path, to_path=to_path)
            if error_msg:                   # if recover generates an error message, return it
                break
    else:
        error_msg = 'Can\'t find source folder.'

    return error_msg
