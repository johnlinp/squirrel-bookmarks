import os
from setuptools import setup

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='squirrel-bookmarks',
    version='0.1.2',
    description='Bookmark system between development branches.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='johnlinp',
    author_email='johnlinp@gmail.com',
    url='https://github.com/johnlinp/squirrel-bookmarks',
    license='New BSD License',
    python_requires='>=3.5',
    scripts=['bin/squirrel'],
    data_files=[
        ('etc/bash_completion.d', ['etc/bash_completion.d/sq'])
    ]
)
