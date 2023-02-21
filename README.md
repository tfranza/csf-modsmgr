# CSF Mods Manager v0.1

Companion application for the game "Commandos: Strike Force" under the Windows OS, while allowing:
- mods selection through a graphical interface
- transparent game data update, with respect to options selected
- restore of the original data, to keep integrity of the installed version 
- automatic choice of the executable file to be fired, according to the currently installed mods

Comes in handy to avoid compatibility issues between different game versions, while being robust to human errors during the data update.

## Featured Mods
- **Widescreen Fix**: Avoids in-game widescreen stretching for screens with 16:9 ratio.
- **No External View**: Sight reduction when external view is activated (toggled with E).

## Requirements
- Python 3.8
    - Tkinter 0.1.0
    - Pillow 9.4.0
    - Pyinstaller 5.8.0

## Installation
1. Use `pyinstaller.exe --onefile --noconsole --icon=modsmgr.ico ../path/to/csf-modsmgr-master/modsmgr.py` to build the project.
2. Copy in the home game folder: 
    - the "*modsmgr*" folder
    - the executable file "modsmgr.exe" generated in the "*dist*" folder
3. Run "*modsmgr.exe*" in game folder.

## Currently Known Issues
- The notification system will show "pending changes" even if a mod option is first selected and then deselected (which would result in no real change).

## Planned Mods
- **More Weapons**: Weapons selection from the full pool, for each character. Customization of rewards for promotion ranks. 
- **More Character Models**: Character models selection from the full pool, for each map.
- **Stamina Updater**: Changes how stamina works in terms of consumption and recovery, for each specific action.
- **No HUD**: Removes the HUD utterly, to allow a more realistic experience.
- **Better Menus**: Brand new selection of wallpapers and videos for modern menus.
