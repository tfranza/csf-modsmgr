"""Module storing any file/folder useful path."""

import os
from pathlib import Path
from enum import Enum

class PATH(Enum):
    """Enum class containing association between path variables and textual ones."""

    HOME = Path(os.getcwd())
    CFG  = Path('config')

    EXE_4_3   = Path('CommXPC.exe')
    EXE_16_9  = Path('CommXPC_16x9.exe')

    CFG_ORIG  = Path('modsmgr/mods/original_config')
    CFG_DEMO  = Path('modsmgr/mods/demo_config')
    CFG_WSFIX = Path('modsmgr/mods/widescreen_fix')
    CFG_EXTV  = Path('modsmgr/mods/no_external_view')

    RES_ICO   = Path('modsmgr/resources/modsmgr.ico')
    RES_CSF   = Path('modsmgr/resources/csf.png')
    RES_STATE = Path('modsmgr/resources/env.dat')
