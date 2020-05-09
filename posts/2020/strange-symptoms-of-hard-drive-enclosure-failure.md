Title: Strange symptoms of hard drive enclosure failure
Date: 2020-05-09 21:35
Author: Steven Maude
Tags: hard drive, hardware, Windows
Summary: Describing some symptoms of a wonky hard drive enclosure on
         Windows

# Reliable failure

It's sometimes a reassuring comfort to know that computers and
computer-related things are entirely reliable. In that they are anything
but.

As I spent about an hour looking into this problem, and now think it has
been fixed, perhaps it is helpful to document the symptoms such that
anyone searching might find this page and save them some time.
Especially if, like me, you don't have a spare enclosure to test with
and are thinking whether to buy a new one or not.

(Yes, you probably should, is the answer, if you don't want to read
further.)

# Some background

My enclosure was a cheap and cheerful once with USB and eSATA ports.
eSATA is a bit dated these days, but is useful if you're working with
old PCs that don't have USB 3 ports.

## Symptoms

There were different failure modes depending on how the drive was
connected:

* When connected by USB, the drive was not recognised by Windows. That
  is, it did not show up in File Explorer when connected, as if it
  wasn't attached at all.

    In Disk Management, Windows was claiming the partition was a GPT
    Protective Partition, whereas it was a real GPT partition, and
    incorrectly had a size of 16,777,216 MB, i.e. the NTFS volume limit
    with default cluster size, which was also incorrect.

* When connected by eSATA, the drive was correctly recognised by
  Windows. Creating folders and, I think, copying moderate sized files
  apparently worked OK, though I didn't try reading the files back from
  the drive.

    However, running the Windows 7 Backup and Restore tool reliably caused
    an error. Often, as soon as the backup process started to write to the
    drive in the enclosure, the drive acted as if it had been
    disconnected. That is, the backup failed, and the drive was no longer
    visible in File Explorer.

## Possible causes?

As far as I could tell, there were three possibilities:

* **Something was wrong with Windows**. Not impossible, but this felt
  like more of a hardware fault, especially with the strange difference
  in behaviour between USB and eSATA, and with observed failures when
  different parts of Windows were running. It wasn't just the Backup and
  Restore tool that was failing, but Disk Cleanup had also caused the
  drive to disconnect.
* **The hard drive itself was failing**. Not impossible either, but
  unlikely. Though a magnetic disk, it is enterprise-grade and hadn't
  had much usage. In fact, the drive's SMART readings indicated a few
  hundred hours of time spent powered on.
* **Something was wrong with the enclosure**. Probably most likely,
  given the enclosure was inexpensive.

A cabling issue was ruled out on the basis that both USB and eSATA
weren't working, and had very different behaviour via the two
connections.

## Closing off the matter

In the end, not having a spare enclosure to test with, I bought a new
enclosure to try out. Out of curiosity, I chose one with both USB and
eSATA to test both out, in case the problem recurred.

This did resolve part of the problem: the drive showed up both via eSATA
and USB in the new enclosure. On the other hand, the Windows 7 Backup
tool on Windows 10 was still failing. My hunch was that the faulty
enclosure had somehow got the drive into an odd state. I never figured
out what exactly the problem was here. A disk check did show errors,
though I can't remember whether those were able to be repaired, or
whether the drive disconnected while trying to do so. Maybe there was
some corruption of the file system?

In the end, formatting the drive, encrypting the drive again and then
backing up finally resolved the — by-now very tedious — problem. So, not
all that exciting, but if you are witnessing similar symptoms, you can
probably fix it with a new enclosure.
