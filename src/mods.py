"""Module for handling mods."""

import os
from pathlib import Path
import re

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

    Raises:
        FileNotFoundError: missing config files to be recovered

    """
    # recover config files
    recover(from_path = PATH.DEMO.value / PATH.CFG_CONTROL.value,
            to_path   =                   PATH.CFG_CONTROL.value)
    recover(from_path = PATH.DEMO.value / PATH.CFG_EDITOR.value,
            to_path   =                   PATH.CFG_EDITOR.value)
    recover(from_path = PATH.DEMO.value / PATH.CFG_JUEGO.value,
            to_path   =                   PATH.CFG_JUEGO.value)
    recover(from_path = PATH.DEMO.value / PATH.CFG_JUEGOPLA.value,
            to_path   =                   PATH.CFG_JUEGOPLA.value)
    recover(from_path = PATH.DEMO.value / PATH.CFG_JUEGOPLA.value,
            to_path   =                   PATH.CFG_JUEGOPLA.value)
    recover(from_path = PATH.DEMO.value / PATH.CFG_MULTIP.value,
            to_path   =                   PATH.CFG_MULTIP.value)
    recover(from_path = PATH.DEMO.value / PATH.CFG_PUNTERIA.value,
            to_path   =                   PATH.CFG_PUNTERIA.value)
    recover(from_path = PATH.DEMO.value / PATH.CFG_RED.value,
            to_path   =                   PATH.CFG_RED.value)
    recover(from_path = PATH.DEMO.value / PATH.CFG_SONIDOS.value,
            to_path   =                   PATH.CFG_SONIDOS.value)

    # recover exe
    recover(from_path = PATH.ORIG.value / PATH.EXE.value,
            to_path   =                   PATH.EXE.value)

def set_wsfix():
    """
    Apply widescreen fix mod.

    Args:
        None
    
    Returns: 
        None

    """
    recover(from_path = PATH.WSFIX.value / PATH.EXE.value,
            to_path   =                    PATH.EXE.value)

    change_config_options(cfg_path = PATH.CFG_JUEGOPLA.value,
                          options  = {'fFOV': '90.000000'})

def set_noextview():
    """
    Apply no-external-view mod.

    Args:
        None
    
    Returns: 
        None

    """
    change_config_options(cfg_path = PATH.CFG_JUEGO.value,
                          options  = {'CameraExternaDistancia'    : '0.000000',
                                      'CameraExternaAnguloInicial': '0.000000',
                                      'CameraExternaAnguloMinimo' : '0.000000',
                                      'CameraExternaAnguloMaximo' : '0.000000',
                                      'CameraExternaIncFOV'       : '0.000000' })

def run_game():
    """
    Run the executable game file that corresponds to the widescreen fix, if active.
    
    Args:
        None

    Returns: 
        None

    Raises:
        FileNotFoundError: missing exe file to run the game

    """
    exe_path = PATH.HOME.value / PATH.EXE.value
    if Path.exists(exe_path):
        os.startfile(exe_path)
    else:
        raise FileNotFoundError(LOG.ERR_RUN_GAME.value)

def change_config_options(
    cfg_path: str,
    options : dict
):
    """
    Change configuration values for the files contained in the config folder.
    
    Args:
        cfg_path (str) : path of the config file
        options (dict) : dictionary containing option names and corresponding updated values.

    Returns: 
        None

    Raises:
        FileNotFoundError: missing config files to be updated

    """
    cfg_absolute_path = PATH.HOME.value / cfg_path

    if Path.exists(cfg_absolute_path):
        with open(cfg_absolute_path, 'r', encoding='utf-8') as handle:
            contents = handle.read()

        updated_contents = contents
        for option, value in options.items():
            pattern = fr'(\.{option}\s+)(\-?\d+(?:\.\d+)?|\(\s+\d+(?:\.\d+)?\s+\d+(?:\.\d+)?\s+\))'
            replacement = fr'\1 {value}'
            updated_contents = re.sub(pattern, replacement, updated_contents)

        with open(cfg_absolute_path, 'w', encoding='utf-8') as handle:
            handle.write(updated_contents)
    else:
        raise FileNotFoundError(LOG.ERR_CHANGE_CFG_FILE.value)
