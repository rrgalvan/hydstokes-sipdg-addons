#!/usr/bin/env bats

## Simple automated test suite in the bash command. It is based on
## bats <https://github.com/sstephenson/bats>.


setup() {
    # Run FreeFem++. Output is stored by bats in the array @{lines[]}
    run FreeFem++-nw ./LaplaceDG-SIPG.edp
}

@test "Check that total is listed" {
    run ls -l
    [[ ${lines[0]} =~ "total" ]]
}

@test "A test" {
    [[ ${lines[-1]} =~ "CG error L2: 0.0138518" ]]
}
