"""
純鬼 - ゲーム定数・設定
docs/処理フロー図.md（全体フロー・メインループ）、docs/要件定義書.md を参照。
数値や色をここにまとめておくと、あとで変更しやすい。
"""

# --- 画面の大きさとフレームレート ---
# 処理フロー「01_全体フロー」の「ディスプレイ作成 1280x720」に対応
SCREEN_WIDTH = 1280                                                         # 画面幅（px）。game.py の set_mode、ui/draw.py の描画位置で使用
SCREEN_HEIGHT = 720                                                         # 画面高さ（px）。game.py の set_mode、ui/draw.py の描画位置で使用
FPS = 60                                                                    # 1秒あたりのフレーム数。game.py の clock.tick(FPS) で使用

# --- 色（R, G, B）---
# 各色は 0～255 の3つの数値のタプル。(0,0,0)=黒、(255,255,255)=白
COLOR_BLACK = (0, 0, 0)                                                     # 黒。ui/draw.py の fill（背景）で使用
COLOR_WHITE = (255, 255, 255)                                               # 白。ui/draw.py の font.render（文字色）で使用

# 壁などに使うグレー（R,G,B を同じにするとグレーになる）
COLOR_GRAY = (64, 64, 64)                                                   # 壁・影用。今後 map 描画などで使用予定

# --- フォント（日本語表示用）---
# 日本語が表示されるフォントのパス。複数ある場合は先に見つかったものを使う
FONT_SIZE = 36                                                              # フォントサイズ。game.py の _create_font で使用
# macOS / Windows のシステムフォント、またはプロジェクトの assets/fonts/ 内のフォント
FONT_PATHS_TO_TRY = [                                                       # game.py の _create_font で順に試し、存在するパスで Font を生成
    "/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc",  # macOS
    "/System/Library/Fonts/Supplemental/Hiragino Sans GB.ttc",
    "/Library/Fonts/Arial Unicode.ttf",
    "C:\\Windows\\Fonts\\meiryo.ttc",                                       # Windows メイリオ
]
# --- ゲーム状態（run() の分岐・描画切り替えで使用）---
STATE_TITLE = "title"                                                       # タイトル画面。game.py の self.state の初期値・比較で使用
STATE_PLAYING = "playing"                                                   # プレイ中。game.py の game_start() で self.state に代入して使用
