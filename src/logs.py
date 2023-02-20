"""Module storing any message to be printed by the logger."""

from enum import Enum

class LOG(Enum):
    """Enum class containing association between descriptive variables and textual messages."""

    BASE_CFG = 'Know nothing of current cfg. Can change it though.'
    BASE_PENDING_CHANGE = 'Pending changes...'

    # Error messages
    ERR_BAK_NOBAK  = 'No backup found.'
    ERR_BAK_NOORIG = 'No original data found.'
    ERR_BAK_DELETE = 'Can\'t find path to be deleted.'
    ERR_BAK_COPY   = 'Can\'t find path to be copied.'
    ERR_BAK_RENAME = 'Can\'t find path to be renamed.'

    ERR_CFG_ORIG   = 'Can\'t reset original config. '
    ERR_CFG_WSFIX  = 'Can\'t apply widescreen-fix. '
    ERR_CFG_NOEXTV = 'Can\'t apply no-ext-view. '
    ERR_CFG_NO_DIR = 'Can\'t find source folder.'

    ERR_RUN_GAME   = 'Can\'t run the game. Exe not found in predefined path.'

    # Success messages
    OK_CFG_ORIG         = 'Restored original config!'
    OK_CFG_WSFIX        = 'Widescreen fix active!'
    OK_CFG_NOEXTV       = 'No-external-view active!'
    OK_CFG_WSFIX_NOEXTV = 'Widescreen fix and No-external-view active!'
