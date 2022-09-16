'''
Testing functions in utils.py
'''

from app.utils.utils import analyse_data

def test_analyse_data():
    '''Test that analyse_data() returns same string as input'''
    assert analyse_data('data') == 'data'


