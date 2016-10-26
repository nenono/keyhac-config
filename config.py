# -*- mode: python; coding: utf-8-with-signature-dos -*-

##
## Windows の操作を emacs のキーバインドで行うための設定（Keyhac版）ver.20160519_01
##

# このスクリプトは、Keyhac for Windows ver 1.70 以降で動作します。
#   https://sites.google.com/site/craftware/keyhac-ja
# スクリプトですので、使いやすいようにカスタマイズしてご利用ください。
#
# この内容は、utf-8-with-signature-dos の coding-system で config.py の名前でセーブして
# 利用してください。
#
# 本設定を利用するための仕様は、以下を参照してください。
#
# ＜共通＞
# ・日本語と英語のどちらのキーボードを利用するかを is_japanese_keyboard 変数で指定できる。
# ・左右どちらの Ctrlキーを使うかを side_of_ctrl_key 変数で指定できる。
# ・左右どちらの Altキーを使うかを side_of_alt_key 変数で指定できる。
# ・is_emacs_target 変数と is_ime_target 変数で、emacsキーバインドや IME の切り替え
#   キーバインドの対象とするアプリケーションソフトを指定できる。
# ・キーバインドの定義では以下の表記が利用できる。
#   ・S-    : Shiftキー
#   ・C-    : Ctrlキー
#   ・A-    : Altキー
#   ・M-    : Altキー と Esc、C-[ のプレフィックスキーを利用する３パターンを定義
#             （emacs キーバインド設定で利用可。emacs の Meta と同様の意味。）
#   ・Ctl-x : ctl_x_prefix_key 変数で定義されているプレフィックスキーに置換え
#             （emacs キーバインド設定で利用可。変数の意味は以下を参照のこと。）
#   ・(999) : 仮想キーコード指定
#
# ＜emacs キーバインド設定を有効にしたアプリケーションソフトでの動き＞
# ・use_emacs_ime_mode 変数の設定により、emacs日本語入力モードを使うかどうかを指定
#   できる。emacs日本語入力モードは、IME が ON の時に文字（英数字と、スペースを除く
#   特殊文字）を入力すると起動する。
#   emacs日本語入力モードでは、以下のキーのみが emacsキーバインドとして利用でき、
#   その他の文字は Windows にそのまま渡されるようになるため IME のショートカットを
#   利用することができる。
#   ・emacs日本語入力モードで使える emacsキーバインドキー
#     ・C-[
#     ・C-b、C-f
#     ・C-p、C-n
#     ・C-h
#     ・C-m
#     ・C-g
#   emacs日本語入力モードは、以下のキーの押下で終了する。
#   ・emacs日本語入力モードを終了するキー
#     ・Enter、C-m
#     ・C-g
#     ・BS、C-h、Esc 押下直後に toggle_input_method_key 変数に設定されているキーが
#       押された場合（間違って日本語入力をしてしまった時のキー操作を想定しての対策）
#   なお、toggle_emacs_ime_mode_key 変数の設定により、明示的に emacs日本語入力モードを
#   切り替える（トグルする）キーを指定できる。このキーも emacs日本語入力モードで
#   Windowsショートカットとして使えるキーから除外される。
# ・use_emacs_shift_mode 変数の設定により、emacsシフトモードを使うかどうかを指定できる。
#   emacsシフトモードを使う場合は以下の動きとなる。
#   ・C-[a-z]キーを Shiftキーと一緒に押した時は、Shiftキーをとったキー（C-[a-z]）が
#     Windows に入力される。
#   ・A-[a-z]キーを Shiftキーと一緒に押した時は、Shiftキーをとったキー（A-[a-z]）が
#     Windows に入力される。
# ・toggle_input_method_key 変数の設定により、IME を切り替えるキーを指定できる。
# ・use_esc_as_meta 変数の設定より、Escキーを Metaキーとして使うかどうかを指定できる。
#   use_esc_as_meta 変数が True（Metaキーとして使う）に設定されている場合、ESC の
#   二回押下で ESC が入力される。
# ・ctl_x_prefix_key 変数の設定により、Ctl-xプレフィックスキーに使うキーを指定できる。
# ・scroll_key 変数の設定により、スクロールに使うキーを指定できる。
# ・C-c、C-z は、Windows の「コピー」、「取り消し」が機能するようにしている。
#   ctl_x_prefix_key 変数が C-x 以外に設定されている場合には、C-x が Windows の
#   「カット」として機能するようにしている。
# ・C-k を連続して実行しても、クリップボードへの削除文字列の蓄積は行われない。
#   C-u による行数指定をすると、削除行を一括してクリップボードに入れることができる。
# ・C-l は、アプリケーションソフト個別対応とする。recenter 関数で個別に指定すること。
#   この設定では、Sakura Editor のみ対応している。
# ・キーボードマクロは emacs の挙動と異なり、IME の変換キーも含めた入力したキーそのものを
#   記録する。このため、キーボードマクロ記録時や再生時、IME の状態に留意した利用が必要。
#
# ＜IME の切り替え設定のみを有効にしたアプリケーションソフトでの動き＞
# ・toggle_input_method_key 変数の設定により、IME を切り替えるキーを指定できる。
#
# ＜全てのアプリケーションソフトで共通の動き＞
# ・other_window_key 変数に設定したキーにより、表示しているウインドウの中で、一番最近
#   までフォーカスがあったウインドウに移動する。NTEmacs の機能やランチャーの機能から
#   Windows アプリケーションソフトを起動した際に、起動元のアプリケーションソフトに戻る
#   のに便利。この機能は Ctl-x o にも割り当てているが、こちらは emacs のキーバインドを
#   適用したアプリケーションソフトのみで有効となる。
# ・clipboardList_key 変数に設定したキーにより、クリップボードリストが起動する。
#   （C-f、C-b でリストの変更、C-n、C-p でリスト内を移動し、Enter で確定する。
#     C-s、C-r で検索も可能。migemo 辞書を登録してあれば、検索文字を大文字で始める
#     ことで migemo 検索も可能。emacs キーバインドを適用しないアプリケーションソフト
#     でもクリップボードリストは起動し、選択した項目を Enter で確定することで、
#     クリップボードへの格納（テキストの貼り付けではない）が行われる。）
# ・lancherList_key 変数に設定したキーにより、ランチャーリストが起動する。
#   （全てのアプリケーションソフトで利用可能。操作方法は、クリップボードリストと同じ。）
# ・クリップボードリストやランチャーリストのリストボックス内では、基本、Altキーを
#   Ctrlキーと同じキーとして扱っている。（C-v と A-v の置き換えのみ行っていない。）
# ・window_switching_key 変数に設定したキーにより、アクティブウィンドウの切り替えが行われ
#   る。アクティブウィンドウを切り替える際、切り替わったウィンドウが最小化されている場合は、
#   ウィンドウのリストアも併せて行われる。
# ・マルチディスプレイを利用している際に、window_movement_key 変数に設定したキーにより、
#   アクティブウィンドウのディスプレイ間の移動が行われる。
# ・window_minimize_key 変数に設定したキーにより、ウィンドウの最小化、リストアが行われる。
# ・desktop_switching_key 変数に設定したキーにより、仮想デスクトップの切り替えが行われる。
#   （仮想デスクトップの利用については、以下を参照ください。
#     ・http://pc-karuma.net/windows-10-virtual-desktops/
#     ・http://pc-karuma.net/windows-10-virtual-desktop-show-all-window-app/
#     仮想デスクトップ切替時のアニメーションを止める方法は以下を参照ください。
#     ・http://www.jw7.org/2015/11/03/windows10_virtualdesktop_animation_off/ ）

import time
import sys
import os.path
import re

from keyhac import *
from keyhac_keymap import *

