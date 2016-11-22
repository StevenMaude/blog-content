Title: Securely erasing frozen hard disks with hdparm
Date: 2016-11-22 13:54
Author: Steven Maude
Tags: hdparm, erase
Summary: How to use hdparm to erase hard drives, and what to do if the drive is frozen.

Yesterday I was trying to erase a hard drive before I used it for a new
install. It may well have never been used, but I couldn't remember and,
for the sake of a few minutes, it seemed sensible to do so first.

The best way to erase, especially if the drive is a solid state drive,
is to use the [ATA Secure
Erase](https://ata.wiki.kernel.org/index.php/ATA_Secure_Erase) command
which [I've mentioned
before]({filename}../2014/securely-erasing-ssd-drives.md).
This command should also work for most magnetic hard drives too, unless
they're ancient.

Instead of just mentioning the tool, I've summarised the details from
the lengthy page where I found them below, and discuss how to deal with
"frozen" drives.

You can access hdparm by booting into, for example, an Ubuntu
installation DVD or USB. Installing Linux isn't required: you can just
"Try Ubuntu" instead which doesn't install anything at all.

## Safety first

First, the most sensible thing to do when erasing a drive is remove any
drives other than those you wish to erase. It means even if you
accidentally type the wrong thing that you won't erase a drive that you
didn't intend to.

Next, you need to get the drive's name. Open a terminal by pressing
Ctrl+Alt+T.

```sh
sudo lshw -class disk
```

This will show you details of the disk, including the name. Replace the
`/dev/sdX` in the commands below with that name.

## Setting a password

The next task is to set a password. I'm not sure that you really need to
do this, but the
[kernel.org guide](https://ata.wiki.kernel.org/index.php/ATA_Secure_Erase)
advises it due to problems with certain PCs, and it only takes one extra
command. Note that the "foo" password below can be replaced by something
of your choice, but it doesn't really matter; when the drive is erased,
the password should be removed.

```sh
$ sudo hdparm --user-master u --security-set-pass foo /dev/sdX
security_password: "foo"
/dev/sdX:
 Issuing SECURITY_SET_PASS command, password="foo", user=user, mode=high
SECURITY_SET_PASS: Input/output error
```

Well, that error wasn't expected.

When I've used hdparm in this way previously, I haven't had a problem.
You might expect it if the drive has a password set already, but in this
case I couldn't recall doing that. If that's the same for you, it could
be a simple fix.  First, check the drive's current status via:

```sh
$ sudo hdparm -I /dev/sdX
```

and you may see "frozen",  as opposed to "not frozen", in the "Security"
section of the `hdparm` output. This means you can't change security
settings, so attempting to set a password fails.

## Unfreezing

In this case, the [actual
fix](https://superuser.com/questions/810867/new-ssd-hdparm-shows-frozen-whether-secure-erase-is-needed-before-installing)
is simple. Suspending the PC, then powering it back on should then give
you an unfrozen drive: you can check by running the `hdparm -I` command
above again.

Now, if you retry setting a password, you should be able to run the
`SECURITY_SET_PASS` command without error. Also, rerunning the `hdparm
-I` command yet another time should show that a password is "enabled" as
opposed to "not enabled".

## Erasing

You can now proceed with the erase. If your drive's `hdparm` output
states `supported: enhanced erase`, you could replace the
`--security-erase` below with `--security-erase-enhanced`:

```sh
$ sudo time hdparm --user-master u --security-erase foo /dev/sdX
```

After the erase, the password should be removed, and running the `hdparm
-I` command one final time should show that the password is "not
enabled".
