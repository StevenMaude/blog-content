Title: Conversation conservation: recording audio input and output simultaneously in Linux
Date: 2016-12-01 12:00
Author: Steven Maude
Tags: audio, recording, Linux, Ubuntu
Summary: Recording audio input and output in Linux for screencasts, podcasts and interviews. 

## Why?

Sometimes you might need to record both the audio playing out on your
computer as well as an input. Often, this might be if you're recording a
screencast or podcast, or if you want to record both sides of an online
voice chat or video call, e.g. with Hangouts, Skype or some WebRTC app,
for instance.

In my case, I wanted to record an interview and, ideally, want to hear
what both of us were saying, without having to record both sides of the
conversation separately and later try to combine them into a single
piece of audio.

## How

The solution if you're using Linux and PulseAudio is [mentioned
here](https://superuser.com/questions/769249/how-to-record-both-input-and-output-audio-simultaneously)
but I've clarified this below so I can find it quickly:

1.  Run `pactl load-module module-loopback` in a terminal. You should
    start hearing your microphone input; with headphones on at least,
    you shouldn't get feedback. What you do get is a very slight delay
    in hearing yourself.  For me, using earphones and removing one
    seemed to help remove most of the off-putting distraction this delay
    causes, while still being able to hear the other participant in the
    conversation.

2.  Start recording in, say, [Audacity](http://www.audacityteam.org/) or
    some other audio recording software.

3.  Open the PulseAudio Volume Control. If you don't have it installed,
    `apt install pavucontrol` should get you it in Ubuntu. You may then
    have a shortcut to it wherever your programs get listed, e.g. in
    Ubuntu, you can access it via the Unity dash.
    
    Alternatively, run `pavucontrol&` in a terminal, open the Recording
    tab. to Recording tab, select what should be something like "Monitor
    of Built-in Audio Analogue Stereo" for the selection for Audacity.
    This is one thing that's a little counterintuitive; you don't see
    this unless you've already started recording.

4.  When you've finished, you can run `pactl unload-module
    module-loopback` to stop hearing audio input in the output. You
    might also want to reset the Audacity recording setting to what it
    was, so that you don't forget you changed it.
