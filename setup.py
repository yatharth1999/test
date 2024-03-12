from setuptools import setup

setup(
    name='test',
    version='0.0.1',
    description='My private package from private github repo',
    url='git@github.com:yatharth1999/test.git',
    author='Yatharth Vohra',
    author_email='yatharth.vohra@gmail.com',
    license='unlicense',
    packages=['test'],
    zip_safe=False
)