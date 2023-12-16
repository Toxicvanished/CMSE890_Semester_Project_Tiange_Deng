import pytest
import workflow_functions

sample_list = {
    "CONTRL": [
        "SCFTYP",
        "MPLEVL",
        "CITYP",
        "CCTYP",
        "RUNTYP",
        "EXETYP",
        "ICHARG",
        "MULT",
        "COORD",
        "UNITS",
        "ISPHER",
        "MAXIT",
        "NPRINT",
        "ICUT",
    ],
    "SYSTEM": ["MWORDS", "MEMDDI"],
    "BASIS": ["GBASIS", "NGAUSS"],
    "SCF": [
        "DIRSCF",
        "DIIS",
        "SOSCF",
        "NOCONV",
        "CONV",
        "COUPLE",
        "F",
        "ALPHA",
        "BETA",
    ],
    "CCINP": ["MAXCC", "NCORE", "NFZV", "ACP(1)", "NACTO", "NACTU"],
}


def test_read_keyword_list():
    assert workflow_functions.read_keyword_list("Category_keywords.csv") == sample_list
