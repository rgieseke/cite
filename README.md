# cite

[![PyPI](https://img.shields.io/pypi/v/cite.svg?style=for-the-badge)](https://pypi.org/project/cite/)

Prints citation from DOIs or URLs of journal articles which provide DOIs in their
metadata.

```
$ cite https://doi.org/10.1103/PhysRev.48.73

Einstein, A., & Rosen, N. (1935). The Particle Problem in the General Theory of Relativity. Physical Review, 48(1), 73–77. doi:10.1103/physrev.48.73
```

To generate a BibTeX entry with a shortdoi-based unique key use

```
$ cite --bibtex https://doi.org/10.1103/PhysRev.48.73
```

Other output formats are supported, e.g. citeproc-json

```
$ cite --format citeproc-json https://doi.org/10.1103/PhysRev.48.73 doi:10.1002/andp.19053221004
```

Where the journals provide the DOI in their website's metadata it is also
possible to use the article website URL:
```
$ cite https://journals.aps.org/pr/abstract/10.1103/PhysRev.48.73

Einstein, A., & Rosen, N. (1935). The Particle Problem in the General Theory of Relativity. Physical Review, 48(1), 73–77. doi:10.1103/physrev.48.73
```

For the full list of options, see
```
$ cite --help
```

Uses [habanero](https://github.com/sckott/habanero) and
the Crossref API (https://www.crossref.org/) as well as [Pybtex](https://pybtex.org/).
