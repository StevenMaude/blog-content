+++
title = "Migration notes"
summary = "Known differences between the original Pelican site and the Hugo migration."
url = "/migration-notes/"
+++

This Hugo migration keeps the original Markdown content, metadata, aliases, and most presentation details intact. The items below highlight the places where the migrated site still differs from the old Pelican setup.

## Site-wide differences

- The site now uses Hugo layouts and CSS instead of the previous Pelican theme, so the design is an approximation of the old clean theme rather than an exact clone.
- The `images` git submodule is mounted into Hugo's `static/images` output. A checkout without submodules still builds, but the image files themselves will be missing until the submodule contents are present.
- Pelican's `Alias` metadata is carried across to Hugo `aliases`, preserving legacy URLs used by the original site.

## Posts with converted Pelican edit notes

- `posts/2013/a-beginners-guide-to-os-encryption-dual.md`
- `posts/2013/dariks-boot-and-nuke-unrecognized.md`
- `posts/2013/horrible-wireless-network-pings-in.md`
- `posts/2013/how-to-secure-your-storage-and-backup.md`
- `posts/2013/installing-bokeh-on-ubuntu-1204-lts.md`
- `posts/2013/patching-android-roms-for-pdroid-using.md`
- `posts/2013/some-spring-winter-ubuntu-cleaning.md`
- `posts/2014/taking-control-of-chromium-and-chrome.md`
- `posts/2015/using-garmin-forerunner-watches-with-linux.md`
- `posts/2016/secure-erasing-a-frozen-drive.md`
- `posts/2016/windows-7-secure-boot.md`
- `posts/2017/rinse-fms-soundcloud-takedown.md`
- `posts/2017/trying-to-trim-down-static-gtfs-feeds.md`
- `posts/2018/a-look-at-pipenv.md`

## Posts and pages that still rely on raw HTML for presentation

- `posts/2013/a-beginners-guide-to-os-encryption-dual.md`
- `posts/2013/firefox-21-annoyances.md`
- `posts/2013/how-to-access-github-over-ssh-on-ubuntu.md`
- `posts/2013/how-to-secure-your-storage-and-backup.md`
- `posts/2013/how-universities-can-help-develop.md`
- `posts/2013/job-advertisements.md`
- `posts/2013/leaky-phone-apps.md`
- `posts/2013/things-ive-learned-from-building-and.md`
- `posts/2013/uses-for-a-raspberry-pi-part-1.md`
- `posts/2013/uses-for-a-raspberry-pi-part-2.md`
- `posts/2014/arduous-lessons-in-python-why-main-is.md`
- `posts/2014/beatmatching-five-reasons-why-digital.md`
- `posts/2014/book-review-data-science-for-business.md`
- `posts/2014/chatting-about-data-science-careers.md`
- `posts/2014/heartbleed-ill-communication.md`
- `posts/2014/making-aero-theme-settings-stick-in.md`
- `posts/2014/rockbox-ipod-nano-2g-and-inverted-audio.md`
- `posts/2014/taking-control-of-chromium-and-chrome.md`
- `posts/2014/us-pycon-2014-talks.md`
- `posts/2016/github-human-detection.md`

## Pages with intentionally adjusted URLs

- `pages/about_me.md` is now published at `/about/` for a clearer Hugo page URL, while retaining the legacy alias `/p/contact.html`.
