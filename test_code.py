import sys
sys.path.append('.')
sys.path.append('..')

from code import myfunc

def test_func():
    assert myfunc(13) == 'gazornin'