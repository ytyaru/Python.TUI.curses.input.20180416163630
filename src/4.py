import curses
import curses.textpad
def main(stdscr):
    stdscr.clear()
    textbox = curses.textpad.Textbox(stdscr)
    # 日本語入力できない
    textbox.edit()
    stdscr.getkey()
curses.wrapper(main)
