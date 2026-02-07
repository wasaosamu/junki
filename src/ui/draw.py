"""
純鬼 - タイトル・ゲームオーバー・プレイ中UIの描画
メインループから呼ばれる描画関数をこのファイルに書く。
"""

import pygame

# config の定数（画面サイズや色）を使うため import
from src.config import COLOR_BLACK, COLOR_WHITE, SCREEN_HEIGHT, SCREEN_WIDTH


def draw_title_screen(screen: pygame.Surface, font: pygame.font.Font) -> None:
    """
    タイトル画面を描画する関数。
    ・screen: 描画先の画面（game.py の self.screen が渡される）
    ・font: 文字を描くときに使うフォント（game.py の self.font が渡される）
    """
    # --- 画面を黒で塗りつぶす（これで背景が黒になる）---
    screen.fill(COLOR_BLACK)

    # --- タイトル用の文字「純鬼（じゅんき）」を描画（こちらは実装済み）---
    # 1) 文字の画像（Surface）を作る:  render(文字, アンチエイリアス, 色)
    title = font.render("純鬼（じゅんき）", True, COLOR_WHITE)
    # 2) その画像を「どこに置くか」の矩形を作る: center= で画面中央の少し上に指定
    tr = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40))
    # 3) 画面に貼り付ける: blit(貼り付ける画像, 位置の矩形)
    screen.blit(title, tr)

    # --- サブテキスト「終了: ウィンドウの × ボタン」をタイトルの下に描画 ---
    sub = font.render("終了: ウィンドウの × ボタン", True, COLOR_WHITE)
    sr = sub.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))
    screen.blit(sub, sr)
