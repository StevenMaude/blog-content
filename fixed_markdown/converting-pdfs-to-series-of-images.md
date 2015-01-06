Title: Converting PDFs to a series of images
Date: 2013-05-16 20:16
Modified: 2013-07-14 13:09
Author: Steven Maude
Tags: PDF, ImageMagick, convert
Slug: converting-pdfs-to-series-of-images
Summary: Using ImageMagick or GraphicsMagick to convert pages of a PDF to individual images.

I'm currently taking the "[Introduction to Data
Science](https://class.coursera.org/datasci-001/)" course via Coursera
(probably a subject itself for another post as it's been pretty
interesting so far even though it's only been going for just over two
weeks).

The lecture slides are provided as PDFs, but I like to annotate them
with my own notes too. I had been using Print Screen and then just
cropping the copied image. But, since I already had
[ImageMagick](http://www.imagemagick.org/) installed, I thought I should
try automatically converting the PDF slides to individual images.

A command like:

```shell
convert -density 300 input.pdf outputname_%0d.png
```

works pretty well to convert to PNGs.

(If using the
[GraphicsMagick](http://www.graphicsmagick.org/) fork of ImageMagick,
you'll need to add `+adjoin` to the command line, [otherwise
you only get the first page of the
PDF](http://sourceforge.net/p/graphicsmagick/bugs/214/) which is named
`outputname\_%0d.png"`.)
