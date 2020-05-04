import os

import pytest

from cite import _read_bibtex_entry, _use_short_doi_key

examples = {
    """@article{Le_Qu_r__2018,
  doi = {10.5194/essd-10-2141-2018},
  year = 2018,
  author = {Corinne Le Qu{\'{e}}r{\'{e}} and Robbie M. Andrew}
""": """@article{LeQuere_2018_gfn48b,
  doi = {10.5194/essd-10-2141-2018},
  year = 2018,
  author = {Corinne Le Qu{\'{e}}r{\'{e}} and Robbie M. Andrew}
""",
    """@article{G_tschow_2016,
  doi = {10.5194/essd-2016-12},
  url = {https://doi.org/10.5194%2Fessd-2016-12},
  year = 2016
}
""": """@article{Guetschow_2016_gcdqfd,
  doi = {10.5194/essd-2016-12},
  url = {https://doi.org/10.5194%2Fessd-2016-12},
  year = 2016
}
""",
}

# Avoids relying on services being up and speeds up CI by skipping these
# potentially slow checks.
@pytest.mark.skipif(
    ("GITHUB_ACTIONS" in os.environ), reason="Only needed for local testing"
)
def test_key_generation():
    for old, new in examples.items():
        print(old)
        print(new)
        assert _use_short_doi_key(old) == new


def test_read_entry():
    assert _read_bibtex_entry('volume = "10",') == ("volume", "10")
    assert _read_bibtex_entry("volume = {10}") == ("volume", "10")
