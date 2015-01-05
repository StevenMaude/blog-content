Title: Android device encryption is (mostly) good
Date: 2014-04-05 10:32
Author: Steven Maude
Tags: encryption, Android
Slug: android-device-encryption-is-mostly-good

If you've read other posts here, you might notice that I've gone through
a phase of
[encrypting](http://www.stevenmaude.co.uk/2013/09/how-to-secure-your-storage-and-backup.html)
[new](http://www.stevenmaude.co.uk/2013/09/a-beginners-guide-to-os-encryption-dual.html)
devices I have.

My [new
phone](http://www.stevenmaude.co.uk/2014/03/phone-upgrades-and-privacy-downgrades.html)
is now no different.

In trying to research what problems can arise if you encrypt Android, it
did seem like encryption isn't a widely used feature. But, as I was
starting afresh with my phone anyway, it seemed a good time to test it
out.

<a name="more"></a>

On my phone, out of the box, it encrypted in just a few minutes. I
didn't bother running any before and after benchmarks, but it doesn't
*feel* like there's any impact on the responsiveness of the phone.

There are two downsides though.

One is the irritating
[feature](https://code.google.com/p/android/issues/detail?id=29468) that
**the encryption password is just the screen unlock password you use**.
This isn't great. It either means you need a painfully complicated
screen lock passphrase, everytime you want to unlock your phone, or it
means you'll have a simple encryption password.

That issue discussion highlights that it is possible to change the
encryption password, but this requires you to enter a shell command as
root. There's an
[app](https://github.com/nelenkov/cryptfs-password-manager) that adds a
convenient frontend to this process, though it still requires root. As
the README there points out, watch out: **changing your screen unlock
code will change your encryption password to this too!**

The second problem is that encryption can impact on your use of
recovery. ClockworkModRecovery doesn't support encrypted devices. TWRP
apparently does, but didn't seem to work with my Moto G; it should
prompt for an encryption password, but doesn't and just fails to mount
the phone's partitions.

That's not a huge problem for me, but I expect that this is going to
prevent my phone from receiving official updates. Perhaps reflashing a
manufacturer recovery and updating will work? In the (only slightly
inconvenient) worst case, I'll just have to backup everything, do a
fresh install, re-root and restore everything.

It would be nice if encryption on Android was more user-friendly, though
as the problems aren't particularly onerous, the extra security is
definitely welcome.

</p>

