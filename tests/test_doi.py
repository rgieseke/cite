from cite import _extract_doi


def test_doi_only():
    assert _extract_doi("10.1103/physrev.48.73") == "10.1103/physrev.48.73"


def test_doi_prefix():
    assert _extract_doi("doi:10.1103/physrev.48.73") == "10.1103/physrev.48.73"


def test_doi_url():
    assert (
        _extract_doi("http://doi.org/10.1103/physrev.48.73") == "10.1103/physrev.48.73"
    )
    assert (
        _extract_doi("https://doi.org/10.1103/physrev.48.73") == "10.1103/physrev.48.73"
    )
    assert _extract_doi("doi.org/10.1103/physrev.48.73") == "10.1103/physrev.48.73"
