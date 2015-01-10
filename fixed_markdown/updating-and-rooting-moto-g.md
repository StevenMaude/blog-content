Title: Updating and rooting Moto G
Date: 2014-08-25 15:42
Modified: 2014-08-25 18:34
Author: Steven Maude
Tags: Moto, firmware, upgrade, Android, system, root
Slug: updating-and-rooting-moto-g
Summary: How to restore a Moto G to stock firmware, unlock bootloader and gain root access.
Alias: /2014/08/updating-and-rooting-moto-g.html

## My Moto G has been nagging me to upgrade firmware

So I did today.

(I was persuaded by the Motorola system updater. Not because it's a
lovely looking bit of software, but because it makes nagging an art with
its focus-stealing prompt. If you go for the "no" option, your phone
kindly reminds you again in an hour **every hour**, just in case you've
forgotten. This is regardless of what you're doing at the time, even if
you're say using Google Maps for driving navigation which is quite
hideous. Even the option to postpone the reminder for a week or a month
would be nice. A rubbish, rubbish, rubbish user experience.)

A simple upgrade is as easy as pressing "upgrade". Because my phone was
rooted and encrypted, the upgrade was likely to fail, so I had to
restore it to stock firmware first.

However, I wanted to then reroot it so that I could use
[XPrivacy](https://github.com/M66B/XPrivacy). This lets you restrict the
permissions that apps have. Google did have App Ops in Android which did
a similar thing (without quite as much granularity, I believe) but
promptly removed it. It would have been good of them to leave it in: it
would have removed one reason I have for rooting. Android apps are just
far more intrusive in their permissions than they usually need to be.

No, I don't want Twitter's app to access my contacts, thanks; I'm more
than capable of finding people on Twitter directly. No, there's no
reason for Soundhound to know where I am. No, even if my phone **had**
NFC, I don't want F-Droid to be able to use it.

The assessment
[here](http://www.cnet.com/news/why-android-wont-be-getting-app-ops-anytime-soon/)
is that one big reason for the removal of App Ops is due to it breaking
apps. I disagree with that though. Using XPrivacy, I restrict almost
every app and haven't had any trouble.

I can understand that if app permission controls were enabled by
default, there's the possibility that it could cause problems for users
that don't understand the implications of allowing/denying permissions,
but if it was something like the developer options where you have to
deliberately enable it, then they wouldn't even know it was present.

Anyway, here are the reference notes I made while upgrading for (the
inevitable) next time.

## Preliminary setup with Ubuntu

(or your choice of a Linux that has `adb` and `fastboot`)

1.  Install (to a live USB, or use an existing install on your laptop)
2.  Enable third party repositories in "Software and Updates".
3.  Do `sudo apt-get update`.
4.  `sudo apt-get install android-tools-adb android-tools-fastboot`

## Backup data from phone

Copy off any photos, documents or other files you want to save.

If you want to backup your call logs and text messages, Call Logs Backup
and Restore, and SMS Backup and Restore work pretty well for me. That
said, they do request internet permissions which I block.

## Restore stock firmware

Stock firmwares are available
[here](http://sbf.droid-developers.org/phone.php?device=14) and [this
post](http://forum.xda-developers.com/showthread.php?t=2542219) was a
useful reference.

Boot into the bootloader using power on and volume down key (or enable
USB debugging mode when the phone's on normally and do
`adb reboot-bootloader`).

```shell
sudo fastboot flash partition gpt.bin
sudo fastboot flash motoboot motoboot.img
sudo fastboot flash logo logo.bin
sudo fastboot flash boot boot.img
sudo fastboot flash recovery recovery.img
sudo fastboot flash system system.img_sparsechunk1
sudo fastboot flash system system.img_sparsechunk2
sudo fastboot flash system system.img_sparsechunk3
sudo fastboot flash modem NON-HLOS.bin
sudo fastboot erase modemst1
sudo fastboot erase modemst2
sudo fastboot flash fsg fsg.mbn
sudo fastboot erase cache
sudo fastboot erase userdata
sudo fastboot reboot
```

(sparsechunk files may have numbers 0, 1, 2 - just flash them in
ascending order.)

## Upgrade

Boot into stock and install update.

**To avoid heartache**, make sure you check for system updates
**after** you update, and install any further updates before
proceeding. Repeat until no update is found. Otherwise, like me, you may
discover after rooting again that there are still updates remaining
after the first one. In that case, you'll have to restore to stock again
:( (I was on 4.4.2, but there was a minor update that didn't change the
version before the latest 4.4.4 update.)

## Unlock bootloader

** Only needed if not previously unlocked; while restoring stock
firmware and upgrading, this didn't get relocked. **

You need a bootloader unlock code from Motorola's
[site](https://motorola-global-portal.custhelp.com/app/standalone/bootloader/unlock-your-device-a).

```shell
fastboot oem unlock
```

Boot into fastboot mode: Enable developer mode again in settings:

```shell
adb reboot bootloader
```

Optional: get a copy of the original Motorola logo and do:

```shell
sudo fastboot flash logo original_logo.bin
```
to remove the annoying "bootloader is unlocked" warning at boot.

See [CyanogenMod's
site](http://wiki.cyanogenmod.org/w/Template:Unlock_Bootloader) for more
details.

## Install custom recovery

Get custom recovery; [I used TWRP](http://teamw.in/project/twrp2/233).

Get a recent fastboot .img; at the time of writing, 2.7.1.1 was the
latest, but didn't work. 2.7.1.0 worked fine.

Install through bootloader using fastboot:

```shell
sudo fastboot flash recovery modified_recovery.img
```

## Root the phone by installing SuperSU

Boot from bootloader into TWRP recovery. Reboot system, say yes to
install SuperSU.

Boot up, run SuperSU installer; go to Play Store and choose **update**
(**not** open).

This will probably prompt to install a new binary; the normal install
should work fine.

## Install XPrivacy

Install XPrivacy installer. Follow each of the several instruction steps
that are shown when you run it.

## Encrypt and change password again

Create a screen lock PIN or password, then fully charge battery and
encrypt.

Change the password using [Cryptfs
Password](https://play.google.com/store/apps/details?id=org.nick.cryptfs.passwdmanager&hl=en)
so that you can have a separate screen unlock code and encryption passphrase.

(This is another good reason to root your phone. Without this, your
encryption password is identical to your screen unlock code. Unless you
want to have either:

* a weak password, or
* a huge password that you have to enter every time you unlock your phone

you'll need to change it using CryptFS which requires root access.)

## Disable all the slow animations

To make Android snappier, disable the animations by enabling the
developer options. Go in Settings \> About phone, scroll to the bottom
and keep pressing build number until it tells you the developer options
are active. Now, in Settings \> Developer options, you can set "Window
animation scale", "Transition animation scale" and "Animator duration
scale" all to off.

## Restore data, account, messages, call logs

Reinstall SMS Backup and Restore, Call Log Backup and Restore, and
restore the backups you made. Reinstall any other apps you want,
including [F-Droid](https://f-droid.org/) if you want AdAway and that's
everything finally done. No more nagging for updates!
