import curses
def main(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, 'getkey(). Please press any key. Exit with [q] key.')
    c = ''
    while 'q' != c:
        c = stdscr.getkey()
        stdscr.addstr(1, 0, '{}'.format(c))
        stdscr.refresh()
    stdscr.addstr(3, 0, 'Exit. press any key.')
    stdscr.getkey()
curses.wrapper(main)
