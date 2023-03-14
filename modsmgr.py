"""Main GUI Module."""

from tkinter import Tk, Frame
from tkinter import Label, Button, Checkbutton
from tkinter import IntVar
from PIL import ImageTk, Image

from src import mods
from src.paths import PATH
from src.logs import LOG
from src.env import Environment

class GUI:
    """GUI of the Mod Manager."""

    # Current state
    env: Environment

    # GUI root ref
    root : Tk

    # frames
    f_config : Frame
    f_footer : Frame

    # widgets
    l_csf_img  : Label
    b_wsfix    : Button
    b_noextv : Button
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
        # initializing environment
        self.env = Environment()

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

        ws_fix_on    = IntVar()      # hold content of mods choices
        noextview_on = IntVar()

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
        self.b_noextv = Checkbutton(
            self.f_config,
            text     = 'No External View',
            width    = 13,
            anchor   = 'w',
            variable = noextview_on,
            command  = self.add_pending_mod
        )
        self.b_apply = Button(
            self.f_config,
            text    = 'APPLY',
            width   = 10,
            justify = 'center',
            command = lambda: self.apply_mods(ws_fix_on.get(), noextview_on.get())
        )
        self.b_run = Button(
            self.f_config,
            text    = 'RUN',
            width   = 10,
            justify = 'center',
            command = lambda: self.play_game()
        )
        self.l_logger = Label(
            self.f_footer,
            text        = LOG.INIT.value,
            width       = 41 ,
            anchor      = 'w',
            borderwidth = 2,
            relief      = 'groove'
        )
        self.load_environment()

        # putting widgets in the interface
        self.l_csf_img .grid(row=0, column=0, rowspan=2)
        self.b_wsfix   .grid(row=0, column=1, padx=15)
        self.b_noextv  .grid(row=1, column=1)
        self.b_apply   .grid(row=0, column=2)
        self.b_run     .grid(row=1, column=2)
        self.l_logger.pack()

        # run the interface loop
        self.gui.mainloop()

    def load_environment(self):
        """
        Load the state of the environment.
        
        Args:
            None

        Returns: 
            None
        
        """
        try:
            self.env.load_state()
        except FileNotFoundError as err:
            self.log(str(err))

        if self.env.wsfix() > 0:
            self.b_wsfix.select()

        if self.env.noextv() > 0:
            self.b_noextv.select()


    # creating button functions
    def apply_mods(self,
        wsfix : bool,
        noextv: bool
    ):
        """
        Widget function that applies config mods onto original data.
        
        Args:
            wsfix  (bool) : widescreen fix mod is active
            noextv (bool) : no external view mod is active

        Returns: 
            str: Notification message regarding the result of the mods application
        
        """
        # Restores original config files. If error is fired, logs it.
        try:
            mods.set_cfg_orig()
        except FileNotFoundError as err:
            self.log(LOG.ERR_CFG_ORIG.value + str(err))
            return
        self.env.enable('cfg_orig')
        self.env.disable('mod_wsfix')
        self.env.disable('mod_noextv')

        # Applies the widescreen-fix mod, if required. If error is fired, logs it.
        if wsfix:
            try:
                mods.set_wsfix()
            except FileNotFoundError as err:
                self.log(LOG.ERR_CFG_WSFIX.value + str(err))
                return
            self.env.disable('cfg_orig')
            self.env.enable('mod_wsfix')

        # Applies the no-ext-view mod, if required. If error is fired, logs it.
        if noextv:
            try:
                mods.set_noextview()
            except FileNotFoundError as err:
                self.log(LOG.ERR_CFG_NOEXTV.value + str(err))
                return
            self.env.disable('cfg_orig')
            self.env.enable('mod_noextv')

        # Saves environment. If error is fired, logs it.
        try:
            self.env.save_state()
        except FileNotFoundError as err:
            self.log(str(err))
            print(str(err))
            return

        # updating buttons availability
        self.b_apply.config(state='disabled')
        self.b_run.config(state='normal')

        # Logs a successful event corresponding to the required (and activated) mods.
        if wsfix and noextv:
            self.log(LOG.OK_CFG_WSFIX_NOEXTV.value)
        elif wsfix:
            self.log(LOG.OK_CFG_WSFIX.value)
        elif noextv:
            self.log(LOG.OK_CFG_NOEXTV.value)
        else:
            self.log(LOG.OK_CFG_ORIG.value)

    def play_game(self):
        """
        Run the game.
        
        Args:
            None

        Returns:
            None
        """
        try:
            mods.run_game()
            self.gui.destroy()
        except FileNotFoundError as err:
            self.log(str(err))

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
        self.log(LOG.PENDING_CHANGES.value)


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
