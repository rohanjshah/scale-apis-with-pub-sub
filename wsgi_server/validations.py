'''
Created on 08-Mar-2016

@author: Rohan Shah
'''
from bottle import abort

def validate_sum_inputs(val1, val2):
    '''
    Validates Sum Inputs and raises 500 error in case of 
    Input issue.
    '''
    # validate inputs
    try:
        val1 = float(val1)
        val2 = float(val2)
    except ValueError:
        abort('Input is not float convertible')