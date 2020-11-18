# Geduld


Requirements
---

- Python3.6+  (On Mac OS run `brew install python3`, other platforms see http://www.python.org/downloads/)

- bearlibterminal
    `pip3 install bearlibterminal`

To play, first clone the repo, `git clone git@github.com:akulakov/geduld.git`; then run `python3 geduld.py`

## Gameplay hints

# Commands

## Move

    h - move left

    l - move right

    k - move up

    j - move down

    H and L - run

## Other

    ? - HELP
    space - action
    u - use item
    i - inventory
    . - wait

    S - save game
    o - load game
    Q - quit

# Window Size

-s arg can be used to adjust tile size and therefore window size
Default is 24, so to make a smaller window, you can run, e.g.:

    python3 geduld.py -s18
