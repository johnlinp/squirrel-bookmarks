from setuptools import setup

setup(name='squirrel-bookmarks',
    version='0.1.0',
    description='Bookmark system between development branches.',
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
