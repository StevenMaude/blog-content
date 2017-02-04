Title: Switching BitLocker protection methods without re-encrypting
Date: 2017-02-04 17:54
Author: Steven Maude
Tags: BitLocker, manage-bde
Summary: How to change BitLocker key protectors without having to
         decrypt and re-encrypt a drive.

## Overzealous TPM protection

I'd set up BitLocker for someone using the Trusted Platform Module (TPM)
in their laptop with a PIN[^1] to decrypt the drive. Unfortunately, they
found that, after some time, the system tended to lock the PIN out,
unless they used a recovery key to bypass the TPM and PIN access
altogether.

As far as I can tell, this is some feature of the TPM in this particular
laptop where too many incorrectly entered passwords results in the TPM
locking out for some lengthy and possibly indefinite amount of time.
Perhaps even permanently. I don't think this is the case where incorrect
passwords are continually entered in a short time period, but where
incorrect attempts over a longer period are cumulatively logged.

In this case, this state doesn't seem to get reset even if you
subsequently re-enter the correct password, or unlock with another
method. (It seems reasonable that the TPM's unaware of whether
BitLocker's been unlocked or not by other means.)

## Fixing the TPM

You can rectify this by [resetting the TPM
lockout](https://technet.microsoft.com/en-us/library/dd851452(v=ws.11).aspx)
but this is only a temporary fix. Again, after some number of password
failures the lockout may happen again. My conclusion in this case is
that, although disabling the TPM makes the system slightly less secure,
the greatest threat here is not an unauthorised user accessing the data,
but an authorised user being unable to access the data. Switching to
just a password unlock then seems more sensible. I wouldn't recommend
this downgrade in security otherwise.

At first look, you might think that this is a chore to switch. There's
no obvious way of doing this in the BitLocker options for the drive, or
under Control Panel, and your instinct might be to decrypt the drive and
encrypt again. That can be time consuming, especially with large drives.

## Using manage-bde to change key protection methods

Instead, you can run the command line utility:
[manage-bde](https://technet.microsoft.com/en-us/library/ff829848(v=ws.10).aspx).

Since TPM plus PIN, or recovery key (or some other method of securing
your BitLocker encryption key) are key protection methods, Microsoft
terms them "protectors". Also, here we are looking at removing a TPM and
PIN protector, but you can use manage-bde to handle any BitLocker
protector.

Specifically, you want to remove the existing TPM and PIN protector:

```dos
manage-bde -protectors -delete <Drive> -tpmandpin
```

You have to do this first, as it's not possible to have both TPM and PIN
protector, and a password protector.

(A caution that `-delete` without specifying `-type` removes all
protectors and then will disable protection, so that you can still
access your drive in future. If you do that, you'll need to add new
protectors, as below, and you'll need to add new recovery protectors,
should you wish. You can do by specifying `-recoverypassword` for a
numerical recovery code, or `-recoverykey` for an external key in the
`-add` command below. And then you must enable the protectors again with
`manage-bde -protectors -enable`, including new recovery keys should you
wish to have them.)

Next, add a new protector, e.g. a password:

```dos
manage-bde -protectors -add <Drive> -password
```

(`C:` is the most likely `<Drive>` value here.)

You'll be prompted to enter, and then confirm, the new password. Now,
you'll have a password protector, which won't be subject to a TPM
lockout, as we wanted.
 
Finally, you can also check BitLocker status:

```dos
manage-bde -protectors -status
```

to confirm that the drive is encrypted, and which key protectors are
active.

[^1]: Well, password. You can configure Group Policy to allow passwords
with TPM, instead of just numerical PINs. Microsoft's documentation
always refers to this option as "TPM and PIN" regardless. This doesn't
change the BitLocker prompt: it still asks for a PIN.
