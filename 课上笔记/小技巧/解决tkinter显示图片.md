```
from tkinter import Tk, PhotoImage, Label
from threading import Thread
import time

from PIL import Image

class Animation:
    def __init__(self, gif_file):
        self.root = Tk()

        self.file_name = gif_file
        self.fill_animate()

        self.label = Label(self.root)
        self.label.pack()

    def fill_animate(self):
        pil_image = Image.open(self.file_name)
        self.num_photos = pil_image.n_frames
        self.photos = [PhotoImage(file=self.file_name, format='gif -index {0}'.format(i)) for i in range(self.num_photos)]

    def display_photo(self, idx):
        idx = idx % self.num_photos
        photo = self.photos[idx]
        self.label.config(image=photo)

    def display_animation(self):
        idx = 0
        while True:
            idx += 1
            self.display_photo(idx)
            time.sleep(0.1)

    def start_thread(self):
        thread_animation = Thread(target=self.display_animation, daemon=True)
        thread_animation.start()

if __name__ == '__main__':
    animate = Animation('abc.gif')
    animate.start_thread()
    animate.root.mainloop()
```

