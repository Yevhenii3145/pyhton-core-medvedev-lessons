from setuptools import setup, find_namespace_packages

setup(
    name="package_crab_124_gg_name",
    version="0.2.0",
    description="This is my first test package",
    url="https://github.com/Yevhenii3145/python-core-medvedev-lessons",
    author='Eugen',
    author_email='zakolochennoe457@gmail.com',
    license='Apache',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': [
        'package_crab_123 = src.package_crab_123_gg:hello_world']},
)
