import argparse

from habanero import cn

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions


parser = argparse.ArgumentParser(description="cite - get citation for DOI.")
parser.add_argument(
    "--format",
    default="text",
    help='Return citation data in specified format: "rdf-xml", "turtle", "citeproc-json", "citeproc-json-ish", "text" (Default), "ris", "bibtex" , "crossref-xml", "datacite-xml","bibentry", or "crossref-tdm"',
)
parser.add_argument("ids", nargs="*", help="Ond or more DOIs")

args = parser.parse_args()


def main():
    items = []
    for item in args.ids:
        items.append(
            item.replace("http://doi.org/", "")
            .replace("https://doi.org/", "")
            .replace("doi:", "")
        )
    results = cn.content_negotiation(items, format=args.format)
    if type(results) is str:
        print(results)
    else:
        for result in results:
            print(result)
