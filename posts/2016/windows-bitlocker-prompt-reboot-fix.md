Title: Stopping Windows from rebooting at the BitLocker boot password prompt
Date: 2016-09-17 23:52
Author: Steven Maude
Tags: BitLocker
Summary: How to prevent Windows from rebooting after a short timeout when waiting for a boot BitLocker password.

Short post, but more noting this for myself more than anything. There
are several times when I've blogged little fixes and they've proven
handy to have in the future, e.g. when I'm setting up a new PC. Partly
because I know they're on my blog, and partly because the posts are
titled in the way I would search for a solution.

If you have a Windows PC (I think 8 upwards; but definitely 10, and 8.1)
with BitLocker enabled, you may find that it reboots shortly without you
even doing anything. If you've a long password and aren't a quick
typist, you may even find that this means you struggle to enter your
password in time. This is apparently a problem if you have a UEFI install,
which will be a common configuration these days.

Having just tested this simple fix that I saw on [Microsoft's
forums](https://social.technet.microsoft.com/Forums/office/en-US/932630c2-ae3d-4cbd-8d79-a492806363ea/windows-81-bitlocker-automatic-shutdown-during-password-prompt?forum=w8itproinstall):

```doscon
bcdedit /set {bootmgr} bootshutdowndisabled 1
```

it seems to have resolved the problem; the password prompt will remain on
indefinitely.
