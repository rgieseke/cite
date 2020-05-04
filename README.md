# cite

[![CI](https://img.shields.io/github/workflow/status/rgieseke/cite/CI?style=for-the-badge&label=actions&logo=github&logoColor=white)](https://github.com/rgieseke/cite/actions)
[![PyPI](https://img.shields.io/pypi/v/cite.svg?style=for-the-badge)](https://pypi.org/project/cite/)

## Installation

```
pip install cite
```

## Usage

Prints citation from DOIs or URLs of journal articles which provide DOIs in their
metadata.

```
$ cite https://doi.org/10.1103/PhysRev.48.73

Einstein, A., & Rosen, N. (1935). The Particle Problem in the General Theory of Relativity. Physical Review, 48(1), 73–77. doi:10.1103/physrev.48.73
```

Other output styles formats are supported, see the list of CSL styles ar <https://citation.crosscite.org/>

```
$ cite --style iso690-author-date-en https://doi.org/10.1103/PhysRev.48.73

EINSTEIN, A. and ROSEN, N., 1935, The Particle Problem in the General Theory of Relativity. Physical Review [online]. 1 July 1935. Vol. 48, no. 1, p. 73–77. DOI 10.1103/physrev.48.73. Available from: http://dx.doi.org/10.1103/PhysRev.48.73
```

To generate a BibTeX entry with a shortdoi-based unique key use `--bibtex` or `-b`

```
$ cite --bibtex https://doi.org/10.1103/PhysRev.48.73
```

The entry's key is made of name, year and [short DOI](http://shortdoi.org/) of the item.

To get Citeproc-JSON use `--json` or `-j`.

Where the journals provide the DOI in their website's metadata it is also
possible to use the article website URL:
```
$ cite https://journals.aps.org/pr/abstract/10.1103/PhysRev.48.73

Einstein, A., & Rosen, N. (1935). The Particle Problem in the General Theory of Relativity. Physical Review, 48(1), 73–77. doi:10.1103/physrev.48.73
```

To add to an entry to an existing BibTex file:

```
cite --bibtex https://doi.org/10.1103/PhysRev.48.73 >> bibliography.bib
```

For the full list of options, see
```
$ cite --help
```

Uses Crosscite [DOI Content Negotiation](https://citation.crosscite.org/).
