"""Module that contains helper backup functions."""

import shutil
import os
from pathlib import Path

from .paths import PATH

def backup(
    from_path: str,
    to_path  : str = None,
    copy     : bool = True
) -> str:
    """
    Makes a backup of original data (file/folder).
    
    Args:
        from_path (str)  : relative path of original data
        to_path   (str)  : relative path of the backup
        copy      (bool) : defines if original data should be copied or moved to the backup location

    Returns: 
        str: success/failure message
    
    """
    if not to_path:
        to_path = from_path / '.bak'

    print(f'> Creating backup of "{from_path}" to "{to_path}"...')

    # shutil requires absolute paths instead of relative ones
    from_path = PATH.HOME.value / from_path
    to_path   = PATH.HOME.value / to_path

    error_msg = None
    if Path.exists(from_path):
        # remove existing backups
        if Path.exists(to_path):
            __delete_path__(to_path)

        # create the backup
        if copy:
            __copy_path__(from_path, to_path)       # keep both original and backup
        else:
            __rename_path__(from_path, to_path)     # rename original into backup
    else:
        error_msg = 'No original data found.'

    return error_msg

def recover(
    to_path  : str,
    from_path: str = None,
    copy     : bool = True
) -> str:
    """
    Recovers original data (file/folder) from a backup.
    
    Args:
        to_path   (str)  : relative path of recovered data
        from_path (str)  : relative path of the backup
        copy      (bool) : defines if backup should be copied or moved to the recovery location

    Returns: 
        str: success/failure message

    """
    if not from_path:
        from_path = to_path / '.bak'

    print(f'> Recovering "{to_path}" from "{from_path}"...')

    # shutil requires absolute paths instead of relative ones
    from_path = PATH.HOME.value / from_path
    to_path   = PATH.HOME.value / to_path

    error_msg = None
    if Path.exists(from_path):
        # remove existing recovered data
        if Path.exists(to_path):
            __delete_path__(to_path)

        # recover from the backup
        if copy:
            __copy_path__(from_path, to_path)      # keep both backup and recovered
        else:
            __rename_path__(from_path, to_path)    # rename the backup into recovered
    else:
        error_msg = 'No backup found.'

    return error_msg

####################          Utility functions          ####################

def __delete_path__(
    from_path: str
) -> str:
    """
    Utility function, used by backup and recover, to delete data (file/folder).
    
    Args:
        from_path (str) : relative path of data (files/folder) to be deleted

    Returns: 
        str: success/failure message.
    
    """
    error_msg = None
    if Path.exists(from_path):
        if Path.is_dir(from_path):
            shutil.rmtree(from_path)
        else:
            os.chmod(from_path, 0o777)
            os.unlink(from_path)
    else:
        error_msg = 'Can\'t find path to be deleted.'

    return error_msg

def __copy_path__(
    from_path: str,
    to_path  : str
) -> str:
    """
    Utility function, used by backup and recover, to copy data (file/folder).
    
    Args:
        from_path (str) : relative path of data to be copied
        to_path   (str) : relative path of copied data 

    Returns: 
        str: success/failure message.
    
    """
    error_msg = None
    if Path.exists(from_path):
        if Path.is_dir(from_path) and Path.is_dir(to_path):
            shutil.copytree(from_path, to_path)
        else:
            shutil.copy2(from_path, to_path)
    else:
        error_msg = 'Can\'t find path to be copied.'

    return error_msg

def __rename_path__(
    from_path: str,
    to_path  : str
) -> str:
    """
    Utility function, used by backup and recover, to rename data (file/folder).
    
    Args:
        from_path (str) : relative path of data to be renamed
        to_path   (str) : relative path of renamed data 

    Returns: 
        str: success/failure message.
    
    """
    error_msg = None
    if Path.exists(from_path):
        if Path.exists(to_path):
            __delete_path__(to_path)
        from_path.rename(to_path)
    else:
        error_msg = 'Can\'t find path to be renamed.'

    return error_msg
