"""
純鬼 - エントリーポイント
処理フロー: 01_全体フロー（プログラム起動 → Pygame初期化 → ディスプレイ作成 → タイトル → 終了）
"""

import sys
from pathlib import Path

# --- モジュールの検索パスを設定 ---
# Python が「from src.game import Game」で src フォルダを見つけられるように、
# このファイル（main.py）があるフォルダ（プロジェクトルート）を path に追加する
sys.path.insert(0, str(Path(__file__).resolve().parent))

# --- ゲーム本体のクラスを読み込む ---
from src.game import Game


def main() -> None:
    """
    プログラムのメイン処理。
    ・Game のインスタンスを1つ作る
    ・run() を呼ぶとウィンドウが開き、ループが始まる（×で閉じるまで）
    ・run() が終わったらプログラム終了
    """
    game = Game()
    game.run()


# --- このファイルを「python main.py」で実行したときだけ main() を呼ぶ ---
# 他のファイルから「import main」したときは main() は呼ばれない
if __name__ == "__main__":
    main()
