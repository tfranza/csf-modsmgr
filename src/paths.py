"""Module storing any file/folder useful path."""

import os
from pathlib import Path
from enum import Enum

class PATH(Enum):
    """Enum class containing association between path variables and textual ones."""

    HOME = Path(os.getcwd())

    EXE = Path('CommXPC.exe')

    CFG = Path('config')
    CFG_CONTROL  = Path('config/Control.cfg')
    CFG_EDITOR   = Path('config/Editor.cfg')
    CFG_JUEGO    = Path('config/Juego.cfg')
    CFG_JUEGOPLA = Path('config/JuegoPla.cfg') 
    CFG_JUEGOVER = Path('config/JuegoVer.cfg')
    CFG_MULTIP   = Path('config/MultiP.cfg')
    CFG_PUNTERIA = Path('config/Punteria.cfg')
    CFG_RED      = Path('config/Red.cfg')
    CFG_SONIDOS  = Path('config/Sonidos.cfg')

    ORIG = Path('modsmgr/orig/')
    DEMO = Path('modsmgr/demo/')
    WSFIX = Path('modsmgr/wsfix/')

    RES_ICO   = Path('modsmgr/resources/modsmgr.ico')
    RES_CSF   = Path('modsmgr/resources/csf.png')
    RES_STATE = Path('modsmgr/resources/env.dat')
