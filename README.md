# Squirrel Bookmarks

Bookmark system between development branches.


## Why?

When I am at work, it's common to work on multiple development branches simultaneously.

For example, when I am developing a new feature on a feature branch `feature-param-validation`, I want
to run a local environment of production branch `production`. Meanwhile, our QA found a critical bug on
the other feature branch `feature-remove-tokens`.

What do I do?

Single clone of the working repository is not enough for me. So I clone multiple copies of the
repositories in my local machine. You can see many directories in the directory of my `~/dev`, and
each directory is a development branch, e.g. `feature-param-validation`, `feature-remove-tokens`,
`production`, etc.

Then it's time for Squirrel Bookmarks. Basically it can do the following 2 things:

- Switch to a bookmark quickly: When I am doing my development, there are some directories that
I frequently `cd` into. For example, I often `cd` into `client-side/js/components` and `server-side/src/resources`.
So I need bookmarks for those directories.

- Switch to a branch quickly:  I also want to switch between branches quickly. As mentioned above, I have
multiple branches: `feature-param-validation`, `feature-remove-tokens`, `production`, etc.

Example usage will be like:

```
$ sq feature-param-validation
jump to /Users/johnlinp/dev/feature-param-validation
$ sq components
jump to /Users/johnlinp/dev/feature-param-validation/client-side/js/components
$ cd checkbox
$ pwd
/Users/johnlinp/dev/feature-param-validation/client-side/js/components/checkbox
$ sq production
jump to /Users/johnlinp/dev/production/client-side/js/components/checkbox
$ sq resources
jump to /Users/johnlinp/dev/production/server-side/src/resources
```


## Requirement

Currently only supports Python 3.5+.


## Install

Please type:

```
$ sudo pip3 install squirrel-bookmarks
```

to install.


## Setup

You have to setup config and the `sq` bash function first.


### Setup Config

Please type:

```
$ squirrel init
```

to initialize your bookmark config.
After that, please edit the config at `~/.squirrel.json` to meet your needs.


### Setup `sq` function

Please type:

```
$ squirrel bashrc
```

to show the bashrc script and then copy/paste into your `~/.bashrc` file.

Alternatively, you can do the following:

```
$ squirrel bashrc >> ~/.bashrc
```

or if you have `~/.bashrc.d/`, you can type:

```
$ squirrel bashrc > ~/.bashrc.d/squirrel.bash
```


## Usage

When you want to jump to a branch called `production`, please type:

```
$ sq production
```

When you want to jump to a bookmark named `components`, please type:

```
$ sq components
```
