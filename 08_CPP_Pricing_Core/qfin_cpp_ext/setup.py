from pathlib import Path

from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

HERE = Path(__file__).resolve().parent
CPP = HERE.parent / "cpp"

ext_modules = [
    Pybind11Extension(
        "qfin_cpp",
        [
            str(HERE / "bindings.cpp"),
            str(CPP / "src" / "black_scholes.cpp"),
        ],
        include_dirs=[str(CPP / "include")],
        cxx_std=17,
    ),
]

setup(
    name="qfin-cpp",
    version="0.1.0",
    author="Q-Fin Portfolio",
    description="Black-Scholes and Monte Carlo kernels (pybind11)",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.9",
)
