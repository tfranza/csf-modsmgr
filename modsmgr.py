"""Main GUI Module."""

from tkinter import Tk, Frame
from tkinter import Label, Button, Checkbutton
from tkinter import IntVar
from PIL import ImageTk, Image

from src import mods
from src.paths import PATH
from src.logs import LOG

class GUI:
    """GUI of the Mod Manager."""

    # GUI root ref
    root : Tk

    # frames
    f_config : Frame
    f_footer : Frame

    # widgets
    l_csf_img  : Label
    b_wsfix    : Button
    b_no_ext_v : Button
    b_apply    : Button
    b_run      : Button
    l_logger   : Label

    def __init__(self,
        gui_title: str = 'CSF Mods',
        gui_size : str = '320x105'
    ):
        """
        Constructor method to initialize gui root reference, frames and widgets
        
        Args:
            gui_title (str) : text that will appear in the title bar
            gui_size  (str) : size of the window application

        Returns: 
            None
        
        """
        # initializing GUI frames
        self.gui = Tk()
        self.gui.title(gui_title)
        self.gui.geometry(gui_size)
        self.gui.resizable(width=False, height=False)
        self.gui.iconbitmap(PATH.RES_ICO.value)

        self.f_config = Frame(self.gui)
        self.f_config.pack(padx=5, pady=5)

        self.f_footer = Frame(self.gui)
        self.f_footer.pack(padx=14)

        ws_fix_on      = IntVar()      # hold content of mods choices
        no_ext_view_on = IntVar()

        # creating widgets
        img = ImageTk.PhotoImage(Image.open(PATH.RES_CSF.value))
        self.l_csf_img = Label(
            self.f_config,
            image    = img,
            anchor   = 'w'
        )
        self.b_wsfix = Checkbutton(
            self.f_config,
            text     = 'Widescreen Fix',
            width    = 13,
            anchor   = 'w',
            variable = ws_fix_on,
            command  = self.add_pending_mod
        )
        self.b_no_ext_v = Checkbutton(
            self.f_config,
            text     = 'No External View',
            width    = 13,
            anchor   = 'w',
            variable = no_ext_view_on,
            command  = self.add_pending_mod
        )
        self.b_apply = Button(
            self.f_config,
            text    = 'APPLY',
            width   = 10,
            justify = 'center',
            command = lambda: self.apply_mods(ws_fix_on.get(), no_ext_view_on.get())
        )
        self.b_run = Button(
            self.f_config,
            text    = 'RUN',
            width   = 10,
            justify = 'center',
            command = lambda: self.play_game(ws_fix_on.get())
        )
        self.l_logger = Label(
            self.f_footer,
            text        = LOG.BASE_CFG.value,
            width       = 41 ,
            anchor      = 'w',
            borderwidth = 2,
            relief      = 'groove'
        )

        # putting widgets in the interface
        self.l_csf_img .grid(row=0, column=0, rowspan=2)
        self.b_wsfix   .grid(row=0, column=1, padx=15)
        self.b_no_ext_v.grid(row=1, column=1)
        self.b_apply   .grid(row=0, column=2)
        self.b_run     .grid(row=1, column=2)
        self.l_logger.pack()

        # run the interface loop
        self.gui.mainloop()


    # creating button functions
    def apply_mods(self,
        ws_fix  : bool,
        no_ext_v: bool
    ):
        """
        Widget function that applies config mods onto original data.
        
        Args:
            ws_fix   (bool) : widescreen fix mod is active
            no_ext_v (bool) : no_ext_view    mod is active

        Returns: 
            str: Notification message regarding the result of the mods application
        
        """
        # Restores original config files. If error is fired, logs it.
        if (error_msg := mods.set_cfg_orig()):
            self.log(LOG.ERR_CFG_ORIG.value + error_msg)
            return

        # Applies the widescreen-fix mod, if required. If error is fired, logs it.
        if ws_fix and (error_msg := mods.set_wsfix()):
            self.log(LOG.ERR_CFG_WSFIX.value + error_msg)
            return

        # Applies the no-ext-view mod, if required. If error is fired, logs it.
        if no_ext_v and (error_msg := mods.set_no_ext_view()):
            self.log(LOG.ERR_CFG_NOEXTV.value + error_msg)
            return

        self.b_apply.config(state='disabled')
        self.b_run.config(state='normal')

        # Logs a successful event corresponding to the required (and activated) mods.
        if ws_fix and no_ext_v:
            self.log(LOG.OK_CFG_WSFIX_NOEXTV.value)
        elif ws_fix:
            self.log(LOG.OK_CFG_WSFIX.value)
        elif no_ext_v:
            self.log(LOG.OK_CFG_NOEXTV.value)
        else:
            self.log(LOG.OK_CFG_ORIG.value)

    def play_game(self,
        ws_fix: bool
    ):
        """
        Run the game.
        
        Args:
            ws_fix (bool) : widescreen fix mod is active

        Returns:
            None
        """
        error_msg = mods.run_game(ws_fix)
        if error_msg:
            self.log(error_msg)
        else:
            self.gui.destroy()

    def add_pending_mod(self):
        """
        Flag the presence of at least one new pending change.
        
        Args:
            None

        Returns:
            None
        """
        self.b_apply.config(state='normal')
        self.b_run.config(state='disabled')
        self.log(LOG.BASE_PENDING_CHANGE.value)


    def log(self,
        message: str
    ):
        """
        Update the logger label with a new notification message.
        
        Args:
            message (str): Notification message

        Returns:
            None
        """
        self.l_logger.config(text = message)

if __name__ == '__main__':
    GUI()
