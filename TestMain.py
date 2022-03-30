from io import StringIO
from main import *
#from main import mode_selection_function 
#import main 
import random
import pytest

def testmode_selection_function(monkeypatch):
    number_inputs = StringIO("real")
    monkeypatch.setattr('sys.stdin', number_inputs)
    assert mode_selection_function != "real"

