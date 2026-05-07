# blog-content

This repository contains the content, layouts, and configuration for
[stevenmaude.co.uk](https://www.stevenmaude.co.uk), now built with Hugo.

## Local development

1. Install Hugo extended.
2. Initialise the images submodule if you want image assets available locally:
   `git submodule update --init --recursive`
3. Start the development server from the repository root:
   `hugo server`

To create a production build, run `hugo --gc --minify`.
