Title: Migrating a Bitlocker Windows installation to a larger drive
Date: 2023-01-02 23:33
Author: Steven Maude
Tags: Bitlocker, Windows
Summary: How to clone a Windows installation to another disk

I recently cloned a Windows 10 installation's Bitlocker encrypted drive
to upgrade a PC's solid state drive (SSD) from a smaller SATA drive to
an NVMe drive. Here are thorough notes on what I did if you need to do
the same.

The Bitlocker aspect doesn't actually seem to make much difference here.
This is the same process you could to clone an unencrypted Windows disk,
but it's worth noting that this does work for Bitlocker-encrypted disks.

## Caveat

This upgrade ostensibly seemed to work fine.

However, with the cloned drive, the Windows Mail app required
reinstallation as it wouldn't load. From reading around, there can be
some weirdness around Universal Windows Platform (UWP) applications.
Right now, I can't find any specific fix outside of reinstalling those
affected apps. In this case, reinstalling the Mail app seemed to work,
and had retained all the existing data. That aside, other UWP apps
seemed to work on the machine, so I don't know. I love computers very
much.

**Do be prepared if you have lots of UWP apps**: you might still need to
reinstall them though. I couldn't find any other workaround, but only
looked for a few minutes.

## Upgrade process

For this kind of installation, I typically write out step-by-step what I
intend to do first, so I'm less likely to miss a step or forget
something. Ultimately, the process as it turned out didn't differ that
much from what I sketched out at first.

Of course, there was one issue I didn't anticipate: there was a Windows
recovery partition at the end of the original drive. This meant that the
free space after upgrading was not contiguous with the existing Windows
volume: the recovery partition was in the way, preventing the volume
from expanding to fill the drive. To fix this, I had to move the Windows
recovery partition to the end of the newer, larger drive, so that the
existing Bitlocker volume could be expanded by the Windows Disk
Management tool. [This Super User
question](https://superuser.com/questions/1453790/how-to-move-the-recovery-partition-on-windows-10)
helped solve that problem, and [this
answer](https://superuser.com/a/1637944) is used as the basis for some
of this guide.

Below are my corrected notes after completing the upgrade, broken into
four sections. It's worth reading through the whole set of instructions
first. These aren't completely exhaustive, but should be enough to get
you to what you need.

### Preparation

1. Backup the old drive entirely first, before starting the upgrade. The
   likelihood of disaster may be small, but the impact of that is high
   if you have no backup. So, **backup**.
2. Ensure you have the Bitlocker recovery key and it works. I don't
   think you should need the recovery key for upgrading a drive in the
   same PC, but, again, best to check this before you start.
3. Shutdown the PC, entirely powering it off. (I actually forgot to do
   this and hibernated, but this was also fine, provided the PC is
   powered off.)
4. Open up the PC, install the new drive into the expansion slot inside
   the PC and close up the PC again.
5. Update drive firmware if there is a update needed. You can try
   searching the manufacturer's site to see if an upgrade is available.
   Manufacturers don't always make this information easy to discover.
   You may just want to install whatever utility the manufacturer offers
   to check for firmware updates and update via that. (Most
   manufacturers have some kind of tool; a few provide updates via a
   bootable disk image.)
6. Download a bootable Linux installation: [Ubuntu](https://ubuntu.com)
   works fine and has all the tools you need.
7. (Optional) Verify the download; there is a [guide for checking Ubuntu
   downloads](https://ubuntu.com/tutorials/how-to-verify-ubuntu).
8. Write that Linux image to a USB drive or DVD as a "live installation.
9. (Optional) Verify that the Linux image has been written correctly:
   you can do this easily [if you're already running
   Linux](https://unix.stackexchange.com/a/84474).

### Cloning the disk

1. Boot the live Ubuntu installation from a USB or DVD. You'll probably
   need to enter the boot menu of your BIOS to select the USB or DVD to
   boot from. For Ubuntu booting via a DVD, you may want to add the
   custom boot parameter: `fsck.mode=skip` to skip the integrity check
   as [it is often very slow via
   DVD](https://bugs.launchpad.net/ubuntu/+source/casper/+bug/1875548).
2. (Optional) Wipe the newly installed drive. This may not be strictly
   be necessary if a new drive, but I tend to do this anyway. The Arch
   Linux wiki has lots of information on using the `hdparm` (for SATA
   drives) and `nvme-cli` (for NVMe drives) tools to do this. In the
   current Ubuntu release (22.04.1), the `nvme-cli` tool is not
   installed, so you'll need to open a terminal and install it via `sudo
   apt update && sudo apt install nvme-cli`. You will run these commands
   in a terminal.
3. Run some command to clone the drive. I went with running in a
   terminal: `sudo dd if=/dev/old-drive-device-name
   of=/dev/new-drive-device-name status=progress bs=32M; sync`

     Use the `lsblk` command to find the correct `old-drive-device-name`
     and `new-drive-device-name`. **Triple check that you have the input
     (`if`) and output (`of`) files the correct way round** before
     running the command.

     The `bs` controls the block size. The default block size is small,
     so we specify a larger one to speed up cloning the disk: the
     transfer rate was about 500 MB/s transfer rate, probably limited by
     the read speed of the SATA SSD drive.

     The final `sync` is to ensure anything cached is written to the
     disk, although shutting Linux down via the shutdown option (as
     opposed to just powering off) as we'll do next should also ensure
     this.

4. Shutdown Ubuntu entirely. Left click the mouse in the top-right of
   the screen where the volume icon is, and you'll see the power
   options.

### Reorganising the disk volumes

1. Check the boot order in the BIOS and reorder it if necessary to
   prioritise the new drive over the old.
2. Boot into Windows.
3. In an command prompt as administrator, use Windows' [REAgentC
   command](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/reagentc-command-line-options)
   to disable the Windows Recovery Environment temporarily: `reagentc
   /disable` — you could optimise this and save a reboot by doing this
   in Windows before cloning.
4. Shutdown Windows.
5. Boot back into your Ubuntu live installation once again.
6. Run the GParted graphical application. Move the Windows recovery
   partition to end of drive. You'll be prompted to fix the incorrect
   GPT record, which will be wrong due to the change in drive size. You
   need to do this otherwise moving the partition will fail. Apply the
   partition changes, which should now be successful.
7. Shutdown Ubuntu again.
8. Boot back into Windows.
9. In an command prompt as administrator, run `reagentc /enable` to
   enable the Windows Recovery Environment again.
10. Run the Computer Management application as administrator, and go
    to Disk Management.
11. Right click on the Bitlocker Windows volume, and select "Extend
    Volume" to fill the unused space.
12. Check the properties of the newly expanded drive in Windows Explorer
    and confirm that the drive has a larger size.

### Final checks and cleaning up

1. Boot into the [Windows Recovery
   Environment](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/windows-recovery-environment--windows-re--technical-reference)
   to confirm that it works. It's also possible to boot to this directly
   with ReAgentC via [`reagentc
   /boottore`](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/reagentc-command-line-options)
   command.
2. After you have checked the Windows recovery environment, reboot back
   into Windows.
3. Via the Activation settings, check that Windows is still activated if
   it was activated previously. I didn't need to reactivate the PC in
   this case.
4. Shutdown Windows.
5. Open the PC, disconnect the old drive, and then remove the old drive
   from the PC.
