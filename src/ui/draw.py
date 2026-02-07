"""
純鬼 - タイトル・ゲームオーバー・プレイ中UIの描画
メインループから呼ばれる描画関数をこのファイルに書く。
"""

import pygame                                 # 描画用。Surface / Font / blit / fill などで使用

from src.config import COLOR_BLACK, COLOR_WHITE, SCREEN_HEIGHT, SCREEN_WIDTH  # 色と画面サイズ。描画位置・背景色で使用


def draw_title_screen(screen: pygame.Surface, font: pygame.font.Font) -> None:
    """
    タイトル画面を描画する関数。
    ・screen: 描画先の画面（game.py の self.screen が渡される）
    ・font: 文字を描くときに使うフォント（game.py の self.font が渡される）
    呼び出し元: game.py の _draw_title()
    """
    screen.fill(COLOR_BLACK)                   # 画面全体を黒で塗りつぶす。背景になる

    title = font.render("純鬼（じゅんき）", True, COLOR_WHITE)   # タイトル文字の画像（Surface）を作成
    tr = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40))  # 画面中央やや上に配置する矩形
    screen.blit(title, tr)                     # タイトルを screen に描画

    sub = font.render("終了: ウィンドウの × ボタン", True, COLOR_WHITE)  # サブテキストの画像を作成
    sr = sub.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))     # タイトルの下に配置する矩形
    screen.blit(sub, sr)                      # サブテキストを screen に描画

    menu_text = font.render("はじめる: Enter  つづきから: L  終了: Q", True, COLOR_WHITE)  # メニュー文字の画像を作成
    mr = menu_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))           # さらに下に配置する矩形
    screen.blit(menu_text, mr)                # メニュー文字を screen に描画
