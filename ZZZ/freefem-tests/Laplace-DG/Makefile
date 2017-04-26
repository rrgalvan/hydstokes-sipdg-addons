edp_script=LaplaceDG-SIP.edp
tests_py=run_tests.py

run: $(edp_script)
	FreeFem++ $(edp_script)

tests: $(tests_py) $(edp_script)
	nosetests3 --nocapture $(tests_py)
