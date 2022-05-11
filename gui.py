from unigui import UniGui
from unigui.widget import TextWidget
from unigui.pygamedisplay import PygameDisplay
from unigui.colorscheme import Solarized, VSCode
import time

WIDTH = 320
HEIGHT = 240
CS = VSCode.dark

# TODO: Here is where we need to create the object that represents our "display"
# This is the screen where we want our graphical user interface (GUI) to appear.
display = ...

gui = UniGui(WIDTH, HEIGHT, colorscheme=CS)

tw = TextWidget("tw", 0, 0, WIDTH, HEIGHT, colorscheme=CS)
tw.set_value("hello world!")
gui.add_widget(tw)

display.show(gui)

while True:
    display.refresh()
    click = display.get_mouse_clicks()
    if click:
        print(click)
    time.sleep(0.2)

git add .
git commit -m "Added PygameDisplay object"
git push origin main

    git checkout -b rpi-spi-display

    pip install adafruit_ili9341

    display = adafruit_ili9341.ILI9341(display_bus,
                                       width=320,
                                       height=240)

    adafruit_bitmap_font/
    adafruit_display_shapes/
    adafruit_display_text/
    adafruit_imageload/
    adafruit_ili9341.mpy
    