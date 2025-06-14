# Disables multi-touch events to prevent unintended gestures or visual artifacts.
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,disable_multitouch')

# Import necessary Kivy modules and utilities for UI creation and cryptographic operations.
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.filechooser import FileChooserListView
from kivy.graphics import Rectangle, Color
from cryptography.fernet import Fernet
import os

# Importing custom cryptographic utilities from an external library.
from CryptoLib import crypto_util

# Define UI configuration variables for consistent styling across screens.
fontsize = 50  # Font size for labels and titles
h = 200        # Height of the title section
h2 = h         # Height of buttons
c = (255, 255, 255)  # Text color in RGB
r, g, b = 128, 128, 128  # Background color in RGB
rb, gb, bb = 128, 128, 128  # Button background color in RGB
bfont = 30     # Font size for button text
titlename = "ELH Encryptor"  # Application title

# Define the main menu screen of the app.
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self.build()

    def build(self):
        # Create a vertical BoxLayout for organizing widgets on the screen.
        layout = BoxLayout(orientation='vertical', padding=10, spacing=20)

        # Add background color to the screen using Kivy graphics instructions.
        with self.canvas.before:
            # Set background color to a neutral grey (RGB: 128,128,128).
            Color(r / 255, g / 255, b / 255, 1)  # RGB values normalized to [0, 1].
            self.rect = Rectangle(size=self.size, pos=self.pos)

        # Bind size and position updates to ensure the background adapts dynamically.
        self.bind(size=self.update_rect, pos=self.update_rect)

        # Add title label with a predefined font size and text color.
        titleM = Label(text=titlename, font_size=fontsize, halign='center', size_hint_y=None, height=h, color=c)
        layout.add_widget(titleM)

        # Create the "Folder" button with custom background color and styling.
        button_folder = Button(
            text='Folder',
            size_hint=(0.5, 0.1),
            pos_hint={'center_x': 0.5},
            background_normal="",  # Removes default button texture for consistent coloring.
            background_color=(rb / 255, gb / 255, bb / 255, 1),  # Button background color in RGBA.
            font_size=bfont,
            color=c  # Button text color matches the overall theme.
        )
        button_folder.bind(on_press=self.go_to_folder)  # Link button to folder screen transition.

        # Create the "File" button with similar styling as the folder button.
        button_file = Button(
            text='File',
            size_hint=(0.5, 0.1),
            pos_hint={'center_x': 0.5},
            background_normal="",
            background_color=(rb / 255, gb / 255, bb / 255, 1),
            font_size=bfont,
            color=c
        )
        button_file.bind(on_press=self.go_to_file)  # Link button to file screen transition.

        # Add buttons to the layout.
        layout.add_widget(button_folder)
        layout.add_widget(button_file)

        # Add the layout to the screen.
        self.add_widget(layout)

    def update_rect(self, *args):
        # Dynamically update the background rectangle's size and position.
        self.rect.size = self.size
        self.rect.pos = self.pos

    def go_to_folder(self, instance):
        # Transition to the folder screen when the folder button is pressed.
        self.manager.current = 'folder'

    def go_to_file(self, instance):
        # Transition to the file screen when the file button is pressed.
        self.manager.current = 'file'


