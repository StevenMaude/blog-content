Title: PyCon 2021: Secure software supply chains
Date: 2021-10-15 17:27
Author: Steven Maude
Tags: PyCon, Python
Summary: A summary of a talk by Dustin Ingram at PyCon 2021.

## Modern Python, less modern me

I've been working for the past few months at The DataLab — now Bennett
Institute for Applied Data Science. There, Python is the main language
for development and collectively the developers have a lot of Python
experience.

Because of that, I've seen a lot more modern Python than I was
accustomed to seeing or writing. What I've found is what I knew about
Python is a little outdated. Certainly there have been a lot of new
Python features introduced that I didn't know about or only vaguely had
heard of, e.g.:

* dataclasses 
* assignment expressions, i.e. `:=`
* `breakpoint()` instead of having to import and use the `pdb` package
  directly

It seemed wise to me then to watch some recent conference talks. I may
write up notes on them. All that said, let's look at the first one.

## Secure Software Supply Chains for Python

This is a summary of [this
talk](https://www.youtube.com/watch?v=VWWgkF-0cDQ) by Dustin Ingram, a
PyPI maintainer.

The talk describes:

* What software supply chain attacks are.
* The current best Python practice for developes.
* What improvements could be made to `pip` and PyPI in future.

### Supply chain attacks

* They are a thing.
    * Involve a compromise of your dependencies, where they are
      distributed and everything used to build them.
    * This applies recursively to your dependencies' dependencies and so
      on.

### Types of supply chain attack

* MITM attack: intercepting a package download and replacing it with
  something malicious.
* Typosquatting: uploading malicious packages with names similar to
  well-known packages.
* Dependency confusion: where internal, non-public packages are used,
  but `pip` is misconfigured to check PyPI first and someone registers a
  malicious public package with the same name as the internal package.
* "Research": people deliberately introducing vulnerabilities into code.
* SolarWinds was mentioned as an example: compromise of build system.
* Compromised maintainers.
* Compromised source control.
* Leaked passwords/API tokens.
* Social engineering.

### Python best practices

* For Python, best current practices are:
    * Use pinned requirements and with hashes, e.g. via `pipenv lock`,
      or `pip-compile --generate-hashes`.
    * Use some notification service that monitors dependencies in your
      source, e.g. Dependabot (this is convenient, but is an extra
      component in the supply chain: you have to trust that Dependabot
      isn't creating malicious pull requests).
* There are other possible future improvements to PyPI and `pip`:
    * Removal of `setup.py` support to stop arbitrary code being run at
      install time. That might save you if you realise you've installed
      a compromised package, before importing and using the package.
    * Signed repository metadata ([PEP 458](https://www.python.org/dev/peps/pep-0458/)).
    * Having namespaces on PyPI.
