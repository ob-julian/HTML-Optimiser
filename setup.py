from setuptools import setup, find_packages

setup(
    name='html_optimiser',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'minify_html',
        'requests',
        # 'tkinter' is part of the standard library
    ],
    description='Optimizes HTML, JS, CSS, and JSON files in a directory.',
    author='Your Name',
    python_requires='>=3.8',
)