# Visual UI for Folder Encryption Screen
class FolderScreen(Screen):
    def __init__(self, **kwargs):
        super(FolderScreen, self).__init__(**kwargs)
        self.build()

    def build(self):
        # Create a vertical BoxLayout to organize the screen elements.
        layout = BoxLayout(orientation='vertical', padding=10, spacing=20)

        # Add background color to the screen using Kivy's canvas instructions.
        with self.canvas.before:
            # Set the background color using predefined RGB values, normalized to [0, 1].
            Color(r / 255, g / 255, b / 255, 1)
            # Draw a rectangle to cover the entire screen for the background.
            self.rect = Rectangle(size=self.size, pos=self.pos)

        # Bind the size and position updates to ensure the background rectangle
        # resizes and repositions dynamically with the screen.
        self.bind(size=self.update_rect, pos=self.update_rect)

        # Add a title to the screen with custom font size and text color.
        titleFo = Label(text="Folder", font_size=fontsize, halign='center', size_hint_y=None, height=h2, color=c)
        layout.add_widget(titleFo)

        # Create an "Encrypt" button for folder encryption.
        button_encrypt = Button(
            text='Encrypt',
            size_hint=(0.5, 0.1), 
            pos_hint={'center_x': 0.5},
            background_normal="",  # Remove default texture for consistent custom background.
            background_color=(rb / 255, gb / 255, bb / 255, 1),  # Set the button background color.
            font_size=bfont,  # Button text font size.
            color=c  # Button text color.
        )
        # Bind the button to a lambda function to open the path screen with option 1.
        button_encrypt.bind(on_press=lambda x: self.open_path_screen(1))
        layout.add_widget(button_encrypt)

        # Create a "Decrypt" button for folder decryption with similar styling.
        button_decrypt = Button(
            text='Decrypt',
            size_hint=(0.5, 0.1),
            pos_hint={'center_x': 0.5},
            background_normal="",
            background_color=(rb / 255, gb / 255, bb / 255, 1),
            font_size=bfont,
            color=c
        )
        # Bind the button to a lambda function to open the path screen with option 3.
        button_decrypt.bind(on_press=lambda x: self.open_path_screen(3))
        layout.add_widget(button_decrypt)

        # Create a "Back to Menu" button to return to the main menu.
        button_back = Button(
            text='Back to Menu',
            size_hint=(0.5, 0.1),
            pos_hint={'center_x': 0.5},
            background_normal="",
            background_color=(rb / 255, gb / 255, bb / 255, 1),
            font_size=bfont,
            color=c
        )
        # Bind the button to the go_to_menu method for transitioning back to the menu screen.
        button_back.bind(on_press=self.go_to_menu)
        layout.add_widget(button_back)

        # Add the layout (containing title and buttons) to the screen.
        self.add_widget(layout)

    def update_rect(self, *args):
        # Update the background rectangle's size and position dynamically
        # whenever the screen's size or position changes.
        self.rect.size = self.size
        self.rect.pos = self.pos

    def open_path_screen(self, option):
        # Navigate to the path screen and pass the selected option.
        # Option determines whether the user chooses encryption or decryption.
        self.manager.get_screen('path').set_option(option)
        self.manager.current = 'path'

    def go_to_menu(self, instance):
        # Transition back to the main menu screen.
        self.manager.current = 'menu'


# Visual UI for File Encryption Screen
class FileScreen(Screen):
    def __init__(self, **kwargs):
        # Initialize the FileScreen class by calling the parent Screen constructor.
        super(FileScreen, self).__init__(**kwargs)
        self.build()

    def build(self):
        # Create a vertical BoxLayout to arrange widgets on the screen.
        layout = BoxLayout(orientation='vertical', padding=10, spacing=20)

        # Add background color to the screen using canvas instructions.
        with self.canvas.before:
            # Set the background color using RGB values, normalized to the range [0, 1].
            Color(r / 255, g / 255, b / 255, 1)
            # Draw a rectangle to represent the background.
            self.rect = Rectangle(size=self.size, pos=self.pos)

        # Dynamically update the background rectangle's size and position
        # whenever the screen's size or position changes.
        self.bind(size=self.update_rect, pos=self.update_rect)

        # Add a title label with custom font size and alignment to the layout.
        titleFi = Label(
            text="File",
            font_size=fontsize,
            halign='center',
            size_hint_y=None,
            height=h2
        )
        layout.add_widget(titleFi)

        # Create an "Encrypt" button for file encryption.
        button_encrypt = Button(
            text='Encrypt',
            size_hint=(0.5, 0.1),
            pos_hint={'center_x': 0.5},
            background_normal="",  # Remove default texture for consistent custom background.
            background_color=(rb / 255, gb / 255, bb / 255, 1),  # Button background color.
            font_size=bfont,  # Font size for button text.
            color=c  # Button text color.
        )
        # Bind the button to the function for opening the path screen with option 2.
        button_encrypt.bind(on_press=lambda x: self.open_path_screen(2))
        layout.add_widget(button_encrypt)

        # Create a "Decrypt" button for file decryption with similar styling.
        button_decrypt = Button(
            text='Decrypt',
            size_hint=(0.5, 0.1),
            pos_hint={'center_x': 0.5},
            background_normal="",
            background_color=(rb / 255, gb / 255, bb / 255, 1),
            font_size=bfont,
            color=c
        )
        # Bind the button to the function for opening the path screen with option 4.
        button_decrypt.bind(on_press=lambda x: self.open_path_screen(4))
        layout.add_widget(button_decrypt)

        # Create a "Back to Menu" button to navigate back to the main menu.
        button_back = Button(
            text='Back to Menu',
            size_hint=(0.5, 0.1),
            pos_hint={'center_x': 0.5},
            background_normal="",
            background_color=(rb / 255, gb / 255, bb / 255, 1),
            font_size=bfont,
            color=c
        )
        # Bind the button to the function for returning to the main menu screen.
        button_back.bind(on_press=self.go_to_menu)
        layout.add_widget(button_back)

        # Add the layout (containing title and buttons) to the screen.
        self.add_widget(layout)

    def update_rect(self, *args):
        # Dynamically update the size and position of the background rectangle
        # whenever the screen's dimensions or position change.
        self.rect.size = self.size
        self.rect.pos = self.pos

    def open_path_screen(self, option):
        # Navigate to the path screen and set the operation option.
        # Option 2 indicates encryption, and option 4 indicates decryption.
        self.manager.get_screen('path').set_option(option)
        self.manager.current = 'path'

    def go_to_menu(self, instance):
        # Transition back to the main menu screen.
        self.manager.current = 'menu'


