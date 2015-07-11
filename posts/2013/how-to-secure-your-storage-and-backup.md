Title: How to secure your storage and backup drives on Windows and Linux
Date: 2013-09-28 17:03
Modified: 2015-01-09 14:10
Author: Steven Maude
Tags: Bitlocker, backup, encryption, USB, HDD, external, TrueCrypt, drive
Slug: how-to-secure-your-storage-and-backup
Summary: A guide to securing data on external and backup drives by encrypting them.
Alias: /2013/09/how-to-secure-your-storage-and-backup.html

If you use computers even a little, you'll probably have acquired a few
external USB drives. They're cheap, reasonably quick and small, so it's
unsurprising that they're so popular. The only issue is that you may
well be storing personal data on them, meaning that if you lost them and
they're unencrypted, anyone can read their contents.

Compared with the painful time [I previously
spent](http://www.stevenmaude.co.uk/2013/09/a-beginners-guide-to-os-encryption-dual)
encrypting operating system drives, it's a relief that encrypting
non-system drives is far, far simpler.

<img class="article-image" src="{filename}/images/2013/Bitlocker_context_menu.png" alt="Bitlocker drive context menu.">

## Bitlocker

If only using Windows, and provided your copy of Windows is bundled with
it, you could use Bitlocker. Bitlocker is straightforward to setup with
self-explanatory instructions.

Right clicking an external drive in Explorer brings up the Bitlocker
option (as shown to the right).

<img class="article-image" src="{filename}/images/2013/Bitlocker_unlock_menu.png" alt="Bitlocker drive unlock menu.">

Next, you then choose a password to unlock the drive, then save or print
a recovery key in case you forget your password. All that's left is to
encrypt the drive by finally choosing to Start Encryption.

The next time you insert the drive, it will prompt you for the password
to unlock it. Enter it and the drive functions just as normal.

### Issues with Bitlocker

Note that you'll need to use Microsoft's [Bitlocker To Go
Reader](http://windows.microsoft.com/en-us/windows7/what-is-the-bitlocker-to-go-reader)
for **read-only access** to Bitlocker-encrypted drives in older Windows
version (Vista and XP). There are also
[some](https://code.google.com/p/libbde/)
[unofficial](http://www.hsc.fr/ressources/outils/dislocker/) projects
that support Bitlocker under Linux and OS X.

Update: Bought a USB 3 drive so that I could backup faster and was told
by Windows that "a drive attached to the system is not functioning" when
trying to enable Bitlocker. This is a [known
issue](http://support.microsoft.com/kb/2704232), but I hadn't read
anything about it until just now. In my case, my drive wouldn't even
show up when plugged in the USB 2 port making my shiny new drive
enclosure fairly useless. This is with the latest USB 3.0 eXtensible
Host Controller Driver for Intel 7 Series (1.0.9.254, at the time of
writing).

Update 2: USB 3 works fine, but there's [some weird Bitlocker or drive
specific issue
behaviour](http://www.stevenmaude.co.uk/2013/10/odd-behaviour-of-bitlocker-or-maybe-my)...

## TrueCrypt

!!! article-edit ""
    Edit: see my [earlier encryption
    post](http://127.0.0.1:8000/a-beginners-guide-to-os-encryption-dual.html#fn:2)
    for notes on the current state of TrueCrypt.

The other main option is [TrueCrypt](http://www.truecrypt.org/) which is
freely available, and has good cross-platform support, perhaps making it
a better choice. Go to Volumes > Create New Volume... and you'll see
this menu:

<img class="article-image" src="{filename}/images/2013/TrueCrypt_menu.png" alt="The TrueCrypt volume creation wizard.">

You can optionally use an encrypted drive container, which is a virtual
disk in a file, should you want to store unencrypted files on your drive
alongside encrypted ones. My preference is just to encrypt the entire
thing, so there's no risk of me inadvertently storing something
containing personal information in the unencrypted part.

<img class="article-image" src="{filename}/images/2013/TrueCrypt_volume_type.png" alt="Specifying TrueCrypt volume type.">

Here, TrueCrypt asks if you want to hide the volume. In my case, a
standard volume is sufficient.

<img class="article-image" src="{filename}/images/2013/TrueCrypt_volume_location.png" alt="Specifying TrueCrypt volume location.">

Click Select Device, choose the drive you want to encrypt and click
Next.

<img class="article-image" src="{filename}/images/2013/TrueCrypt_encryption_options.png" alt="The TrueCrypt volume creation window.">

If you've nothing on the drive already, you can format it. Otherwise,
you'll have to encrypt it in place which will take longer. On the next
page after this, it allows you to specify the encryption algorithms, I
leave these as default. It will then tell you the volume size so that
you can double check you've specified the correct drive.

<img class="article-image" src="{filename}/images/2013/TrueCrypt_format_options.png" alt="The TrueCrypt volume format window.">

After that, you enter a password, choose what kind of filesystem (e.g.
FAT or NTFS) you want for the drive, move the mouse in the TrueCrypt for
a while to generate random data and click Format.

<img class="article-image" src="{filename}/images/2013/TrueCrypt_drive_menu.png" alt="The TrueCrypt window showing a list of drives and drive letters to mount.">

To mount the drive, you launch TrueCrypt, choose Select Device, select
your TrueCrypt drive, select an empty drive letter and choose Mount.
You'll be prompted for your password, and then providing you enter the
correct password, your drive will be mounted and you can access the
files on it. When you've finished working with the drive, you should
select it in TrueCrypt and choose Dismount. You can then safely eject
the drive from Windows as you would normally, and then remove it from
your PC.

### Issues with TrueCrypt

The only requirement is that you need TrueCrypt to be running on a
destination PC. This can either be via having it installed to the PC
directly, or, for Windows PCs at least, having access to an appropriate
portable version of TrueCrypt.

The one big tradeoff compared with Bitlocker is that you require
administrative privileges even when running the
[portable](https://en.wikipedia.org/wiki/Portable_application) version
on Windows. If TrueCrypt has been previously installed to a Windows PC
by an administrator, then admin privileges are **not** required to mount
drives. (On Linux, even with TrueCrypt installs, it asks for admin
privileges since it requires them to mount a drive.) With Bitlocker,
non-admins can access drives without any issue (aside from older Windows
version needing the reader application ), and this might factor into
your choice of encryption software.

## Encrypting backup drives

If you're encrypting everything else, it probably makes sense to
considering encrypting your backups too. If your system is already
encrypted completely, you could simply clone the entire drive with
[Clonezilla](http://clonezilla.org/). I haven't tested this and I'm not
sure if there are issues with restoring the drive, particularly when if
a drive's been encrypted with TrueCrypt, though [some users report this
is fine](http://superuser.com/questions/312166/how-to-properly-image-a-truecrypt-system-partition).

Using the backup tools provided by each individual OS is also an
option.

### Windows

Windows Backup and Restore [needs slightly awkward
workarounds](http://superuser.com/questions/126111/how-can-you-use-windows-backup-with-a-truecrypt-encrypted-backup-destination)
to function with TrueCrypt drives; however, Bitlocker encrypted external
drives work seamlessly with this feature. The File History feature in
Windows 8 should work fine with TrueCrypt drives, on the other hand (it
doesn't use Volume Shadow Copy that TrueCrypt is incompatible with).

### Ubuntu

For Ubuntu, I'm using the built-in Backup tool (Déjà Dup) which is based
on [Duplicity](http://duplicity.nongnu.org/). At its core, this backup
tool is very much end-user focused. It's incredibly simple to set up.
Although it could benefit from better scheduling and more options, e.g.
exclusion of files versus simply choosing which directories to include,
making backups easy for users to do is not a bad thing.

Despite this, Déjà Dup has two handy features. First, it supports
encryption natively, so you don't even need to specially format a drive
or partition to encrypt the backup. You choose an encryption password
and it encrypts the backup.

Second, it integrates nicely with Ubuntu. Given a backup, you are able
to restore deleted files or previous versions directly from
[Nautilus](https://en.wikipedia.org/wiki/Nautilus_%28file_manager%29).

There are other backup alternatives like
[rsnapshot](http://www.rsnapshot.org/) (though you'd have to [handle
encryption
yourself](http://pig-monkey.com/2012/09/24/cryptshot-automated-encrypted-backups-rsnapshot/)),
but Déjà Dup gave me a fuss-free way to get an encrypted backup running,
which I really like.

## Summary

If you're carrying around sensitive or personal data on portable drives,
it's worth taking the time to make sure that the data's secure in case
you lose the drive. It's simple to setup regardless of whichever OS
you're using.
