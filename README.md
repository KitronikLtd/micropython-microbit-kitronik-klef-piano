# micropython-microbit-kitronik-klef-piano
Example MicroPython (for BBC micro:bit) code for the Kitronik :KLEF Piano ( www.kitronik.co.uk/5631 )

## Operation

This package contains a function to check whether a key has been touched on the piano:
```blocks
KitronikPiano.keyIsPressed(KitronikPiano, KitronikPiano.PianoKeys.KEY_K9)
```
The function returns a True or False output, so is ideal for use in 'if' statements or 'while' loops.

## Settings

There are two other public functions which can be used to adjust settings on the :KLEF Piano.

* Key Sensitivity:
	A higher value increases the sensitivity.
	To set the sensitivity of capacitive touch keys, this function should be used:
```blocks
KitronikPiano.setKeySensitivity(KitronikPiano, 10):
```
	(Sensitivty values range from 1 - 32; the default value is 8)
* Noise Threshold:
	A higher value enables the piano to be used in areas with more electrical noise.
	To set the noise threshold of capacitive touch keys, this function should be used:
```blocks
KitronikPiano.setKeyNoiseThreshold(KitronikPiano, 20):
```
	(Noise Threshold values range from 1 - 63; the default value is 5)

## License

MIT

## Supported Targets

BBC micro:bit
