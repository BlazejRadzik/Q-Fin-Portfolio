cmake_minimum_required(VERSION 3.16)
project(qfin_numerical_kernels LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_library(qfin_bs STATIC
    src/black_scholes.cpp
)
target_include_directories(qfin_bs PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/include
)

add_executable(bs_demo tools/bs_demo.cpp)
target_link_libraries(bs_demo PRIVATE qfin_bs)
