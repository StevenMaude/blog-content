Title: Making a MIDI keyboard modulation wheel work with third-party VSTs in FL Studio
Date: 2014-04-27 18:19
Modified: 2014-04-27 18:21
Author: Steven Maude
Tags: MIDI, production, keyboard, FL, VST, Studio, music, audio
Slug: making-midi-keyboard-modulation-wheel
Summary: How to get a mod wheel working with third-party plugins in FL Studio.

Been playing around with third-party VSTs in FL Studio and found I
couldn't get the modulation wheel to work (though it works fine in the
bundled plugins).

Eventually I found the fix
[here](http://music.tutsplus.com/tutorials/quick-tip-how-to-enable-the-mod-wheel-in-fl-studio--audio-10778).

The short version: add a third-party VST to your project. Go to the
browser menu and go to Current Project \> Generators \> Fruity Wrapper.
Next, you should see Modulation Wheel in the list under Fruity Wrapper;
right click it and choose "Link to controller". Enable Omni, make sure
Autodetect is enabled (it is by default for me), then move the wheel.

That link also suggests starting with an empty project, doing this
setup, then deleting the VST and saving the project as a template, which
is handy to avoid repeating this every time you work on a new project.
Just make a sub-directory in one of the existing FL Studio Templates
directories and save the .flp file in there.
