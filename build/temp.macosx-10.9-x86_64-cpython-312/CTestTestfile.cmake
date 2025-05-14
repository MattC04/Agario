# CMake generated Testfile for 
# Source directory: /Users/heleny/Documents/GitHub/AgarLE
# Build directory: /Users/heleny/Documents/GitHub/AgarLE/build/temp.macosx-10.9-x86_64-cpython-312
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test([=[GameEngine]=] "agario/test-engine")
set_tests_properties([=[GameEngine]=] PROPERTIES  _BACKTRACE_TRIPLES "/Users/heleny/Documents/GitHub/AgarLE/CMakeLists.txt;25;add_test;/Users/heleny/Documents/GitHub/AgarLE/CMakeLists.txt;0;")
add_test([=[GameEngine-Renderable]=] "agario/test-engine-renderable")
set_tests_properties([=[GameEngine-Renderable]=] PROPERTIES  _BACKTRACE_TRIPLES "/Users/heleny/Documents/GitHub/AgarLE/CMakeLists.txt;28;add_test;/Users/heleny/Documents/GitHub/AgarLE/CMakeLists.txt;0;")
add_test([=[LearningEnvironment]=] "environment/test-envs")
set_tests_properties([=[LearningEnvironment]=] PROPERTIES  _BACKTRACE_TRIPLES "/Users/heleny/Documents/GitHub/AgarLE/CMakeLists.txt;31;add_test;/Users/heleny/Documents/GitHub/AgarLE/CMakeLists.txt;0;")
add_test([=[OpenAI-Gym]=] "python" "-m" "tests")
set_tests_properties([=[OpenAI-Gym]=] PROPERTIES  WORKING_DIRECTORY ".." _BACKTRACE_TRIPLES "/Users/heleny/Documents/GitHub/AgarLE/CMakeLists.txt;36;add_test;/Users/heleny/Documents/GitHub/AgarLE/CMakeLists.txt;0;")
subdirs("agario")
subdirs("environment")
subdirs("utils")
subdirs("bench")
