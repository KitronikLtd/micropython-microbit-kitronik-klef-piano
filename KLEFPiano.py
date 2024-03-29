# Copyright (c) Kitronik Ltd 2022. 
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from KitronikKLEFPiano import *
import music

# On V2 micro:bits only
from microbit import set_volume
volume = 100
set_volume(volume)

# Setup :KLEF Piano
piano = KitronikPiano()

# Will run forever listening for key presses
# Each key press will play a different note
while True:
    # Up arrow key
    if piano.keyIsPressed(piano.PianoKeys.KEY_K0):
        if volume < 250:
            volume += 50
        # On V2 micro:bits only
        set_volume(volume)
    # Down arrow key
    if piano.keyIsPressed(piano.PianoKeys.KEY_K8):
        if volume > 0:
            volume -= 50
        # On V2 micro:bits only
        set_volume(volume)
    # C key
    if piano.keyIsPressed(piano.PianoKeys.KEY_K9):
        music.play('c4')
    # C# key
    if piano.keyIsPressed(piano.PianoKeys.KEY_K1):
        music.play('c#4')
    # D key
    if piano.keyIsPressed(piano.PianoKeys.KEY_K10):
        music.play('d4')
    # D# key
    if piano.keyIsPressed(piano.PianoKeys.KEY_K2):
        music.play('d#4')
    # E key
    if piano.keyIsPressed(piano.PianoKeys.KEY_K11):
        music.play('e4')
    # F key
    if piano.keyIsPressed(piano.PianoKeys.KEY_K12):
        music.play('f4')
    # F# key
    if piano.keyIsPressed(piano.PianoKeys.KEY_K3):
        music.play('f#4')
    # G key
    if piano.keyIsPressed(piano.PianoKeys.KEY_K13):
        music.play('g4')
    # G# key
    if piano.keyIsPressed(piano.PianoKeys.KEY_K4):
        music.play('g#4')
    # A key
    if piano.keyIsPressed(piano.PianoKeys.KEY_K14):
        music.play('a4')
    # A# key
    if piano.keyIsPressed(piano.PianoKeys.KEY_K5):
        music.play('a#4')
    # B key
    if piano.keyIsPressed(piano.PianoKeys.KEY_K6):
        music.play('b4')
    # High C key
    if piano.keyIsPressed(piano.PianoKeys.KEY_K7):
        music.play('c5')
