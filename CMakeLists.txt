cmake_minimum_required(VERSION 2.8)
Project("proj3")

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(proj3 proj3/src/main.cpp)
target_link_libraries(proj3 ${CONAN_LIBS})
