"""
純鬼 - ゲーム定数・設定
docs/処理フロー図.md（全体フロー・メインループ）、docs/要件定義書.md を参照。
数値や色をここにまとめておくと、あとで変更しやすい。
"""

# --- 画面の大きさとフレームレート ---
# 処理フロー「01_全体フロー」の「ディスプレイ作成 1280x720」に対応
SCREEN_WIDTH = 1280   # 画面の幅（ピクセル）
SCREEN_HEIGHT = 720   # 画面の高さ（ピクセル）
FPS = 60              # 1秒間に何回画面を更新するか（60 = なめらか）

# --- 色（R, G, B）---
# 各色は 0～255 の3つの数値のタプル。(0,0,0)=黒、(255,255,255)=白
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

# 壁などに使うグレー（R,G,B を同じにするとグレーになる）
COLOR_GRAY = (64, 64, 64)

# --- フォント（日本語表示用）---
# 日本語が表示されるフォントのパス。複数ある場合は先に見つかったものを使う
FONT_SIZE = 36
# macOS / Windows のシステムフォント、またはプロジェクトの assets/fonts/ 内のフォント
FONT_PATHS_TO_TRY = [
    "/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc",  # macOS
    "/System/Library/Fonts/Supplemental/Hiragino Sans GB.ttc",
    "/Library/Fonts/Arial Unicode.ttf",
    "C:\\Windows\\Fonts\\meiryo.ttc",  # Windows メイリオ
]
