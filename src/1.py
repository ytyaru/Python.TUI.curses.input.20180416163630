import curses
def main(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, 'getch(). Please press any key. Exit with [q] key.')
    c = 0
    while 0x71 != c:
        c = stdscr.getch()
        stdscr.addstr(1, 0, '10進数: {0:d}'.format(c))
        stdscr.addstr(2, 0, '16進数: 0x{0:X}'.format(c))
        stdscr.refresh()
    stdscr.addstr(3, 0, 'Exit. press any key.')
    stdscr.getkey()
curses.wrapper(main)
