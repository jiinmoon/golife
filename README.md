golife : Conway's Game of Life
==============================

Introduction
------------

![Gosper's glider gun pattern](https://upload.wikimedia.org/wikipedia/commons/e/e5/Gospers_glider_gun.gif)

Here is a brief description of **Conway's [Game of Life][]** from Wikipedia:


> The **Game of Life**, also known simply as **Life**, is a cellular automaton devised
> by the British mathematician John Horton Conway in 1970. It is a zero-player
> game, meaning that its evolution is determined by its initial state,
> requiring no further input. One interacts with the Game of Life by creating
> an initial configuration and observing how it evolves. It is Turing complete
> and can simulate a universal constructor or any other Turing machine.


It is one of more intersting topics not only in Computer Science but also
within the programming community - for it is facinating to observe how little
deviation in the initial condition can propagate and disrupt the entire system.

This project is a self-interest driven study project focused on creating the
simulation environment for _Game of Life_ in Python3.

How To Run 
----------

_The basic usage is covered with `python golife.py -h`_.

The application runs in three "modes" - "random", "template" and "gif":

`python golife.py random`

![example-of-running-in-random-mode](./resources/running_in_random.gif)

_Random_ mode is as the name implies simulates the game of life with the
randomized starting template. It uses `curses` to display the board onto the
terminal, and it can be terminated at anytime with `CRTL + C`. If the provided
`WIDTH` and `HEIGHT` parameters exceed the current window size, then it will
default to the safe value of 10.

`python golife.py template`

todo

`python golife.py gif`

todo


TODO
----

- Give project a better structure.
- Finish template mode.
- Finish .gif export mode.


Contacts
--------

Author's homepage is <http://jiinmoon.com>.

My email is [jmoon@tutanota.com](mailto::jmoon@jiinmoon.com).

I am also available at
[#jmoon:matrix.org](https://matrix.to/#/!oXEFoxrdcJbExYsHWu:matrix.org?via=matrix.org).

Sources
-------

A single Gosper's glider gun creating gliders image was used under terms of GNU
Free Documentation License.

[Game of Life]: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life "Wikipedia: Game of Life"
