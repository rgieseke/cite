# cite

Prints citation for DOIs.

```
cite https://doi.org/10.1103/PhysRev.48.73 doi:10.1119/1.10927
```

Other formats are supported, e.g.

```
cite --format bibtex https://doi.org/10.1103/PhysRev.48.73 doi:10.1119/1.10927
```

For the full list, see
```
cite --help
```

Uses [habanero](https://github.com/sckott/habanero) and
the Crossref API (https://www.crossref.org/).