class EnterPath(Screen):
    def __init__(self, **kwargs):
        # Initialize the EnterPath class and set up the required variables.
        super(EnterPath, self).__init__(**kwargs)
        self.option = None  # Stores the encryption/decryption option selected by the user.
        self.build()

    def build(self):
        # Create a vertical BoxLayout to organize widgets on the screen.
        layout = BoxLayout(orientation='vertical', padding=10, spacing=20)

        # Add background color to the screen using canvas instructions.
        with self.canvas.before:
            # Set the background color using RGB values, normalized to [0, 1].
            Color(r / 255, g / 255, b / 255, 1)
            # Draw a rectangle to represent the background.
            self.rect = Rectangle(size=self.size, pos=self.pos)

        # Dynamically update the background rectangle's size and position
        # whenever the screen's size or position changes.
        self.bind(size=self.update_rect, pos=self.update_rect)

        # Add label prompting the user to enter a path.
        file_label = Label(
            text="Enter path:",
            size_hint=(1, 0.2),
            font_size=30,
            color=c  # Text color.
        )
        layout.add_widget(file_label)

        # Create a TextInput widget for manual path entry.
        self.input = TextInput(hint_text="Path", multiline=False, size_hint=(1, 0.2))
        layout.add_widget(self.input)

        # Add a label for the FileChooser visual.
        button_chooser = Label(
            text='Visual Select',
            size_hint=(1, 0.2),
            font_size=30,
            color=c  # Text color.
        )
        layout.add_widget(button_chooser)

        # Add a FileChooser widget allowing users to select files or folders.
        
        self.filechooser = FileChooserListView(dirselect=True)  # Enable directory selection.
        self.filechooser.filters = ["!DumpStack.log.tmp", "!hiberfil.sys", "!pagefile.sys", "!swapfile.sys"]
        layout.add_widget(self.filechooser)

        # Create a "Process" button to execute encryption/decryption.
        button_process = Button(
            text='Process',
            size_hint=(0.5, 0.1),
            pos_hint={'center_x': 0.5},
            background_normal="",  # Remove default texture for consistent custom background.
            background_color=(rb / 255, gb / 255, bb / 255, 1),
            font_size=bfont,
            color=c  # Button text color.
        )
        button_process.bind(on_press=self.process)  # Bind button to the process method.
        layout.add_widget(button_process)

        # Create a "Back" button to return to the main menu.
        button_back = Button(
            text='Back',
            size_hint=(0.5, 0.1),
            pos_hint={'center_x': 0.5},
            background_normal="",
            background_color=(rb / 255, gb / 255, bb / 255, 1),
            font_size=bfont,
            color=c
        )
        button_back.bind(on_press=self.go_to_menu)  # Bind button to the method for navigation.
        layout.add_widget(button_back)

        # Add the layout (containing labels, buttons, and FileChooser) to the screen.
        self.add_widget(layout)

    def update_rect(self, *args):
        # Update the size and position of the background rectangle dynamically
        # whenever the screen's dimensions or position change.
        self.rect.size = self.size
        self.rect.pos = self.pos

    def set_option(self, option):
        # Set the option indicating whether to encrypt/decrypt a file or folder.
        # Option values: 1 (encrypt folder), 2 (encrypt file),
        # 3 (decrypt folder), 4 (decrypt file).
        self.option = option

    def should_ignore_file(self, filename):
        ignored_files = ["DumpStack.log.tmp", "hiberfil.sys", "pagefile.sys", "swapfile.sys"]
        return any(file in filename for file in ignored_files)

    def process(self, instance):

        if self.input.text.strip():
            path = self.input.text.strip()  # Use manually entered path if provided.
        elif self.filechooser.selection:
            path = self.filechooser.selection[0]  # Use FileChooser selection if no manual path is provided.
            
            # **Check if selected file is one of the ignored system files**
            if self.should_ignore_file(os.path.basename(path)):
                error_screen = self.manager.get_screen('error')
                error_screen.update_message("Error: Selected file is restricted by the OS.")
                self.manager.current = 'error'
                return
        else:
            error_screen = self.manager.get_screen('error')
            error_screen.update_message("Error: No file or path selected.")
            self.manager.current = 'error'
            return

        # Continue with encryption/decryption
        key = crypto_util.generate_key() if self.option in [1, 2] else crypto_util.load_key()
        success = False

        if self.option == 1:
            success = crypto_util.encrypt_folder(path, key)
            message = "Encrypted Folder" if success else "Failed to Encrypt Folder"
        elif self.option == 2:
            success = crypto_util.encrypt_file(path, key)
            message = "Encrypted File" if success else "Failed to Encrypt File"
        elif self.option == 3:
            success = crypto_util.decrypt_folder(path, key)
            message = "Decrypted Folder" if success else "Failed to Decrypt Folder"
        elif self.option == 4:
            success = crypto_util.decrypt_file(path, key)
            message = "Decrypted File" if success else "Failed to Decrypt File"

        error_screen = self.manager.get_screen('error')
        error_screen.update_message(message)
        self.manager.current = 'error'

        self.input.text = ""  # Clear input after processing.

    def go_to_menu(self, instance):
        # Navigate back to the main menu screen.
        self.manager.current = 'menu'


