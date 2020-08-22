# woody-puzzel

_pronounced "wood-ee puh-ZELL"_

**woody-puzzel** is a command-line clone of the popular mobile game
[Woody Puzzle][]. It's also a platform for building and testing machine
learning algorithms that play the game.

At least, that's what we *want* it to be. Right now, it's just an idea and some
code.

## Installation

 1. Clone this repo. `git clone https://github.com/loboyd/woody-puzzel.git`
 2. (*optional*) Set up a [virtual environment][].
 3. Install dependencies. `cd woody-puzzel; pip install -r requirements.txt`
 4. Run the game. `./main.py`

## Documentation

**woody-puzzel** ships with `pdoc`. To generate HTML documentation, run

```
cd woody-puzzel
pdoc .
```

To view the documentation, navigate to `./html/woody-puzzel/index.html` in a
web browser.

[Woody Puzzle]: https://www.woodypuzzle.com/
[virtual environment]: https://realpython.com/python-virtual-environments-a-primer/
