from setuptools import setup

setup(
    name="math_to_spoken_text",
    version="0.0.1",
    description="Package to convert math expression to spoken text",
    url="git@github.com:Hrushikesh777/math_to_spoken_text.git",
    author="Hrushikesh Vanga",
    author_email="",
    license="unlicense",
    py_modules=["math_to_spoken_text"],
    install_requires=[
        "latex2sympy2 @ git+https://github.com/Hrushikesh777/latex2sympy.git#egg=latex2sympy2"
    ],
)