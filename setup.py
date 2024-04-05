from setuptools import setup, find_packages

setup(
    name='lr72axon',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    author='Marcos Schejtman',
    author_email='marcos.schejtman@gmail.com',
    description='A library to migrate objects from LogRhythm7 to LogRhythm Axon',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/natashell666/lr72axon",
    install_requires=[
        'requests', 'torch', 'scikit-learn', 'sentence-transformers', 'setuptools'
    ],
)