class ErrorMessage(Screen):
    def __init__(self, **kwargs):
        super(ErrorMessage, self).__init__(**kwargs)
        self.message_label = None
        self.build()

    def build(self):
        # Create a vertical BoxLayout to organize widgets on the screen.
        layout = BoxLayout(orientation='vertical', padding=10, spacing=20)

        # Add background color to the screen using canvas instructions.
        with self.canvas.before:
            # Set the background color using RGB values, normalized to [0, 1].
            Color(r / 255, g / 255, b / 255, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        # Bind the size and position of the background rectangle to the screen.
        self.bind(size=self.update_rect, pos=self.update_rect)

        # Add a label to display the error message
        self.message_label = Label(
            text="",
            size_hint=(1, 0.8),  # Larger space for the message
            font_size=30,
            color=c  # Text color.
        )
        layout.add_widget(self.message_label)

        # Create a "Back to Menu" button to return to the main menu.
        button_back = Button(
            text="Back to Menu",
            size_hint=(0.5, 0.1),
            pos_hint={'center_x': 0.5},
            background_normal="",
            background_color=(rb / 255, gb / 255, bb / 255, 1),
            font_size=bfont,
            color=c
        )
        button_back.bind(on_press=self.go_to_menu)
        layout.add_widget(button_back)

        # Add the layout to the screen.
        self.add_widget(layout)

    def update_rect(self, *args):
        # Ensure the background rectangle updates dynamically with the screen.
        self.rect.size = self.size
        self.rect.pos = self.pos

    def update_message(self, message):
        # Update the displayed message dynamically.
        self.message_label.text = message

    def go_to_menu(self, instance):
        # Navigate back to the main menu screen.
        self.manager.current = 'menu'

# Visual UI Sequence for Screen Management
class EncryptApp(App):
    def build(self):
        # Set up the ScreenManager and add all screens to the application.
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))  # Main menu screen.
        sm.add_widget(FolderScreen(name='folder'))  # Folder encryption/decryption screen.
        sm.add_widget(FileScreen(name='file'))  # File encryption/decryption screen.
        sm.add_widget(EnterPath(name='path'))  # Screen for entering the path.
        sm.add_widget(ErrorMessage(name='error'))
        return sm

# Entry point for running the application.
if __name__ == '__main__':
    EncryptApp().run()

