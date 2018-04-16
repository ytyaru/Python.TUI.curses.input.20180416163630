# input

種類|概要
----|----
`window.getch()`|キーをintで取得
`window.getkey()`|キーを文字で取得
`curses.echo()`|`window.getstr()`で入力したテキストを取得。カーソル移動すると文字が消える。
`curses.textpad.Textbox(window)`|emacs風。日本語入力できない。

デフォルトではまともに日本語入力できるAPIがない。`echo()`なら可能だが、カーソル移動ができない。やると文字が削除される。

エディタを自作するしか無い。非常に大変そう。

https://torina.top/detail/439/

