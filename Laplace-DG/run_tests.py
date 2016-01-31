from nose.tools import assert_not_equal, assert_almost_equal
from nose.tools import with_setup

import subprocess

output="" # Global variable to be used by test functions

def setup_function():
    "Setup code needed by most tests"
    global output
    edp_script = "LaplaceDG-SIP.edp"
    output = subprocess.check_output(["FreeFem++", edp_script])
    output = output.split('\n')
    # Assert that 'FreeFem++' substring is found in first output line
    assert_not_equal(output[0].find('FreeFem++'), -1)

def read_DG_CG_errors_from_line(i,n):
    iDGerror = i+3 # Line where DG error was printed
    line = output[iDGerror]
    line = line.split('=')
    errorDG = float(line[1])

    iCGerror = i+4 # Line where CG error was printed
    line = output[iCGerror]
    line = line.split('=')
    errorCG = float(line[1])

    return[errorDG, errorCG]

@with_setup(setup_function)
def test_laplace_errors_n8():
    "Test Laplace DG Errors for n=8 (mesh size)"
    test_pass = False

    # String defining the start of data lines
    test_start_strings = ["Test, n=8", "Test, n=16"]
    expected_
    # Number of data lines
    test_n_data_lines = 4

    for i in xrange(len(output)):
        line = output[i]
        # Find a line where a target data starts
        for s in test_start_strings:
            if(line.find(s) != -1):
                n = test_n_data_lines
                # Build a dictionary from wollowing n lines
                d = dict(item.split(':') for item in output[i+1:i+n+1])
                # Extract data from the dictionary and assert data is OK
                errorDG = float(d[r'DG error L2'])
                errorCG = float(d[r'CG error L2'])
                assert_almost_equal(errorDG, errorCG, places=1)
                test_pass = True
                break
    assert(test_pass)
