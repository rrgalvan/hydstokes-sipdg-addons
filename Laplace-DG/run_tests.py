from nose.tools import assert_not_equal, assert_almost_equal
from nose.tools import with_setup

import subprocess

freefem_output="" # Global variable to be used by test functions
last_index=0 # Globas variable, for avoid starting from zero

def setup_function():
    "Setup code needed by most tests"
    global freefem_output
    edp_script = "LaplaceDG-SIP.edp"
    freefem_output = subprocess.check_output(["FreeFem++", edp_script])
    freefem_output = freefem_output.split('\n')
    # Assert that 'FreeFem++' substring is found in first output line
    assert_not_equal(freefem_output[0].find('FreeFem++'), -1)

def read_data(all_lines, heading_line, nb_data_lines, start=0, data_separator='='):
    """Read data contained in the list of strings 'all_lines'

    This function reads lines from 'all_lines', searching (from the one
    with index start) for one containing the string contained in
    heading_line. The following nb_data_lines lines are supposed to store
    data formatted as

    key = value

    Other data separators (not only '=') are allowed. Data is read in a dictionary.
    Function returns a list containing the dictionary and the number of line where
    heading_line was found.
    """

    d = dict()
    for i in xrange(len(all_lines)):
        line = all_lines[i]
        if(line.find(heading_line) != -1): # Found heading line
            d = dict( item.split(data_separator)
                      for item in all_lines[i+1: i+nb_data_lines+1] )
            break
    return [d, i]

@with_setup(setup_function)
def test_laplace_errors():
    "Test DG vs CG errors for the Laplace problem"
    global last_index # For avoid start searching lines from zero
    nb_data_lines = 4 # Number of data lines for each test output
    data_separator='=' # Separator defining (key, value)

    # List of tests. Each element contains a dictionary with:
    # - A string defining the start of data lines
    # - A floating point defining the nb. of exact digits after decimal point
    list_of_tests = [
        {
        'id_string': 'Test, n=8',
        'fp_places': 1
        }, {
        'id_string': 'Test, n=16',
        'fp_places': 2
        }, {
        'id_string': 'Test, n=32',
        'fp_places': 2
        }, {
        'id_string': 'Test, n=64',
        'fp_places': 3
        }, {
        'id_string': 'Test, n=128',
        'fp_places': 4
        }
    ]
    for test in list_of_tests:
        [d, last_index] = read_data(freefem_output,
                                    heading_line=test['id_string'],
                                    nb_data_lines=4,
                                    start=last_index)
        errorDG = float( d['DG error L2'] )
        errorCG = float( d['CG error L2'] )
        try:
            assert_almost_equal(errorDG, errorCG, places=test['fp_places'])
        except Exception, e:
            print "Error in test '%s'" % (test['id_string'])
            raise e
