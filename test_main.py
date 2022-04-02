from io import StringIO
#from main import *
from main import mode_selection_function 
import main
import random
import pytest

def test_function(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO("r\n2+2\n"))
    mode_selection_function()
    assert main.modes_history[:-1] == "Real Mode"
