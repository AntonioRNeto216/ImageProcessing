import os
import tkinter
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox

from .application import Application


class ApplicationGUI:
    """
    ApplicationGUI manage all user interface logic and style.
    """
    
    def __init__(self) -> None:
        """
        Defines a bunch of attributes and calls some methods to build the interface.\n
        Note: an Application object is an attribute of the ApplicationGUI.
        """
        self._application = Application()
        self._application_gui = tkinter.Tk()

        self._is_increase_brightness_on = tkinter.BooleanVar(value=False)
        self._is_gaussian_kernel_size_on = tkinter.BooleanVar(value=False)
        self._is_video_on = tkinter.BooleanVar(value=False)
        self._is_camera_on = tkinter.BooleanVar(value=False)
        self._video_path = None

        self._frames_background = 'white smoke'
        self._frames_label_font = ("Arial", 12)
        self._entry_label_font = ("Arial", 8)
        self._init_text_choose_video = 'Choose Video'
        self._init_dir_browse_file = f'{os.getcwd()}/videos/'

        self._screen_config()
        self._gui_frame1()
        self._gui_frame2()
        self._gui_confirm_button()

    def init_gui(self) -> None:
        """
        Call the application_gui mainloop.
        """
        self._application_gui.mainloop()

    def _screen_config(self) -> None:
        """
        Defines the window title, background color, geometry and if is resizable.
        """
        self._application_gui.title('Image Processing')
        self._application_gui.configure(background='white')
        self._application_gui.geometry('640x480')
        self._application_gui.resizable(False, False)

    def _gui_frame1(self) -> None:
        """
        Sets all labels, check buttons and entries for frame1.
        """
        self._frame1 = tkinter.Frame(self._application_gui)
        self._frame1.configure(background=self._frames_background)
        self._frame1.place(
            relx=0.05, 
            rely=0.05, 
            relwidth=0.90, 
            relheight=0.40
        )

        self._label_frame1 = tkinter.Label(
            self._frame1, 
            text='Image Modifiers', 
            background=self._frames_background, 
            font=self._frames_label_font
        )
        self._label_frame1.place(
            relx=0.0, 
            rely=0.02, 
            relwidth=1
        )

        self._checkbox_increase_brightness_entry = tkinter.Checkbutton(
            self._frame1, 
            background=self._frames_background, 
            variable=self._is_increase_brightness_on, 
            onvalue=True, 
            offvalue=False
        )
        self._checkbox_increase_brightness_entry.place(
            relx=0.025, 
            rely=0.38
        )

        self._label_increase_brightness_entry = tkinter.Label(
            self._frame1, 
            text='Brightness (0 to 255)', 
            background=self._frames_background, 
            font=self._entry_label_font
        )
        self._label_increase_brightness_entry.place(
            relx=0.08, 
            rely=0.30
        )

        self._increase_brightness_entry = tkinter.Entry(self._frame1)
        self._increase_brightness_entry.place(
            relx=0.08, 
            rely=0.38
        )

        self._checkbox_gaussian_kernel_size_entry = tkinter.Checkbutton(
            self._frame1, 
            background=self._frames_background, 
            variable=self._is_gaussian_kernel_size_on, 
            onvalue=True, 
            offvalue=False
        )
        self._checkbox_gaussian_kernel_size_entry.place(
            relx=0.025, 
            rely=0.68
        )

        self._label_gaussian_kernel_size_entry = tkinter.Label(
            self._frame1, 
            text='Kernel Size (Only odd numbers)', 
            background=self._frames_background, 
            font=self._entry_label_font
        )
        self._label_gaussian_kernel_size_entry.place(
            relx=0.08, 
            rely=0.60
        )

        self._gaussian_kernel_size_entry = tkinter.Entry(self._frame1)
        self._gaussian_kernel_size_entry.place(
            relx=0.08, 
            rely=0.68
        )
    
    def _gui_frame2(self) -> None:
        """
        Sets all labels, check buttons and entries for frame2.
        """
        self._frame2 = tkinter.Frame(self._application_gui)
        self._frame2.configure(background=self._frames_background)
        self._frame2.place(
            relx=0.05, 
            rely=0.50, 
            relwidth=0.90, 
            relheight=0.40
        )

        self._label_frame2 = tkinter.Label(
            self._frame2, 
            text='Capture Source', 
            background=self._frames_background, 
            font=self._frames_label_font
        )
        self._label_frame2.place(
            relx=0.0, 
            rely=0.02, 
            relwidth=1
        )

        self._checkbox_camera = tkinter.Checkbutton(
            self._frame2, 
            background=self._frames_background, 
            variable=self._is_camera_on, 
            onvalue=True, 
            offvalue=False,
            text='Camera'
        )
        self._checkbox_camera.place(
            relx=0.025, 
            rely=0.38
        )

        self._checkbox_video = tkinter.Checkbutton(
            self._frame2, 
            background=self._frames_background, 
            variable=self._is_video_on, 
            onvalue=True, 
            offvalue=False,
        )
        self._checkbox_video.place(
            relx=0.025, 
            rely=0.625
        )

        self._choose_video_button = tkinter.Button(
            self._frame2, 
            text=self._init_text_choose_video,
            bd=2,
            command=self._browse_files
        )
        self._choose_video_button.place(
            relx=0.08, 
            rely=0.60
        )

    def _browse_files(self) -> None:
        """
        Opens a file dialog to choose a video.\n
        This method is a trigger for the choose video button.
        """
        self._video_path = filedialog.askopenfilename(
            initialdir=self._init_dir_browse_file, 
            title=self._init_text_choose_video,
            filetypes=(('MP4', '*.mp4'),)
        )
        self._choose_video_button.configure(text=f'File: {self._video_path.replace(self._init_dir_browse_file, "")}')

    def _gui_confirm_button(self) -> None:
        """
        Sets confirm button configurations.
        """
        self._confirm_button = tkinter.Button(
            self._application_gui, 
            text='Confirm', 
            font=self._frames_label_font, 
            bd=2,
            command=self._onclick_confirm
        )
        self._confirm_button.place(
            relx=0.05, 
            rely=0.925, 
            relwidth=0.9, 
            relheight=0.05
        )
    
    def _onclick_confirm(self) -> None:
        """
        Execute a lot of validations to call init application (Application method).
        After execution the function clear all Entries and CheckButtons.
        """
        increase_brightness_value = int(self._increase_brightness_entry.get()) if self._is_increase_brightness_on.get() else None
        if increase_brightness_value is not None and not 0 <= increase_brightness_value <= 255:
            messagebox.showinfo('INFO', 'Brightness value must be between 0 and 255.')
            return
        
        gaussian_blur_kernel = int(self._gaussian_kernel_size_entry.get()) if self._is_gaussian_kernel_size_on.get() else None
        if gaussian_blur_kernel is not None and gaussian_blur_kernel % 2 == 0:
            messagebox.showinfo('INFO', 'Gaussian Kernel Size must be an odd number.')
            return

        if self._is_camera_on.get() and self._is_video_on.get():
            messagebox.showinfo('INFO', 'It\'s not possible to choose two capture sources.')
            return
        elif not self._is_camera_on.get() and not self._is_video_on.get():
            messagebox.showinfo('INFO', 'Choose one capture source.')
            return
        elif self._is_camera_on.get():
            self._application.init_application(increase_brightness_value, gaussian_blur_kernel)
        elif self._is_video_on.get() and self._video_path is not None:
            self._application.init_application(increase_brightness_value, gaussian_blur_kernel, video_path=self._video_path)
        else:
            messagebox.showinfo('INFO', 'Choose a video.')
            return

        self._is_increase_brightness_on.set(value=False)
        self._increase_brightness_entry.delete(0, 'end')

        self._is_gaussian_kernel_size_on.set(value=False)
        self._gaussian_kernel_size_entry.delete(0, 'end')

        self._is_video_on.set(value=False)
        self._is_camera_on.set(value=False)

        self._choose_video_button.configure(text=self._init_text_choose_video)
        self._video_path = None