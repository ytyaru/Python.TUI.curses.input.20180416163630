import curses
def main(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, 'echo mode. Please input some text. Exit [Enter] key.')
    curses.echo()
    # カーソル移動すると消されてしまう
    s = stdscr.getstr(1, 0)
    stdscr.addstr(2, 0, '{}'.format(s))
    stdscr.addstr(3, 0, '{}'.format(s.decode('utf-8')))
    stdscr.addstr(4, 0, 'Exit. press any key.')
    stdscr.getkey()
curses.wrapper(main)