def configure(keymap):

    ####################################################################################################
    ## カスタマイズ用の設定
    ####################################################################################################

    # 日本語キーボードかどうかを指定する（True: 日本語キーボード、False: 英語キーボード）
    is_japanese_keyboard = True

    # 左右どちらの Ctrlキーを使うかを指定する（"L": 左、"R": 右）
    side_of_ctrl_key = "L"

    # 左右どちらの Altキーを使うかを指定する（"L": 左、"R": 右）
    side_of_alt_key = "L"

    # emacs日本語入力モードを使うかどうかを指定する（True: 使う、False: 使わない）
    use_emacs_ime_mode = False

    # emacs日本語入力モードを切り替える（トグルする）キーを指定する
    toggle_emacs_ime_mode_key = None

    # emacsシフトモードを使うかどうかを指定する（True: 使う、False: 使わない）
    use_emacs_shift_mode = False

    # IME を切り替えるキーを指定する（複数指定可）
    # toggle_input_method_key = ["C-Yen"]
    toggle_input_method_key = []

    # Escキーを Metaキーとして使うかどうかを指定する（True: 使う、False: 使わない）
    use_esc_as_meta = False

    # Ctl-xプレフィックスキーに使うキーを指定する
    # （Ctl-xプレフィックスキーのモディファイアキーは、Ctrl または Alt のいずれかから指定してください）
    ctl_x_prefix_key = "C-x"

    # スクロールに使うキーの組み合わせ（Up、Down の順）を指定する
    # scroll_key = None # PageUp、PageDownキーのみを利用する
    scroll_key = ["M-v", "C-v"]

    # 表示しているウインドウの中で、一番最近までフォーカスがあったウインドウに移動するキーを指定する
    other_window_key = "A-o"

    # クリップボードリストを起動するキーを指定する
    clipboardList_key = "A-y"

    # ランチャーリストを起動するキーを指定する
    lancherList_key = "A-l"

    # アクティブウィンドウを切り替えるキーの組み合わせ（前、後 の順）を指定する（複数指定可）
    window_switching_key = [["A-p", "A-n"]]

    # アクティブウィンドウをディスプレイ間で移動するキーの組み合わせ（前、後 の順）を指定する（複数指定可）
    # （other_window_key に割り当てている A-o との連係した利用を想定し、A-C-o を割り当てています。）
    # window_movement_key = None # Single display
    window_movement_key = [[None, "A-C-o"]] # Multi-display

    # ウィンドウを最小化、リストアするキーの組み合わせ（リストア、最小化 の順）を指定する（複数指定可）
    window_minimize_key = [["A-r", "A-m"]]

    # 仮想デスクトップを切り替えるキーの組み合わせ（前、後 の順）を指定する（複数指定可）
    # desktop_switching_key = None # for Windows 7 or 8.1
    desktop_switching_key = [["A-C-p", "A-C-n"]] # for Windows 10

    # shell_command 関数で起動するアプリケーションソフトを指定する
    # （パスが通っていない場所にあるコマンドは、絶対パスで指定してください。）
    command_name = r"cmd.exe"

    # emacs のキーバインドに"したくない"アプリケーションソフトを指定する（False を返す）
    # （Keyhac のメニューから「内部ログ」を ON にすると processname や classname を確認することができます。）
    def is_emacs_target(window):
        if is_list_window(window):
            return False

        # 変更箇所はここの in の中の指定
        if window.getProcessName() in ("cmd.exe",            # cmd
                                       "mintty.exe",         # mintty
                                       "emacs.exe",          # Emacs
                                       "emacs-w32.exe",      # Emacs
                                       "gvim.exe",           # GVim
                                       # "eclipse.exe",        # Eclipse
                                       # "firefox.exe",        # firefox
                                       "xyzzy.exe",          # xyzzy
                                       #"VirtualBox.exe",     # VirtualBox
                                       "XWin.exe",           # Cygwin/X
                                       "Xming.exe",          # Xming
                                       "putty.exe",          # PuTTY
                                       "ttermpro.exe",       # TeraTerm
                                       "MobaXterm.exe",      # MobaXterm
                                       "TurboVNC.exe",       # TurboVNC
                                       "vncviewer.exe"):     # UltraVNC

            keymap.window_keybind = "not_emacs"
            return False

        keymap.window_keybind = "emacs"
        return True

    # IME の切り替えのみをしたいアプリケーションソフトを指定する（True を返す）
    # （指定できるアプリケーションソフトは、is_emacs_target で除外指定したものからのみとしてください。）
    def is_ime_target(window):

        # 変更箇所はここの in の中の指定
        if window.getProcessName() in ("cmd.exe",            # cmd
                                       "mintty.exe",         # mintty
                                       "gvim.exe",           # GVim
                                       # "eclipse.exe",        # Eclipse
                                       # "firefox.exe",        # firefox
                                       "xyzzy.exe",          # xyzzy
                                       "putty.exe",          # PuTTY
                                       "ttermpro.exe",       # TeraTerm
                                       "MobaXterm.exe"):     # MobaXterm
            return True
        return False


    ####################################################################################################
    ## 基本設定
    ####################################################################################################

    if use_emacs_ime_mode:
        keymap_emacs = keymap.defineWindowKeymap(check_func=lambda wnd: is_emacs_target(wnd) and not is_emacs_ime_mode(wnd))
    else:
        keymap_emacs = keymap.defineWindowKeymap(check_func=is_emacs_target)

    keymap_ime   = keymap.defineWindowKeymap(check_func=is_ime_target)

    # mark がセットされると True になる
    keymap_emacs.is_marked = False

    # 検索が開始されると True になる
    keymap_emacs.is_searching = False

    # キーボードマクロの play 中 は True になる
    keymap_emacs.is_playing_kmacro = False

    # universal-argument コマンドが実行されると True になる
    keymap_emacs.is_universal_argument = False

    # digit-argument コマンドが実行されると True になる
    keymap_emacs.is_digit_argument = False

    # コマンドのリピート回数を設定する
    keymap_emacs.repeat_counter = 1

    # undo のモードの時 True になる（redo のモードの時 False になる）
    keymap_emacs.is_undo_mode = True

    # Ctl-xプレフィックスキーを構成するキーの仮想キーコードを設定する
    if ctl_x_prefix_key:
        keyCondition = KeyCondition.fromString(ctl_x_prefix_key)

        if keyCondition.mod == MODKEY_CTRL:
            ctl_x_prefix_skey = side_of_ctrl_key + ctl_x_prefix_key
            if side_of_ctrl_key == "L":
                ctl_x_prefix_vkey = [VK_LCONTROL, keyCondition.vk]
            else:
                ctl_x_prefix_vkey = [VK_RCONTROL, keyCondition.vk]
        elif keyCondition.mod == MODKEY_ALT:
            ctl_x_prefix_skey = side_of_alt_key + ctl_x_prefix_key
            if side_of_alt_key == "L":
                ctl_x_prefix_vkey = [VK_LMENU, keyCondition.vk]
            else:
                ctl_x_prefix_vkey = [VK_RMENU, keyCondition.vk]
        else:
            print("Ctl-xプレフィックスキーのモディファイアキーは、Ctrl または Alt のいずれかから指定してください")

    ##################################################
    ## IME の切り替え
    ##################################################

    def toggle_input_method():
        keymap.InputKeyCommand("A-(25)")()
        time.sleep(0.05) # delay

        if not keymap_emacs.is_playing_kmacro:
            # IME の状態を取得する
            if keymap.getWindow().getImeStatus():
                message = "[あ]"
            else:
                message = "[A]"

            # IME の状態をバルーンヘルプで表示する
            keymap.popBalloon("ime_status", message, 500)

    ##################################################
    ## ファイル操作
    ##################################################

    def find_file():
        keymap.InputKeyCommand("C-o")()

    def save_buffer():
        keymap.InputKeyCommand("C-s")()

    def write_file():
        keymap.InputKeyCommand("A-f", "A-a")()

    def dired():
        keymap.ShellExecuteCommand(None, r"explorer.exe", "", "")()

    ##################################################
    ## カーソル移動
    ##################################################

    def backward_char():
        keymap.InputKeyCommand("Left")()

    def forward_char():
        keymap.InputKeyCommand("Right")()

    def backward_word():
        keymap.InputKeyCommand("C-Left")()

    def forward_word():
        keymap.InputKeyCommand("C-Right")()

    def previous_line():
        keymap.InputKeyCommand("Up")()

    def next_line():
        keymap.InputKeyCommand("Down")()

    def move_beginning_of_line():
        keymap.InputKeyCommand("Home")()

    def move_end_of_line():
        keymap.InputKeyCommand("End")()
        if keymap.getWindow().getClassName() == "_WwG": # Microsoft Word
            if keymap_emacs.is_marked:
                keymap.InputKeyCommand("Left")()

    def beginning_of_buffer():
        keymap.InputKeyCommand("C-Home")()

    def end_of_buffer():
        keymap.InputKeyCommand("C-End")()

    def scroll_up():
        keymap.InputKeyCommand("PageUp")()

    def scroll_down():
        keymap.InputKeyCommand("PageDown")()

    def recenter():
        if keymap.getWindow().getClassName() == "EditorClient": # Sakura Editor
            keymap.InputKeyCommand("C-h")()

    ##################################################
    ## カット / コピー / 削除 / アンドゥ
    ##################################################

    def delete_backward_char():
        keymap.InputKeyCommand("Back")()

    def delete_char():
        keymap.InputKeyCommand("Delete")()

    def backward_kill_word(repeat=1):
        keymap_emacs.is_marked = True
        def move_beginning_of_region():
            for i in range(repeat):
                backward_word()
        mark(move_beginning_of_region)()
        delay(kill_region)()

    def kill_word(repeat=1):
        keymap_emacs.is_marked = True
        def move_end_of_region():
            for i in range(repeat):
                forward_word()
        mark(move_end_of_region)()
        delay(kill_region)()

    def kill_line(repeat=1):
        keymap_emacs.is_marked = True
        if repeat == 1:
            mark(move_end_of_line)()
            if keymap.getWindow().getClassName() == "HM32CLIENT": # Hidemaru Editor
                delay(keymap.InputKeyCommand("C-x"))()
                if getClipboardText() == "":
                    keymap.InputKeyCommand("Delete")()
            else:
                delay(keymap.InputKeyCommand("C-c", "Delete"))() # 改行を消せるようにするため C-x にはしていない
        else:
            def move_end_of_region():
                if keymap.getWindow().getClassName() == "_WwG": # Microsoft Word
                    for i in range(repeat):
                        next_line()
                    move_beginning_of_line()
                else:
                    for i in range(repeat - 1):
                        next_line()
                    move_end_of_line()
                    forward_char()
            mark(move_end_of_region)()
            delay(kill_region)()

    def kill_region():
        keymap.InputKeyCommand("C-x")()

    def kill_ring_save():
        keymap.InputKeyCommand("C-c")()
        if keymap.getWindow().getClassName() == "EditorClient": # Sakura Editor
            # 選択されているリージョンのハイライトを解除するために Esc を発行する
            keymap.InputKeyCommand("Esc")()

    def yank():
        keymap.InputKeyCommand("C-v")()

    def undo():
        # redo（C-y）の機能を持っていないアプリケーションソフトは常に undo とする
        if keymap.getWindow().getClassName() in ("Edit"): # NotePad
            keymap.InputKeyCommand("C-z")()
        else:
            if keymap_emacs.is_undo_mode:
                keymap.InputKeyCommand("C-z")()
            else:
                keymap.InputKeyCommand("C-y")()

    def redo():
        keymap_emacs.is_undo_mode = False
        undo()

    def set_mark_command():
        if keymap_emacs.is_marked:
            keymap_emacs.is_marked = False
        else:
            keymap_emacs.is_marked = True

    def mark_whole_buffer():
        if keymap.getWindow().getClassName().startswith("EXCEL"): # Microsoft Excel
            # Excel のセルの中でも機能するようにする対策
            keymap.InputKeyCommand("C-End", "C-S-Home")()
        else:
            keymap.InputKeyCommand("C-Home", "C-a")()

    def mark_page():
        mark_whole_buffer()

    def open_line():
        keymap.InputKeyCommand("Enter", "Up", "End")()

    ##################################################
    ## バッファ / ウインドウ操作
    ##################################################

    def kill_buffer():
        keymap.InputKeyCommand("C-F4")()

    def switch_to_buffer():
        keymap.InputKeyCommand("C-Tab")()

    def other_window():
        window_list = getWindowList()
        for wnd in window_list[1:]:
            if not wnd.isMinimized():
                wnd.getLastActivePopup().setForeground()
                break

    ##################################################
    ## 文字列検索 / 置換
    ##################################################

    def isearch(direction):
        if keymap_emacs.is_searching:
            if keymap.getWindow().getProcessName() == "EXCEL.EXE":  # Microsoft Excel
                if keymap.getWindow().getClassName() == "EDTBX": # 検索ウィンドウ
                    keymap.InputKeyCommand({"backward":"A-S-f", "forward":"A-f"}[direction])()
                else:
                    keymap.InputKeyCommand("C-f")()
            else:
                keymap.InputKeyCommand({"backward":"S-F3", "forward":"F3"}[direction])()
        else:
            keymap.InputKeyCommand("C-f")()
            keymap_emacs.is_searching = True

    def isearch_backward():
        isearch("backward")

    def isearch_forward():
        isearch("forward")

    def query_replace():
        if keymap.getWindow().getClassName() in ("EditorClient", # Sakura Editor
                                                 "HM32CLIENT"):  # Hidemaru Editor
            keymap.InputKeyCommand("C-r")()
        else:
            keymap.InputKeyCommand("C-h")()

    ##################################################
    ## キーボードマクロ
    ##################################################

    def kmacro_start_macro():
        keymap.command_RecordStart()

    def kmacro_end_macro():
        keymap.command_RecordStop()
        # キーボードマクロの終了キー「Ctl-xプレフィックスキー + ")"」の Ctl-xプレフィックスキーがマクロに
        # 記録されてしまうのを対策する（キーボードマクロの終了キーの前提を「Ctl-xプレフィックスキー + ")"」
        # としていることについては、とりえず了承ください。）
        if ctl_x_prefix_key and len(keymap.record_seq) >= 4:
            if (((keymap.record_seq[len(keymap.record_seq) - 1] == (ctl_x_prefix_vkey[0], True) and
                  keymap.record_seq[len(keymap.record_seq) - 2] == (ctl_x_prefix_vkey[1], True)) or
                 (keymap.record_seq[len(keymap.record_seq) - 1] == (ctl_x_prefix_vkey[1], True) and
                  keymap.record_seq[len(keymap.record_seq) - 2] == (ctl_x_prefix_vkey[0], True))) and
                keymap.record_seq[len(keymap.record_seq) - 3] == (ctl_x_prefix_vkey[1], False)):
                   keymap.record_seq.pop()
                   keymap.record_seq.pop()
                   keymap.record_seq.pop()
                   if keymap.record_seq[len(keymap.record_seq) - 1] == (ctl_x_prefix_vkey[0], False):
                       for i in range(len(keymap.record_seq) - 1, -1, -1):
                           if keymap.record_seq[i] == (ctl_x_prefix_vkey[0], False):
                               keymap.record_seq.pop()
                           else:
                               break
                   else:
                       # コントロール系の入力が連続して行われる場合があるための対処
                       keymap.record_seq.append((ctl_x_prefix_vkey[0], True))

    def kmacro_end_and_call_macro():
        keymap_emacs.is_playing_kmacro = True
        keymap.command_RecordPlay()
        keymap_emacs.is_playing_kmacro = False

    ##################################################
    ## その他
    ##################################################

    def newline():
        keymap.InputKeyCommand("Enter")()

    def newline_and_indent():
        keymap.InputKeyCommand("Enter", "Tab")()

    def indent_for_tab_command():
        keymap.InputKeyCommand("Tab")()

    def keyboard_quit():
        if not keymap.getWindow().getClassName().startswith("EXCEL"): # Microsoft Excel 以外
            # 選択されているリージョンのハイライトを解除するために Esc を発行しているが、
            # アプリケーションソフトによっては効果なし
            keymap.InputKeyCommand("Esc")()
        keymap.command_RecordStop()
        if keymap_emacs.is_undo_mode:
            keymap_emacs.is_undo_mode = False
        else:
            keymap_emacs.is_undo_mode = True

    def kill_emacs():
        keymap.InputKeyCommand("A-F4")()

    def universal_argument():
        if keymap_emacs.is_universal_argument:
            if keymap_emacs.is_digit_argument == True:
                keymap_emacs.is_universal_argument = False
            else:
                keymap_emacs.repeat_counter *= 4
        else:
            keymap_emacs.is_universal_argument = True
            keymap_emacs.repeat_counter *= 4

    def digit_argument(number):
        if keymap_emacs.is_digit_argument:
            keymap_emacs.repeat_counter = keymap_emacs.repeat_counter * 10 + number
        else:
            keymap_emacs.repeat_counter = number
            keymap_emacs.is_digit_argument = True

    def shell_command():
        def popCommandWindow(wnd, command):
            if wnd.isVisible() and not wnd.getOwner() and wnd.getProcessName() == command:
                popWindow(wnd)()
                keymap_emacs.is_executing_command = True
                return False
            return True

        keymap_emacs.is_executing_command = False
        Window.enum(popCommandWindow, os.path.basename(command_name))

        if not keymap_emacs.is_executing_command:
            keymap.ShellExecuteCommand(None, command_name, "", "")()

    ##################################################
    ## 共通関数
    ##################################################

    def self_insert_command(key):
        return keymap.InputKeyCommand(key)

    if use_emacs_ime_mode:
        def self_insert_command2(key):
            def _func():
                keymap.InputKeyCommand(key)()
                if keymap.getWindow().getImeStatus():
                    enable_emacs_ime_mode()
            return _func
    else:
        def self_insert_command2(key):
            return keymap.InputKeyCommand(key)

    def kbd(keys):
        if keys:
            keys_lists = [keys.split()]

            if keys_lists[0][0] == "Ctl-x":
                if ctl_x_prefix_key:
                    keys_lists[0][0] = ctl_x_prefix_skey
                else:
                    keys_lists = []

            elif keys_lists[0][0].startswith("C-"):
                keys_lists[0][0] = side_of_ctrl_key + keys_lists[0][0]

            elif keys_lists[0][0].startswith("A-"):
                keys_lists[0][0] = side_of_alt_key + keys_lists[0][0]

            elif keys_lists[0][0].startswith("M-"):
                key = keys_lists[0][0].replace("M-", "")
                keys_lists[0][0] = side_of_alt_key + "A-" + key
                keys_lists.append([side_of_ctrl_key + "C-OpenBracket", key])
                if use_esc_as_meta:
                    keys_lists.append(["Esc", key])
        else:
            keys_lists = []

        return keys_lists

    def define_key(keymap, keys, command):
        for keys_list in kbd(keys):
            if len(keys_list) == 1:
                keymap[keys_list[0]] = command
            else:
                keymap[keys_list[0]][keys_list[1]] = command

    def digit(number):
        def _func():
            if keymap_emacs.is_universal_argument:
                digit_argument(number)
            else:
                reset_undo(reset_counter(reset_mark(repeat(self_insert_command2(str(number))))))()
        return _func

    def digit2(number):
        def _func():
            keymap_emacs.is_universal_argument = True
            digit_argument(number)
        return _func

    def delay(func, sec=0.01):
        def _func():
            time.sleep(sec) # delay
            func()
            time.sleep(sec) # delay
        return _func

    def mark(func):
        def _func():
            if keymap_emacs.is_marked:
                # D-Shift だと、M-< や M-> 押下時に、D-Shift が解除されてしまう。その対策。
                keymap.InputKeyCommand("D-LShift", "D-RShift")()
                delay(func)()
                keymap.InputKeyCommand("U-LShift", "U-RShift")()
            else:
                func()
        return _func

    def reset_mark(func):
        def _func():
            func()
            keymap_emacs.is_marked = False
        return _func

    def reset_counter(func):
        def _func():
            func()
            keymap_emacs.is_universal_argument = False
            keymap_emacs.is_digit_argument = False
            keymap_emacs.repeat_counter = 1
        return _func

    def reset_undo(func):
        def _func():
            func()
            keymap_emacs.is_undo_mode = True
        return _func

    def reset_search(func):
        def _func():
            func()
            keymap_emacs.is_searching = False
        return _func

    def repeat(func):
        def _func():
            # 以下の２行は、キーボードマクロの繰り返し実行の際に必要な設定
            repeat_counter = keymap_emacs.repeat_counter
            keymap_emacs.repeat_counter = 1
            for i in range(repeat_counter):
                func()
        return _func

    def repeat2(func):
        def _func():
            if keymap_emacs.is_marked:
                keymap_emacs.repeat_counter = 1
            repeat(func)()
        return _func

    def repeat3(func):
        def _func():
            func(keymap_emacs.repeat_counter)
        return _func

    ##################################################
    ## キーバインド
    ##################################################

    # キーバインドの定義に利用している表記の意味は以下のとおりです。
    # ・S-    : Shiftキー
    # ・C-    : Ctrlキー
    # ・A-    : Altキー
    # ・M-    : Altキー と Esc、C-[ のプレフィックスキーを利用する３パターンを定義（emacs の Meta と同様）
    # ・Ctl-x : ctl_x_prefix_key 変数で定義されているプレフィックスキーに置換え
    # ・(999) : 仮想キーコード指定

    # https://github.com/crftwr/keyhac/blob/master/keyhac_keymap.py
    # https://github.com/crftwr/pyauto/blob/master/pyauto_const.py
    # http://www.yoshidastyle.net/2007/10/windowswin32api.html
    # http://homepage3.nifty.com/ic/help/rmfunc/vkey.htm
    # http://www.azaelia.net/factory/vk.html

    ## マルチストロークキーの設定
    define_key(keymap_emacs, "Ctl-x",         keymap.defineMultiStrokeKeymap(ctl_x_prefix_key))
    define_key(keymap_emacs, "C-q",           keymap.defineMultiStrokeKeymap("C-q"))
    define_key(keymap_emacs, "C-OpenBracket", keymap.defineMultiStrokeKeymap("C-OpenBracket"))
    if use_esc_as_meta:
        define_key(keymap_emacs, "Esc", keymap.defineMultiStrokeKeymap("Esc"))

    ## 数字キーの設定
    for key in range(10):
        s_key = str(key)
        define_key(keymap_emacs,        s_key, digit(key))
        define_key(keymap_emacs, "C-" + s_key, digit2(key))
        define_key(keymap_emacs, "M-" + s_key, digit2(key))
        define_key(keymap_emacs, "S-" + s_key, reset_undo(reset_counter(reset_mark(repeat(self_insert_command2("S-" + s_key))))))

    ## アルファベットキーの設定
    for vkey in range(VK_A, VK_Z + 1):
        s_vkey = "(" + str(vkey) + ")"
        define_key(keymap_emacs,        s_vkey, reset_undo(reset_counter(reset_mark(repeat(self_insert_command2(       s_vkey))))))
        define_key(keymap_emacs, "S-" + s_vkey, reset_undo(reset_counter(reset_mark(repeat(self_insert_command2("S-" + s_vkey))))))

    ## 特殊文字キーの設定
    s_vkey = "(" + str(VK_SPACE) + ")"
    define_key(keymap_emacs,        s_vkey, reset_undo(reset_counter(reset_mark(repeat(self_insert_command(       s_vkey))))))
    define_key(keymap_emacs, "S-" + s_vkey, reset_undo(reset_counter(reset_mark(repeat(self_insert_command("S-" + s_vkey))))))

    for vkey in [VK_OEM_MINUS, VK_OEM_PLUS, VK_OEM_COMMA, VK_OEM_PERIOD, VK_OEM_1, VK_OEM_2, VK_OEM_3, VK_OEM_4, VK_OEM_5, VK_OEM_6, VK_OEM_7, VK_OEM_102]:
        s_vkey = "(" + str(vkey) + ")"
        define_key(keymap_emacs,        s_vkey, reset_undo(reset_counter(reset_mark(repeat(self_insert_command2(       s_vkey))))))
        define_key(keymap_emacs, "S-" + s_vkey, reset_undo(reset_counter(reset_mark(repeat(self_insert_command2("S-" + s_vkey))))))

    ## 10key の特殊文字キーの設定
    for vkey in [VK_MULTIPLY, VK_ADD, VK_SUBTRACT, VK_DECIMAL, VK_DIVIDE]:
        s_vkey = "(" + str(vkey) + ")"
        define_key(keymap_emacs, s_vkey, reset_undo(reset_counter(reset_mark(repeat(self_insert_command2(s_vkey))))))

    ## quoted-insertキーの設定
    for vkey in keyCondition.vk_str_table.keys():
        s_vkey = "(" + str(vkey) + ")"
        define_key(keymap_emacs, "C-q "     + s_vkey, reset_search(reset_undo(reset_counter(reset_mark(self_insert_command(         s_vkey))))))
        define_key(keymap_emacs, "C-q S-"   + s_vkey, reset_search(reset_undo(reset_counter(reset_mark(self_insert_command("S-"   + s_vkey))))))
        define_key(keymap_emacs, "C-q C-"   + s_vkey, reset_search(reset_undo(reset_counter(reset_mark(self_insert_command("C-"   + s_vkey))))))
        define_key(keymap_emacs, "C-q C-S-" + s_vkey, reset_search(reset_undo(reset_counter(reset_mark(self_insert_command("C-S-" + s_vkey))))))
        define_key(keymap_emacs, "C-q A-"   + s_vkey, reset_search(reset_undo(reset_counter(reset_mark(self_insert_command("A-"   + s_vkey))))))
        define_key(keymap_emacs, "C-q A-S-" + s_vkey, reset_search(reset_undo(reset_counter(reset_mark(self_insert_command("A-S-" + s_vkey))))))

    ## C-S-[a-z] -> C-[a-z]、A-S-[a-z] -> A-[a-z] の置き換え設定（emacsシフトモードの設定）
    if use_emacs_shift_mode:
        for vkey in range(VK_A, VK_Z + 1):
            s_vkey = "(" + str(vkey) + ")"
            define_key(keymap_emacs, "C-S-" + s_vkey, reset_search(reset_undo(reset_counter(reset_mark(self_insert_command("C-" + s_vkey))))))
            define_key(keymap_emacs, "A-S-" + s_vkey, reset_search(reset_undo(reset_counter(reset_mark(self_insert_command("A-" + s_vkey))))))

    ## Escキーの設定
    define_key(keymap_emacs, "C-OpenBracket C-OpenBracket", reset_undo(reset_counter(self_insert_command("Esc"))))
    if use_esc_as_meta:
        define_key(keymap_emacs, "Esc Esc", reset_undo(reset_counter(self_insert_command("Esc"))))
    else:
        define_key(keymap_emacs, "Esc", reset_undo(reset_counter(self_insert_command("Esc"))))

    ## universal-argumentキーの設定
    define_key(keymap_emacs, "C-u", universal_argument)

    ## 「IME の切り替え」のキー設定
    define_key(keymap_emacs, "(243)",  toggle_input_method)
    define_key(keymap_emacs, "(244)",  toggle_input_method)
    define_key(keymap_emacs, "A-(25)", toggle_input_method)

    define_key(keymap_ime,   "(243)",  toggle_input_method)
    define_key(keymap_ime,   "(244)",  toggle_input_method)
    define_key(keymap_ime,   "A-(25)", toggle_input_method)

    ## 「ファイル操作」のキー設定
    define_key(keymap_emacs, "Ctl-x C-f", reset_search(reset_undo(reset_counter(reset_mark(find_file)))))
    define_key(keymap_emacs, "Ctl-x C-s", reset_search(reset_undo(reset_counter(reset_mark(save_buffer)))))
    define_key(keymap_emacs, "Ctl-x C-w", reset_search(reset_undo(reset_counter(reset_mark(write_file)))))
    define_key(keymap_emacs, "Ctl-x d",   reset_search(reset_undo(reset_counter(reset_mark(dired)))))

    ## 「カーソル移動」のキー設定
    define_key(keymap_emacs, "C-b",        reset_search(reset_undo(reset_counter(mark(repeat(backward_char))))))
    define_key(keymap_emacs, "C-f",        reset_search(reset_undo(reset_counter(mark(repeat(forward_char))))))
    define_key(keymap_emacs, "M-b",        reset_search(reset_undo(reset_counter(mark(repeat(backward_word))))))
    define_key(keymap_emacs, "M-f",        reset_search(reset_undo(reset_counter(mark(repeat(forward_word))))))
    define_key(keymap_emacs, "C-p",        reset_search(reset_undo(reset_counter(mark(repeat(previous_line))))))
    define_key(keymap_emacs, "C-n",        reset_search(reset_undo(reset_counter(mark(repeat(next_line))))))
    define_key(keymap_emacs, "C-a",        reset_search(reset_undo(reset_counter(mark(move_beginning_of_line)))))
    define_key(keymap_emacs, "C-e",        reset_search(reset_undo(reset_counter(mark(move_end_of_line)))))
    define_key(keymap_emacs, "M-S-Comma",  reset_search(reset_undo(reset_counter(mark(beginning_of_buffer)))))
    define_key(keymap_emacs, "M-S-Period", reset_search(reset_undo(reset_counter(mark(end_of_buffer)))))
    define_key(keymap_emacs, "C-l",        reset_search(reset_undo(reset_counter(recenter))))

    ## 「カット / コピー / 削除 / アンドゥ」のキー設定
    define_key(keymap_emacs, "C-h",      reset_search(reset_undo(reset_counter(reset_mark(repeat2(delete_backward_char))))))
    define_key(keymap_emacs, "C-d",      reset_search(reset_undo(reset_counter(reset_mark(repeat2(delete_char))))))
    define_key(keymap_emacs, "C-Back",   reset_search(reset_undo(reset_counter(reset_mark(repeat3(backward_kill_word))))))
    define_key(keymap_emacs, "M-Delete", reset_search(reset_undo(reset_counter(reset_mark(repeat3(backward_kill_word))))))
    define_key(keymap_emacs, "C-Delete", reset_search(reset_undo(reset_counter(reset_mark(repeat3(kill_word))))))
    define_key(keymap_emacs, "M-d",      reset_search(reset_undo(reset_counter(reset_mark(repeat3(kill_word))))))
    define_key(keymap_emacs, "C-k",      reset_search(reset_undo(reset_counter(reset_mark(repeat3(kill_line))))))
    define_key(keymap_emacs, "C-w",      reset_search(reset_undo(reset_counter(reset_mark(kill_region)))))
    define_key(keymap_emacs, "M-w",      reset_search(reset_undo(reset_counter(reset_mark(kill_ring_save)))))
    define_key(keymap_emacs, "C-c",      reset_search(reset_undo(reset_counter(reset_mark(kill_ring_save)))))
    define_key(keymap_emacs, "C-y",      reset_search(reset_undo(reset_counter(reset_mark(yank)))))
    define_key(keymap_emacs, "C-z",      reset_search(reset_counter(reset_mark(undo))))
    define_key(keymap_emacs, "C-Slash",  reset_search(reset_counter(reset_mark(undo))))
    define_key(keymap_emacs, "Ctl-x u",  reset_search(reset_counter(reset_mark(undo))))

    # C-Underscore を機能させるための設定
    if is_japanese_keyboard:
        define_key(keymap_emacs, "C-S-BackSlash", reset_search(reset_undo(reset_counter(reset_mark(redo)))))
    else:
        define_key(keymap_emacs, "C-S-Minus", reset_search(reset_undo(reset_counter(reset_mark(redo)))))

    if is_japanese_keyboard:
        # C-Atmark だとうまく動かない方が居るようなので C-(192) としている
        # （http://bhby39.blogspot.jp/2015/02/windows-emacs.html）
        define_key(keymap_emacs, "C-(192)", reset_search(reset_undo(reset_counter(set_mark_command))))
    else:
        # C-S-2 は有効とならないが、一応設定は行っておく（C-S-3 などは有効となる。なぜだろう？）
        define_key(keymap_emacs, "C-S-2", reset_search(reset_undo(reset_counter(set_mark_command))))

    define_key(keymap_emacs, "C-Space",   reset_search(reset_undo(reset_counter(set_mark_command))))
    define_key(keymap_emacs, "Ctl-x h",   reset_search(reset_undo(reset_counter(reset_mark(mark_whole_buffer)))))
    define_key(keymap_emacs, "Ctl-x C-p", reset_search(reset_undo(reset_counter(reset_mark(mark_page)))))

    ## 「バッファ / ウインドウ操作」のキー設定
    define_key(keymap_emacs, "Ctl-x k", reset_search(reset_undo(reset_counter(reset_mark(kill_buffer)))))
    define_key(keymap_emacs, "Ctl-x b", reset_search(reset_undo(reset_counter(reset_mark(switch_to_buffer)))))
    define_key(keymap_emacs, "Ctl-x o", reset_search(reset_undo(reset_counter(reset_mark(other_window)))))

    ## 「文字列検索 / 置換」のキー設定
    define_key(keymap_emacs, "C-r",   reset_undo(reset_counter(reset_mark(isearch_backward))))
    define_key(keymap_emacs, "C-s",   reset_undo(reset_counter(reset_mark(isearch_forward))))
    define_key(keymap_emacs, "M-S-5", reset_search(reset_undo(reset_counter(reset_mark(query_replace)))))

    ## 「キーボードマクロ」のキー設定
    if is_japanese_keyboard:
        define_key(keymap_emacs, "Ctl-x S-8", kmacro_start_macro)
        define_key(keymap_emacs, "Ctl-x S-9", kmacro_end_macro)
    else:
        define_key(keymap_emacs, "Ctl-x S-9", kmacro_start_macro)
        define_key(keymap_emacs, "Ctl-x S-0", kmacro_end_macro)

    define_key(keymap_emacs, "Ctl-x e", reset_search(reset_undo(reset_counter(repeat(kmacro_end_and_call_macro)))))

    ## 「その他」のキー設定
    define_key(keymap_emacs, "Enter",     reset_undo(reset_counter(reset_mark(repeat(newline)))))
    define_key(keymap_emacs, "C-m",       reset_undo(reset_counter(reset_mark(repeat(newline)))))
    #define_key(keymap_emacs, "C-j",       reset_undo(reset_counter(reset_mark(newline_and_indent))))
    define_key(keymap_emacs, "Tab",       reset_undo(reset_counter(reset_mark(repeat(indent_for_tab_command)))))
    define_key(keymap_emacs, "C-i",       reset_undo(reset_counter(reset_mark(repeat(indent_for_tab_command)))))
    define_key(keymap_emacs, "C-g",       reset_search(reset_counter(reset_mark(keyboard_quit))))
    define_key(keymap_emacs, "Ctl-x C-c", reset_search(reset_undo(reset_counter(reset_mark(kill_emacs)))))
    define_key(keymap_emacs, "M-S-1",     reset_search(reset_undo(reset_counter(reset_mark(shell_command)))))

    ## 「IME の切り替え」のキー設定（上書きされないように最後に設定する）
    if toggle_input_method_key:
        for key in toggle_input_method_key:
            define_key(keymap_emacs, key, toggle_input_method)
            define_key(keymap_ime,   key, toggle_input_method)

    ## 「スクロール」のキー設定（上書きされないように最後に設定する）
    if scroll_key:
        define_key(keymap_emacs, scroll_key[0], reset_search(reset_undo(reset_counter(mark(scroll_up)))))
        define_key(keymap_emacs, scroll_key[1], reset_search(reset_undo(reset_counter(mark(scroll_down)))))

    ## 「カット」のキー設定（上書きされないように最後に設定する）
    if ctl_x_prefix_key != "C-x":
        define_key(keymap_emacs, "C-x", reset_search(reset_undo(reset_counter(reset_mark(kill_region)))))


    ####################################################################################################
    ## emacs日本語入力モードの設定
    ####################################################################################################
    if use_emacs_ime_mode:

        # emacs日本語入力モードが開始されると True になる
        keymap_emacs.is_emacs_ime_mode = False

        def is_emacs_ime_mode(window):
            return keymap_emacs.is_emacs_ime_mode

        keymap_emacs_ime = keymap.defineWindowKeymap(check_func=lambda wnd: is_emacs_target(wnd) and is_emacs_ime_mode(wnd))

        ##################################################
        ## emacs日本語入力モード の切り替え
        ##################################################

        def enable_emacs_ime_mode():
            keymap_emacs.is_emacs_ime_mode = True
            keymap_emacs.last_func = None
            keymap._updateKeymap(keymap.getWindow())

        def disable_emacs_ime_mode():
            keymap_emacs.is_emacs_ime_mode = False
            keymap._updateKeymap(keymap.getWindow())

        def toggle_emacs_ime_mode():
            if keymap_emacs.is_emacs_ime_mode:
                disable_emacs_ime_mode()
            else:
                enable_emacs_ime_mode()
            ei_popBalloon()

        ##################################################
        ## IME の切り替え（emacs日本語入力モード用）
        ##################################################

        def ei_toggle_input_method(key):
            def _func():
                if keymap_emacs.last_func in (delete_backward_char, ei_esc):
                    toggle_input_method()
                    disable_emacs_ime_mode()
                else:
                    ei_record_func(self_insert_command(key)())
            return _func

        ##################################################
        ## その他（emacs日本語入力モード用）
        ##################################################

        def ei_esc():
            keymap.InputKeyCommand("Esc")()

        def ei_newline():
            keymap.InputKeyCommand("Enter")()
            disable_emacs_ime_mode()

        def ei_keyboard_quit():
            keymap.InputKeyCommand("Esc")()
            disable_emacs_ime_mode()

        ##################################################
        ## 共通関数（emacs日本語入力モード用）
        ##################################################

        def ei_popBalloon():
            if not keymap_emacs.is_playing_kmacro:
                if keymap_emacs.is_emacs_ime_mode:
                    message = "[IME]"
                else:
                    message = "[main]"

                # emacs サブキーバインドモードの状態をバルーンヘルプで表示する
                keymap.popBalloon("emacs_ime_mode", message, 500)

        def ei_record_func(func):
            def _func():
                keymap_emacs.last_func = func
                func()
            return _func

        ##################################################
        ## キーバインド（emacs日本語入力モード用）
        ##################################################

        ## 数字キーの設定
        for key in range(10):
            s_key = str(key)
            define_key(keymap_emacs_ime, s_key, ei_record_func(self_insert_command(s_key)))

        ## アルファベットキーの設定
        for vkey in range(VK_A, VK_Z + 1):
            s_vkey = "(" + str(vkey) + ")"
            define_key(keymap_emacs_ime,        s_vkey, ei_record_func(self_insert_command(       s_vkey)))
            define_key(keymap_emacs_ime, "S-" + s_vkey, ei_record_func(self_insert_command("S-" + s_vkey)))
            define_key(keymap_emacs_ime, "C-" + s_vkey, ei_record_func(self_insert_command("C-" + s_vkey)))

        ## 特殊文字キーの設定
        for vkey in [VK_SPACE, VK_OEM_MINUS, VK_OEM_PLUS, VK_OEM_COMMA, VK_OEM_PERIOD, VK_OEM_1, VK_OEM_2, VK_OEM_3, VK_OEM_4, VK_OEM_5, VK_OEM_6, VK_OEM_7, VK_OEM_102]:
            s_vkey = "(" + str(vkey) + ")"
            define_key(keymap_emacs_ime,        s_vkey, ei_record_func(self_insert_command(       s_vkey)))
            define_key(keymap_emacs_ime, "S-" + s_vkey, ei_record_func(self_insert_command("S-" + s_vkey)))

        ## 10key の特殊文字キーの設定
        for vkey in [VK_MULTIPLY, VK_ADD, VK_SUBTRACT, VK_DECIMAL, VK_DIVIDE]:
            s_vkey = "(" + str(vkey) + ")"
            define_key(keymap_emacs_ime, s_vkey, ei_record_func(self_insert_command(s_vkey)))

        ## Escキーの設定
        define_key(keymap_emacs_ime, "Esc",           ei_record_func(ei_esc))
        define_key(keymap_emacs_ime, "C-OpenBracket", ei_record_func(ei_esc))

        ## 「カーソル移動」のキー設定
        define_key(keymap_emacs_ime, "C-b", ei_record_func(backward_char))
        define_key(keymap_emacs_ime, "C-f", ei_record_func(forward_char))
        define_key(keymap_emacs_ime, "C-p", ei_record_func(previous_line))
        define_key(keymap_emacs_ime, "C-n", ei_record_func(next_line))

        ## 「カット / コピー / 削除 / アンドゥ」のキー設定
        define_key(keymap_emacs_ime, "Back", ei_record_func(delete_backward_char))
        define_key(keymap_emacs_ime, "C-h",  ei_record_func(delete_backward_char))

        ## 「その他」のキー設定
        define_key(keymap_emacs_ime, "Enter", ei_newline)
        define_key(keymap_emacs_ime, "C-m",   ei_newline)
        define_key(keymap_emacs_ime, "Tab",   ei_record_func(indent_for_tab_command))
        define_key(keymap_emacs_ime, "C-g",   ei_keyboard_quit)

        ## 「IME の切り替え」のキー設定（上書きされないように最後に設定する）
        if toggle_input_method_key:
            for key in toggle_input_method_key:
                define_key(keymap_emacs_ime, key, ei_toggle_input_method(key))

        ## emacs日本語入力モードを切り替える（トグルする）
        define_key(keymap_emacs,     toggle_emacs_ime_mode_key, toggle_emacs_ime_mode)
        define_key(keymap_emacs_ime, toggle_emacs_ime_mode_key, toggle_emacs_ime_mode)


    ####################################################################################################
    ## デスクトップ用の設定
    ####################################################################################################

    keymap_global = keymap.defineWindowKeymap()

    ##################################################
    ## ウインドウ操作（デスクトップ用）
    ##################################################

    def popWindow(wnd):
        def _func():
            try:
                if wnd.isMinimized():
                    wnd.restore()
                wnd.getLastActivePopup().setForeground()
            except:
                print("選択したウィンドウは存在しませんでした")
        return _func

    def getWindowList():
        def makeWindowList(wnd, arg):
            if wnd.isVisible() and not wnd.getOwner():

                class_name = wnd.getClassName()
                title = wnd.getText()

                if class_name == "Emacs" or title != "":

                    # 操作の対象としたくないアプリケーションソフトのクラス名称を、re.match 関数
                    # （先頭からのマッチ）の正規表現に「|」を使って繋げて指定してください。
                    # （完全マッチとするためには $ の指定が必要です。）
                    if not re.match(r"Progman$", class_name):

                        process_name = wnd.getProcessName()

                        # 操作の対象としたくないアプリケーションソフトのプロセス名称を、re.match 関数
                        # （先頭からのマッチ）の正規表現に「|」を使って繋げて指定してください。
                        # （完全マッチとするためには $ の指定が必要です。）
                        if not re.match(r"RocketDock.exe$", process_name): # サンプルとして RocketDock.exe を登録

                            # 表示されていないストアアプリ（「設定」等）が window_list に登録されるのを抑制する
                            if class_name == "Windows.UI.Core.CoreWindow":
                                if title in window_dict:
                                    window_list.remove(window_dict[title])
                                else:
                                    window_dict[title] = wnd
                            elif class_name == "ApplicationFrameWindow":
                                if title not in window_dict:
                                    window_dict[title] = wnd
                                    window_list.append(wnd)
                            else:
                                window_list.append(wnd)

                            # print(process_name + " : " + class_name + " : " + title + " : " + str(wnd.isMinimized()))
            return True

        window_dict = {}
        window_list = []
        # print("----------------------------------------------------------------------------------------------------")
        Window.enum(makeWindowList, None)

        return window_list

    def restoreWindow():
        wnd = keymap.getTopLevelWindow()
        if wnd and wnd.isMinimized():
            wnd.restore()

    def previous_desktop():
        keymap.InputKeyCommand("W-" + side_of_ctrl_key + "C-Left")()

    def next_desktop():
        keymap.InputKeyCommand("W-" + side_of_ctrl_key + "C-Right")()

    def previous_window():
        keymap.InputKeyCommand("A-S-Esc")()
        time.sleep(0.2) # delay
        keymap.delayedCall(restoreWindow, 0)

    def next_window():
        keymap.InputKeyCommand("A-Esc")()
        time.sleep(0.2) # delay
        keymap.delayedCall(restoreWindow, 0)

    def previous_display():
        keymap.InputKeyCommand("W-S-Left")()

    def next_display():
        keymap.InputKeyCommand("W-S-Right")()

    def minimize_window():
        wnd = keymap.getTopLevelWindow()
        if wnd and not wnd.isMinimized():
            wnd.minimize()

    def restore_window():
        window_list = getWindowList()
        if not (sys.getwindowsversion().major == 6 and
                sys.getwindowsversion().minor == 1):
            window_list.reverse()
        for wnd in window_list:
            if wnd.isMinimized():
                wnd.restore()
                break

    ##################################################
    ## キーバインド（デスクトップ用）
    ##################################################

    # 表示しているウインドウの中で、一番最近までフォーカスがあったウインドウに移動
    define_key(keymap_global, other_window_key, reset_search(reset_undo(reset_counter(reset_mark(other_window)))))

    # アクティブウィンドウの切り替え
    if window_switching_key:
        for previous_key, next_key in window_switching_key:
            define_key(keymap_global, previous_key, reset_search(reset_undo(reset_counter(reset_mark(previous_window)))))
            define_key(keymap_global, next_key,     reset_search(reset_undo(reset_counter(reset_mark(next_window)))))

    # アクティブウィンドウのディスプレイ間移動
    if window_movement_key:
        for previous_key, next_key in window_movement_key:
            define_key(keymap_global, previous_key, reset_search(reset_undo(reset_counter(reset_mark(previous_display)))))
            define_key(keymap_global, next_key,     reset_search(reset_undo(reset_counter(reset_mark(next_display)))))

    # ウィンドウの最小化、リストア
    if window_minimize_key:
        for restore_key, minimize_key in window_minimize_key:
            define_key(keymap_global, restore_key,  reset_search(reset_undo(reset_counter(reset_mark(restore_window)))))
            define_key(keymap_global, minimize_key, reset_search(reset_undo(reset_counter(reset_mark(minimize_window)))))

    # 仮想デスクトップの切り替え
    if desktop_switching_key:
        for previous_key, next_key in desktop_switching_key:
            define_key(keymap_global, previous_key, reset_search(reset_undo(reset_counter(reset_mark(previous_desktop)))))
            define_key(keymap_global, next_key,     reset_search(reset_undo(reset_counter(reset_mark(next_desktop)))))


    ####################################################################################################
    ## リストウィンドウ用の設定
    ####################################################################################################

    # リストウィンドウはクリップボードリストで利用していますが、クリップボードリストの機能を
    # emacs キーバインドを適用していないアプリケーションソフトでも利用できるようにするため、
    # クリップボードリストで Enter を押下した際の挙動を、以下のとおりに切り分けています。
    #
    # １）emacs キーバインドを適用しているアプリケーションソフトからクリップボードリストを起動
    # 　　→   Enter（テキストの貼り付け）
    # ２）emacs キーバインドを適用していないアプリケーションソフトからクリップボードリストを起動
    # 　　→ S-Enter（テキストをクリップボードに格納）
    #
    # （emacs キーバインドを適用しないアプリケーションソフトには、キーの入出力の方式が特殊な
    # 　ものが多く指定されているため、テキストの貼り付けがうまく機能しないものがあります。
    # 　このため、アプリケーションソフトにペーストする場合は、そのアプリケーションソフトの
    # 　ペースト操作で行うことを前提とし、上記のとおりの仕様としてます。もし、どうしても
    # 　Enter（テキストの貼り付け）の入力を行いたい場合には、C-m の押下により対応できます。
    # 　なお、C-Enter（引用記号付で貼り付け）の置き換えは、対応が複雑となるため行っておりません。）

    keymap.setFont("ＭＳ ゴシック", 12)

    def is_list_window(window):
        if window.getClassName() == "KeyhacWindowClass" and window.getText() != "Keyhac":
            return True
        return False

    keymap_lw = keymap.defineWindowKeymap(check_func=is_list_window)

    # リストウィンドウで検索が開始されると True になる
    keymap_lw.is_searching = False

    ##################################################
    ## 文字列検索 / 置換（リストウィンドウ用）
    ##################################################

    def lw_isearch(direction):
        if keymap_lw.is_searching:
            keymap.InputKeyCommand({"backward":"Up", "forward":"Down"}[direction])()
        else:
            keymap.InputKeyCommand("f")()
            keymap_lw.is_searching = True

    def lw_isearch_backward():
        lw_isearch("backward")

    def lw_isearch_forward():
        lw_isearch("forward")

    ##################################################
    ## その他（リストウィンドウ用）
    ##################################################

    def lw_keyboard_quit():
        keymap.InputKeyCommand("Esc")()

    ##################################################
    ## 共通関数（リストウィンドウ用）
    ##################################################

    def lw_newline():
        if keymap.window_keybind == "emacs":
            keymap.InputKeyCommand("Enter")()
        else:
            keymap.InputKeyCommand("S-Enter")()

    def lw_exit_search(func):
        def _func():
            if keymap_lw.is_searching:
                keymap.InputKeyCommand("Enter")()
            func()
        return _func

    def lw_reset_search(func):
        def _func():
            func()
            keymap_lw.is_searching = False
        return _func

    ##################################################
    ## キーバインド（リストウィンドウ用）
    ##################################################

    ## Escキーの設定
    define_key(keymap_lw, "Esc",           lw_reset_search(self_insert_command("Esc")))
    define_key(keymap_lw, "C-OpenBracket", lw_reset_search(self_insert_command("Esc")))

    ## 「カーソル移動」のキー設定
    define_key(keymap_lw, "C-b", backward_char)
    define_key(keymap_lw, "A-b", backward_char)

    define_key(keymap_lw, "C-f", forward_char)
    define_key(keymap_lw, "A-f", forward_char)

    define_key(keymap_lw, "C-p", previous_line)
    define_key(keymap_lw, "A-p", previous_line)

    define_key(keymap_lw, "C-n", next_line)
    define_key(keymap_lw, "A-n", next_line)

    if scroll_key:
        define_key(keymap_lw, scroll_key[0].replace("M-", "A-"), scroll_up)
        define_key(keymap_lw, scroll_key[1].replace("M-", "A-"), scroll_down)

    ## 「カット / コピー / 削除 / アンドゥ」のキー設定
    define_key(keymap_lw, "C-h", delete_backward_char)
    define_key(keymap_lw, "A-h", delete_backward_char)

    define_key(keymap_lw, "C-d", delete_char)
    define_key(keymap_lw, "A-d", delete_char)

    ## 「文字列検索 / 置換」のキー設定
    define_key(keymap_lw, "C-r", lw_isearch_backward)
    define_key(keymap_lw, "A-r", lw_isearch_backward)

    define_key(keymap_lw, "C-s", lw_isearch_forward)
    define_key(keymap_lw, "A-s", lw_isearch_forward)

    ## 「その他」のキー設定
    define_key(keymap_lw, "Enter", lw_exit_search(lw_newline))
    define_key(keymap_lw, "C-m",   lw_exit_search(lw_newline))
    define_key(keymap_lw, "A-m",   lw_exit_search(lw_newline))

    define_key(keymap_lw, "C-g", lw_reset_search(lw_keyboard_quit))
    define_key(keymap_lw, "A-g", lw_reset_search(lw_keyboard_quit))

    define_key(keymap_lw, "S-Enter", lw_exit_search(self_insert_command("S-Enter")))
    define_key(keymap_lw, "C-Enter", lw_exit_search(self_insert_command("C-Enter")))
    define_key(keymap_lw, "A-Enter", lw_exit_search(self_insert_command("C-Enter")))


    ####################################################################################################
    ## クリップボードリストの設定
    ####################################################################################################
    if 1:
        # クリップボードリストを利用するための設定です。クリップボードリストは clipboardList_key 変数で
        # 設定したキーの押下により起動します。クリップボードリストを開いた後、C-f（→）や C-b（←）
        # キーを入力することで画面を切り替えることができます。
        # （参考：https://github.com/crftwr/keyhac/blob/master/_config.py）

        # リストウィンドウのフォーマッタを定義する
        list_formatter = "{:30}"

        # 定型文
        fixed_items = [
            ["---------+ x 8", "---------+" * 8],
            ["メールアドレス", "user_name@domain_name"],
            ["住所",           "〒999-9999 ＮＮＮＮＮＮＮＮＮＮ"],
            ["電話番号",       "99-999-9999"],
        ]
        fixed_items[0][0] = list_formatter.format(fixed_items[0][0])

        import datetime

        # 日時をペーストする機能
        def dateAndTime(fmt):
            def _func():
                return datetime.datetime.now().strftime(fmt)
            return _func

        # 日時
        datetime_items = [
            ["YYYY/MM/DD HH:MM:SS", dateAndTime("%Y/%m/%d %H:%M:%S")],
            ["YYYY/MM/DD",          dateAndTime("%Y/%m/%d")],
            ["HH:MM:SS",            dateAndTime("%H:%M:%S")],
            ["YYYYMMDD_HHMMSS",     dateAndTime("%Y%m%d_%H%M%S")],
            ["YYYYMMDD",            dateAndTime("%Y%m%d")],
            ["HHMMSS",              dateAndTime("%H%M%S")],
        ]
        datetime_items[0][0] = list_formatter.format(datetime_items[0][0])

        keymap.cblisters += [
            ["定型文",  cblister_FixedPhrase(fixed_items)],
            ["日時",    cblister_FixedPhrase(datetime_items)],
        ]

        def lw_clipboardList():
            keymap.command_ClipboardList()

        # クリップボードリストを起動する
        define_key(keymap_global, clipboardList_key, lw_reset_search(reset_search(reset_undo(reset_counter(reset_mark(lw_clipboardList))))))


    ####################################################################################################
    ## ランチャーリストの設定
    ####################################################################################################
    if 1:
        # ランチャー用のリストを利用するための設定です。ランチャーリストは lancherList_key 変数で
        # 設定したキーの押下により起動します。ランチャーリストを開いた後、C-f（→）や C-b（←）
        # キーを入力することで画面を切り替えることができます。
        # （参考：https://github.com/crftwr/keyhac/blob/master/_config.py）

        def lw_lancherList():
            def popLancherList():

                # リストウィンドウのフォーマッタを定義する
                list_formatter = "{:30}"

                # 既にリストが開いていたら閉じるだけ
                if keymap.isListWindowOpened():
                    keymap.cancelListWindow()
                    return

                # ウィンドウ
                window_list = getWindowList()
                window_items = []
                if window_list:
                    processName_length = max(map(len, map(Window.getProcessName, window_list)))

                    formatter = "{0:" + str(processName_length) + "} | {1}"
                    for wnd in window_list:
                        window_items.append((formatter.format(wnd.getProcessName(), wnd.getText()), popWindow(wnd)))

                window_items.append((list_formatter.format("<Desktop>"), keymap.ShellExecuteCommand(None, r"shell:::{3080F90D-D7AD-11D9-BD98-0000947B0257}", "", "")))

                # アプリケーションソフト
                application_items = [
                    ["notepad",     keymap.ShellExecuteCommand(None, r"notepad.exe", "", "")],
                    ["sakura",      keymap.ShellExecuteCommand(None, r"C:\Program Files (x86)\sakura\sakura.exe", "", "")],
                    ["explorer",    keymap.ShellExecuteCommand(None, r"explorer.exe", "", "")],
                    ["cmd",         keymap.ShellExecuteCommand(None, r"cmd.exe", "", "")],
                    ["chrome",      keymap.ShellExecuteCommand(None, r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", "", "")],
                    ["firefox",     keymap.ShellExecuteCommand(None, r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe", "", "")],
                    ["thunderbird", keymap.ShellExecuteCommand(None, r"C:\Program Files (x86)\Mozilla Thunderbird\thunderbird.exe", "", "")],
                ]
                application_items[0][0] = list_formatter.format(application_items[0][0])

                # ウェブサイト
                website_items = [
                    ["Google",          keymap.ShellExecuteCommand(None, r"https://www.google.co.jp/", "", "")],
                    ["Facebook",        keymap.ShellExecuteCommand(None, r"https://www.facebook.com/", "", "")],
                    ["Twitter",         keymap.ShellExecuteCommand(None, r"https://twitter.com/", "", "")],
                    ["Keyhac",          keymap.ShellExecuteCommand(None, r"https://sites.google.com/site/craftware/keyhac-ja", "", "")],
                    ["NTEmacs＠ウィキ", keymap.ShellExecuteCommand(None, r"http://www49.atwiki.jp/ntemacs/", "", "")],
                ]
                website_items[0][0] = list_formatter.format(website_items[0][0])

                # その他
                other_items = [
                    ["Edit   config.py", keymap.command_EditConfig],
                    ["Reload config.py", keymap.command_ReloadConfig],
                ]
                other_items[0][0] = list_formatter.format(other_items[0][0])

                listers = [
                    ["Window",  cblister_FixedPhrase(window_items)],
                    ["App",     cblister_FixedPhrase(application_items)],
                    ["Website", cblister_FixedPhrase(website_items)],
                    ["Other",   cblister_FixedPhrase(other_items)],
                ]

                try:
                    select_item = keymap.popListWindow(listers)

                    if not select_item:
                        Window.find("Progman", None).setForeground()
                        select_item = keymap.popListWindow(listers)

                    if select_item and select_item[0] and select_item[0][1]:
                        select_item[0][1]()
                except:
                    print("エラーが発生しました")

            # キーフックの中で時間のかかる処理を実行できないので、delayedCall() を使って遅延実行する
            keymap.delayedCall(popLancherList, 0)

        # ランチャーリストを起動する
        define_key(keymap_global, lancherList_key, lw_reset_search(reset_search(reset_undo(reset_counter(reset_mark(lw_lancherList))))))


    ####################################################################################################
    ## Excel の場合、^Enter に F2（セル編集モード移行）を割り当てる（オプション）
    ####################################################################################################
    if 1:
        keymap_excel = keymap.defineWindowKeymap(class_name="EXCEL*")

        # C-Enter 押下で、「セル編集モード」に移行する
        define_key(keymap_excel, "C-Enter", reset_search(reset_undo(reset_counter(reset_mark(self_insert_command("F2"))))))


    ####################################################################################################
    ## Emacs の場合、IME 切り替え用のキーを C-\ に置き換える（オプション）
    ####################################################################################################
    if 0:
        # NTEmacs の利用時に Windows の IME の切換えを無効とするための設定です。（mozc.el を利用する場合など）
        # 追加したいキーがある場合は、次の方法で追加するキーの名称もしくはコードを確認し、
        # スクリプトを修正してください。
        # 　1) タスクバーにある Keyhac のアイコンを左クリックしてコンソールを開く。
        # 　2) アイコンを右クリックしてメニューを開き、「内部ログ ON」を選択する。
        # 　3) 確認したいキーを押す。

        keymap_real_emacs = keymap.defineWindowKeymap(class_name="Emacs")

        # IME 切り替え用のキーを C-\ に置き換える
        keymap_real_emacs["(28)"]   = keymap.InputKeyCommand("C-Yen") # 「変換」キー
        keymap_real_emacs["(29)"]   = keymap.InputKeyCommand("C-Yen") # 「無変換」キー
        keymap_real_emacs["(240)"]  = keymap.InputKeyCommand("C-Yen") # 「英数」キー
        keymap_real_emacs["(242)"]  = keymap.InputKeyCommand("C-Yen") # 「カタカナ・ひらがな」キー
        keymap_real_emacs["(243)"]  = keymap.InputKeyCommand("C-Yen") # 「半角／全角」キー
        keymap_real_emacs["(244)"]  = keymap.InputKeyCommand("C-Yen") # 「半角／全角」キー
        keymap_real_emacs["A-(25)"] = keymap.InputKeyCommand("C-Yen") # 「Alt-`」 キー
