from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

version = '0.0.0'
try:
    import design_patterns
    version = design_patterns.__version__
except ImportError:
    pass

tests_require = [
    'pytest',
    'pytest-cov',
    'pytest-xdist',
    'pytest-capturelog',
]

setup(
    name='design-patterns',
    description='Useful design patterns for Python',
    keywords='design patterns',
    author='Victor Lin',
    author_email='hello@victorlin.me',
    url='https://github.com/victorlin/design-patterns',
    license='MIT',
    version=version,
    packages=find_packages(exclude=('tests', )),
    install_requires=[
    ],
    extras_require=dict(
        tests=tests_require,
    ),
    tests_require=tests_require,
)
