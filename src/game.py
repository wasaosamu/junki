"""
純鬼 - メインゲームループ・画面状態
処理フロー: 01_全体フロー, 02_メインゲームループ
  起動 → Pygame初期化 → ディスプレイ作成 → タイトル画面 → ループ（イベント・描画・tick）→ 終了
エンディング処理は未実装（後で追加）。
"""

import pygame

from src.config import (
    COLOR_BLACK,
    COLOR_WHITE,
    FPS,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)


class Game:
    """
    ゲーム全体を管理するクラス。
    ・ウィンドウ（screen）と時計（clock）、フォントを持つ
    ・run() で「イベントを見る → 描画する → 60FPSで待つ」を繰り返す
    """

    def __init__(self) -> None:
        """ゲーム開始時に1回だけ実行される。Pygame とウィンドウの準備をする。"""
        # Pygame の各機能（画面・キー・フォントなど）を初期化
        pygame.init()

        # 描画先のウィンドウを作成。サイズは config の定数を使用
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        # ウィンドウのタイトルバーに表示する文字
        pygame.display.set_caption("純鬼")

        # フレームレート（60FPS）を守るための時計
        self.clock = pygame.time.Clock()
        # 文字を描画するときのフォント（None = デフォルト、36 = サイズ）
        self.font = pygame.font.Font(None, 36)

    def run(self) -> None:
        """
        メインループ。ウィンドウが閉じられるまで繰り返す。
        処理の流れ（02_メインゲームループ）:
          1. イベント取得（キー入力や×ボタンなど）
          2. 描画（今はタイトル画面）
          3. 画面を更新（flip）
          4. 60FPS になるよう待つ（tick）
        """
        running = True

        while running:
            # ---------- 1. イベント取得 ----------
            # このフレームで起きた「できごと」を全部取得する
            for event in pygame.event.get():
                # ウィンドウの×ボタンが押されたら終了
                if event.type == pygame.QUIT:
                    running = False
                    break

            if not running:
                break

            # ---------- 2. 描画 ----------
            # タイトル画面を描画（中身は ui/draw.py の draw_title_screen に任せる）
            self._draw_title()
            # 描画した内容を実際に画面に反映する
            pygame.display.flip()
            # ---------- 3. フレームレート制御 ----------
            # 1秒間に FPS 回（60回）になるように待つ。ループが速くなりすぎないようにする
            self.clock.tick(FPS)

        # ループを抜けたら Pygame を終了する（お片付け）
        pygame.quit()

    def _draw_title(self) -> None:
        """
        タイトル画面を描画する。
        実際の描画は src.ui.draw の draw_title_screen に任せている。
        （あなたが draw_title_screen を実装すると、ここから呼ばれる）
        """
        from src.ui.draw import draw_title_screen
        draw_title_screen(self.screen, self.font)
