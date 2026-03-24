#include <pybind11/pybind11.h>
#include "qfin/black_scholes.hpp"

namespace py = pybind11;

PYBIND11_MODULE(qfin_cpp, m) {
    m.def(
        "black_scholes_call",
        &qfin::black_scholes_call,
        py::arg("spot"),
        py::arg("strike"),
        py::arg("time_years"),
        py::arg("rate"),
        py::arg("vol"));
    m.def(
        "monte_carlo_call",
        &qfin::monte_carlo_call,
        py::arg("spot"),
        py::arg("strike"),
        py::arg("time_years"),
        py::arg("rate"),
        py::arg("vol"),
        py::arg("paths"),
        py::arg("seed") = 42);
}
