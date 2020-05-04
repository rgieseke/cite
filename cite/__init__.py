import argparse
import sys
import urllib

import requests
from lxml import html
from pybtex.database import BibliographyData, parse_string
from slugify import slugify

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions

doi_fields = ["doi", "citation_doi", "prism.doi", "dc.identifier"]

parser = argparse.ArgumentParser(description="cite - get citation for DOI.")
parser.add_argument(
    "-v",
    "--version",
    action="version",
    version="%(prog)s {version}".format(version=__version__),
)
parser.add_argument(
    "-s",
    "--style",
    default="apa",
    required=False,
    help='return text citation specified formatting CSL style',
)
parser.add_argument(
    "-b",
    "--bibtex",
    required=False,
    action="store_true",
    help="return bibtex with a shortdoi-based unique bibtex key",
)
parser.add_argument(
    "-j",
    "--json",
    required=False,
    action="store_true",
    help="return citeproc-JSON",
)
parser.add_argument("identifier", nargs=1, help="DOI, link or webpage with DOI content")

args = parser.parse_args()


def _extract_doi(item):
    """Extract or provide DOI only."""
    if item.startswith("10."):
        return item
    elif item.startswith("doi:"):
        return item[4:]
    elif item.startswith("https://doi.org/"):
        return item[16:]
    elif item.startswith("http://doi.org/"):
        return item[15:]
    elif item.startswith("doi.org/"):
        return item[8:]
    else:
        # Try to find the DOI from a Journal's webpage meta data attributes.
        r = requests.get(item)
        tree = html.fromstring(r.content)
        doi = None
        for i in tree.xpath("//meta"):
            if "name" in i.attrib and i.attrib["name"].lower() in doi_fields:
                doi = _extract_doi(i.attrib["content"])
                break
        return doi


def _short_doi(doi):
    r = requests.get("http://shortdoi.org/{}?format=json".format(doi))
    return r.json()["ShortDOI"]


def main():
    doi = _extract_doi(args.identifier[0])

    if doi is None:
        print(args.identifier[0])
    elif args.bibtex:
        headers = {"Accept": "application/x-bibtex"}
        r = requests.get(f"https://doi.org/{doi}", headers=headers)
        content = r.content.decode("UTF-8")
        bibtex = parse_string(content, "bibtex")
        try:
            name = "".join(bibtex.entries.values()[0].persons.values()[0][0].last_names)
            name = name.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue")
            name = slugify(name, lowercase=False, separator="")
            shortdoi = _short_doi(doi)[3:]
            year = bibtex.entries.values()[0].fields["year"]
            key = "{}_{}_{}".format(name, year, shortdoi)
            bibtex.entries.values()[0].fields["url"] = urllib.parse.unquote(
                bibtex.entries.values()[0].fields["url"]
            )
            new = BibliographyData()
            new.add_entry(key, bibtex.entries[bibtex.entries.keys()[0]])
            print(new.to_string("bibtex"))
        except KeyError:
            print(doi)
            sys.exit(1)

    elif args.json:
        headers = {'Accept': 'application/vnd.citationstyles.csl+json'}
        r = requests.get(f"https://doi.org/{doi}", headers=headers)
        content = r.content.decode("UTF-8")
        print(content)
    else:
        headers = {"Accept": f"text/x-bibliography; style={args.style}"}
        r = requests.get(f"https://doi.org/{doi}", headers=headers)
        if r.status_code == 200:
            print(r.content.decode("UTF-8"))
        else:
            print(doi)
            sys.exit(1)
