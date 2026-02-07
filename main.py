"""
純鬼 - エントリーポイント
処理フロー: 01_全体フロー（プログラム起動 → Pygame初期化 → ディスプレイ作成 → タイトル → 終了）
"""

import sys                                    # システム用。パス操作や終了に利用
from pathlib import Path                      # ファイルパスを扱う。下で __file__ の親ディレクトリを取得するために使用

# プロジェクトルートを sys.path の先頭に追加。from src.game などで src を import できるようにする（main 実行時のみ）
sys.path.insert(0, str(Path(__file__).resolve().parent))

from src.game import Game                     # ゲーム本体。main() でインスタンス化して run() を呼ぶ


def main() -> None:
    """
    プログラムのメイン処理。
    ・Game のインスタンスを1つ作る
    ・run() を呼ぶとウィンドウが開き、ループが始まる（×で閉じるまで）
    ・run() が終わったらプログラム終了
    """
    game = Game()                             # ゲームを1つ作成。__init__ で Pygame 初期化・ウィンドウ・フォントなどを準備
    game.run()                                 # メインループ開始。ウィンドウが閉じるまで繰り返し、終了時に pygame.quit()


# このファイルを python main.py で実行したときだけ main() を呼ぶ。他ファイルから import されたときは呼ばない
if __name__ == "__main__":
    main()
