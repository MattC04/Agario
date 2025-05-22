# CMake generated Testfile for 
# Source directory: /Users/rosiechen/AgarLE
# Build directory: /Users/rosiechen/AgarLE/build/temp.macosx-11.1-arm64-cpython-311
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test([=[OpenAI-Gym]=] "python" "-m" "tests")
set_tests_properties([=[OpenAI-Gym]=] PROPERTIES  WORKING_DIRECTORY ".." _BACKTRACE_TRIPLES "/Users/rosiechen/AgarLE/CMakeLists.txt;36;add_test;/Users/rosiechen/AgarLE/CMakeLists.txt;0;")
subdirs("agario")
subdirs("environment")
subdirs("utils")
subdirs("bench")
