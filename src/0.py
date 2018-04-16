import curses
def main(stdscr):
    stdscr.clear()
    #print(c)
    stdscr.addstr(0, 0, 'Please press any key. Exit with [q] key.')
    c = stdscr.getch()
    stdscr.addstr(1, 0, '10進数: {0:d}'.format(c))
    stdscr.addstr(2, 0, '16進数: 0x{0:X}'.format(c))
    stdscr.refresh()
    stdscr.getkey()
curses.wrapper(main)
