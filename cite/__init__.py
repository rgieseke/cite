import argparse
import requests
from requests_html import HTMLSession
from habanero import cn

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
    help='Return citation data in specified format: "rdf-xml", "turtle", "citeproc-json", "citeproc-json-ish", "text" (Default), "ris", "bibtex" , "crossref-xml", "datacite-xml","bibentry", or "crossref-tdm"',
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


def main():
    for item in args.ids:
        doi = _extract_doi(item)

        if doi is None:
            print(item)
            print()
        else:
            try:
                result = cn.content_negotiation(doi, format=args.format)
                print(result)
            except requests.exceptions.HTTPError:
                print(doi)
                print()

