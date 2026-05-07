# Hugo migration notes

The following content was migrated with known non-identical implementation details:

- `posts/2013/a-beginners-guide-to-os-encryption-dual.md` keeps existing inline HTML markup and depends on Hugo Goldmark unsafe rendering to preserve the original presentation.
- `posts/2013/firefox-21-annoyances.md` keeps existing inline HTML markup and depends on Hugo Goldmark unsafe rendering to preserve the original presentation.
- `posts/2013/how-to-access-github-over-ssh-on-ubuntu.md` keeps existing inline HTML markup and depends on Hugo Goldmark unsafe rendering to preserve the original presentation.
- `posts/2013/how-to-secure-your-storage-and-backup.md` keeps existing inline HTML markup and depends on Hugo Goldmark unsafe rendering to preserve the original presentation.
- `posts/2013/job-advertisements.md` keeps existing inline HTML markup and depends on Hugo Goldmark unsafe rendering to preserve the original presentation.
- `posts/2013/leaky-phone-apps.md` keeps existing inline HTML markup and depends on Hugo Goldmark unsafe rendering to preserve the original presentation.
- `posts/2013/things-ive-learned-from-building-and.md` keeps existing inline HTML markup and depends on Hugo Goldmark unsafe rendering to preserve the original presentation.
- `posts/2013/uses-for-a-raspberry-pi-part-1.md` keeps existing inline HTML markup and depends on Hugo Goldmark unsafe rendering to preserve the original presentation.
- `posts/2013/uses-for-a-raspberry-pi-part-2.md` keeps existing inline HTML markup and depends on Hugo Goldmark unsafe rendering to preserve the original presentation.
- `posts/2014/arduous-lessons-in-python-why-main-is.md` keeps existing inline HTML markup and depends on Hugo Goldmark unsafe rendering to preserve the original presentation.
- `posts/2014/beatmatching-five-reasons-why-digital.md` keeps existing inline HTML markup and depends on Hugo Goldmark unsafe rendering to preserve the original presentation.
- `posts/2014/book-review-data-science-for-business.md` keeps existing inline HTML markup and depends on Hugo Goldmark unsafe rendering to preserve the original presentation.
- `posts/2014/chatting-about-data-science-careers.md` keeps existing inline HTML markup and depends on Hugo Goldmark unsafe rendering to preserve the original presentation.
- `posts/2014/heartbleed-ill-communication.md` keeps existing inline HTML markup and depends on Hugo Goldmark unsafe rendering to preserve the original presentation.
- `posts/2014/making-aero-theme-settings-stick-in.md` keeps existing inline HTML markup and depends on Hugo Goldmark unsafe rendering to preserve the original presentation.
- `posts/2014/rockbox-ipod-nano-2g-and-inverted-audio.md` keeps existing inline HTML markup and depends on Hugo Goldmark unsafe rendering to preserve the original presentation.
- `posts/2014/taking-control-of-chromium-and-chrome.md` keeps existing inline HTML markup and depends on Hugo Goldmark unsafe rendering to preserve the original presentation.
- `posts/2014/us-pycon-2014-talks.md` keeps existing inline HTML markup and depends on Hugo Goldmark unsafe rendering to preserve the original presentation.
- `posts/2016/github-human-detection.md` keeps existing inline HTML markup and depends on Hugo Goldmark unsafe rendering to preserve the original presentation.

Other intentional migration differences:

- The site theme is a Hugo implementation that matches the original layout closely, but it is not the Pelican Bootstrap theme.
- Legacy Pelican `{filename}` links were converted to Hugo `relref` shortcodes.
- The images submodule was replaced with tracked static files required by the migrated site build.
