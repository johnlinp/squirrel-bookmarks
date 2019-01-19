# Squirrel Bookmarks

Bookmark system between development branches.


## Requirement

Currently only supports Python 3.5+.


## Install

Please type:

```
$ pip3 install squirrel-bookmarks
```

to install.


## Setup

Please type:

```
$ squirrel init
```

to initialize your bookmark config.
After that, please edit the config at `~/.squirrel.json` to meet your needs.

Then type:

```
$ squirrel bashrc
```

to show the bashrc script and then copy/paste into your bashrc.


## Usage

When you want to jump to a branch called `stable`, please type:

```
$ sq stable
```

When you want to jump to a bookmark named `ui`, please type:

```
$ sq ui
```
