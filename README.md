# WebSDR Writeup

**Hardware [350 pts]**

## Challenge Discerption:

```html
**At nightfall, everything lights up.
A beacon emits a signal in order to be recovered. The signal is emitted at 3.58 MHz 
every minute for about 30 seconds.
Find the message emitted.**
```

### Understanding the challenge

So from the challenge name we know there is a Software-Defined Radio trying to send the message on 3.58 MHz frequency in France as the CTF organized by ESIEE Paris engineering school in France

### Start working

After trying to catch that message from different SDR websites find the best and clear one working on kiwi SDR also we notice the massage it repeated at some point 

[best.wav](WebSDR%20Wri%20094c1/best.wav)

![Untitled](WebSDR%20Wri%20094c1/Untitled.png)

### Analyze the signal [RTTY]

after record the signal from the Web SDR let’s plot the frequency's values to know its uses two frequencies with low and higher one and compare it with the RTTY plot they similar 

![Untitled](WebSDR%20Wri%20094c1/Untitled%201.png)

![Untitled](WebSDR%20Wri%20094c1/Untitled%202.png)

### Knowing the Modulation [FSK]

From the step above or after wiki search for RTTY signals we will know we have an RTTY signal means its a FSK with shifting 400 Hz 

![Untitled](WebSDR%20Wri%20094c1/Untitled%203.png)

**Now what is FSK modulation?**

is a method of transmitting digital signals using discrete signals in binary states -- logic 0 (low) and 1 (high) in a binary frequency-shift key mechanism

Example:

![Untitled](WebSDR%20Wri%20094c1/Untitled%204.png)

Let’s try that on our signal after generate the spectrogram of it 

![Untitled](WebSDR%20Wri%20094c1/Untitled%205.png)

### FSK Decoding

From the last example we know the bitrate=12 bps and now we need to convert every signal element present more than one binary digits, the best way to deal with FSK using wav file recorded before but I would using image processing as we have the spectrogram of the signal

[aa.png](WebSDR%20Wri%20094c1/aa.png)

![aa.png](WebSDR%20Wri%20094c1/aa%201.png)

### Scripting Time 😜

From the previous apportion I wrote a script the extract the binary and search for the first alphabet of the flag **H** as a 8 bit binary then step by bitrate[12] and decode the collected binary's

[solve.py](WebSDR%20Wri%20094c1/solve.py)

```python
import math
from xml.etree.ElementTree import PI
from PIL import Image

a = 17
im = Image.open("aa.png")
w, h = im.size
condition = True

binary = ""

for i in range(w):

    if im.getpixel((i, 375))[0] > 200 and condition == True:
        z = 0
        for c in range(i,i+200):
            try:
                if im.getpixel((c, 375))[0] > 200:
                    z += 1
                else:
                    break
            except:
                break
        z = round(z/a)
        condition = False
        binary += "1" * z

    if im.getpixel((i, 375))[0] < 200 and condition == False:
        z = 0
        for c in range(i,i+200):
            try:
                if im.getpixel((c, 375))[0] < 200:
                    z += 1
                else:
                    break
            except:
                break
        z = round(z/a)
        condition = True
        binary += "0" * z

flag = ""
for i in range (binary.find("01001000"),len(binary),12):
    c = chr(int(binary[i:i+8],2))
    flag = flag + c
    if c == '}':
        print("Flag :",flag)
        break
```