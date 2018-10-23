# cite

Prints citation from DOIs or URLs of journal articles which provide DOIs in their
metadata.

```
$ cite https://doi.org/10.1103/PhysRev.48.73 doi:10.1002/andp.19053221004

Einstein, A., & Rosen, N. (1935). The Particle Problem in the General Theory of Relativity. Physical Review, 48(1), 73–77. doi:10.1103/physrev.48.73

Einstein, A. (1905). Zur Elektrodynamik bewegter Körper. Annalen Der Physik, 322(10), 891–921. doi:10.1002/andp.19053221004
```

Other output formats are supported, e.g. for BibTeX

```
$ cite --format bibtex https://doi.org/10.1103/PhysRev.48.73 doi:10.1002/andp.19053221004
```

Where the journals provide the DOI in their website's metadata it is also
possible to use the article website URL:
```
$ cite https://journals.aps.org/pr/abstract/10.1103/PhysRev.48.73

Einstein, A., & Rosen, N. (1935). The Particle Problem in the General Theory of Relativity. Physical Review, 48(1), 73–77. doi:10.1103/physrev.48.73
```

For the full list, see
```
$ cite --help
```

Uses [habanero](https://github.com/sckott/habanero) and
the Crossref API (https://www.crossref.org/).
