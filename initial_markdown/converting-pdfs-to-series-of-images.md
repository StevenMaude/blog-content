Title: Converting PDFs to a series of images
Date: 2013-07-14 13:09
Author: Steven Maude (noreply@blogger.com)
Tags: PDF, ImageMagick, convert
Slug: converting-pdfs-to-series-of-images

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
<span>convert -density 300 input.pdf outputname\_%0d.png</span>  
<span style="font-family: inherit;">works pretty well to convert to
PNGs.</span>  
  
<span style="font-family: inherit;">(If using the
[GraphicsMagick](http://www.graphicsmagick.org/) fork of ImageMagick,
you'll need to add <span>+adjoin</span> to the command line, [otherwise
you only get the first page of the
PDF](http://sourceforge.net/p/graphicsmagick/bugs/214/) which is named
<span>outputname\_%0d.png</span>".)</span>  
<span><span style="font-family: inherit;"><span style="font-family: inherit;">  
</span></span></span>
