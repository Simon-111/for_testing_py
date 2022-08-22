import sys
sys.path.append('.')
sys.path.append('..')

import pytest
from code import myfunc

def test_func():
    assert myfunc(13) == 'gazonrnin'
