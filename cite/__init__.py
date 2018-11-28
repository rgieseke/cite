import argparse
import json
import requests

from requests_html import HTMLSession
from habanero import cn
from unidecode import unidecode

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
    "--format",
    default="text",
    required=False,
    help='Return citation data in specified format: "rdf-xml", "turtle", "citeproc-json", "citeproc-json-ish", "text" (Default), "ris", "bibtex" , "crossref-xml", "datacite-xml","bibentry", or "crossref-tdm"',
)
parser.add_argument(
    "--bibtex",
    required=False,
    action="store_true",
    help='Return bibtex',
)
parser.add_argument("ids", nargs="+", help="One or more DOIs")

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
    else:
        # Try to find the DOI from a Journal's webpage meta data attributes.
        session = HTMLSession()
        r = session.get(item)
        doi = None
        for i in r.html.find("meta"):
            if "name" in i.attrs and i.attrs["name"].lower() in doi_fields:
                doi = _extract_doi(i.attrs["content"])
                break
        return doi


def _short_doi(doi):
    r = requests.get("http://shortdoi.org/{}?format=json".format(doi))
    return r.json()["ShortDOI"]


def main():
    for item in args.ids:
        doi = _extract_doi(item)

        if doi is None:
            print(item)
        elif args.bibtex:
            result = json.loads(
                cn.content_negotiation(doi, format="citeproc-json")
            )
            name = unidecode(result["author"][0]["family"])
            shortdoi = _short_doi(doi)[3:]
            year = result["issued"]["date-parts"][0][0]
            print("{}_{}_{}".format(name, year, shortdoi))
        else:
            try:
                result = cn.content_negotiation(doi, format=args.format)
                print(result)
            except requests.exceptions.HTTPError:
                print(doi)
        print()
