# SemiGenre

The SemiGenre library provides a Python interface for tagging and comparing music in a personal audio library. The purpose of SemiGenre is primarily to discover structure in musical preferences through [semi-supervised](https://en.wikipedia.org/wiki/Semi-supervised_learning) machine learning. Genres are not always the best way to talk about musical taste and SemiGenre aims to personalize the process of music recommendation by digging into the details of the music you care about most.

[![CircleCI](https://circleci.com/gh/gregorybchris/semigenre/tree/master.svg?style=svg)](https://circleci.com/gh/gregorybchris/semigenre/tree/master)

## Installation

Install the current PyPI release:

```python
pip install semigenre
```

Or install from source:

```python
pip install git+https://github.com/gregorybchris/semigenre
```


## Dependencies

To enable full use of the `semigenre.audio` module, install [VLC Media Player](https://download.cnet.com/VLC-Media-Player/3000-13632_4-10210434.html). The rest of the SemiGenre package will still work if you do not intend to listen to music through the SemiGenre media player.

## Usage

In order to seed the SemiGenre package with personalized information, run the rating CLI and follow the prompts.

```python
from semigenre.audio.library import Library
from semigenre.rating.cli import RatingCLI

library = Library('path/to/library.xml')
RatingCLI(library).run()
```

This package is currently in beta and interfaces are subject to change.