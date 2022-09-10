from pytube import YouTube
from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from pathlib import Path
import os

class MainWindow(Widget):

    name = ObjectProperty(None)
    message = ObjectProperty(None)

    def btn(self):
        vid = self.name.text 
        try:
            url = YouTube(vid)
            t = url.title
            print('Downloading')
            self.message.text = f'Downloading...... {t}'
            video = url.streams.get_highest_resolution()
            path_to_download_folder = str(os.path.join(Path.home(), "Videos"))
            video.download(path_to_download_folder)
        except:
            print('Omoooooo')
            self.message.text = f'Sorry, an error occured while downloading the file'

        self.message.text = f'{t} has been Downloaded successfully. Check you videos folder'



class Myapp(App):

    def build(self):
        return MainWindow()


if __name__ == '__main__':
    Myapp().run()



