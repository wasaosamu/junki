"""
純鬼 - メインゲームループ・画面状態
処理フロー: 01_全体フロー, 02_メインゲームループ
  起動 → Pygame初期化 → ディスプレイ作成 → タイトル画面 → ループ（イベント・描画・tick）→ 終了
エンディング処理は未実装（後で追加）。
"""

from pathlib import Path                                                    # ファイルパス取得。_create_font でプロジェクトルート・assets/fonts を参照
import pygame                                                               # ゲーム用ライブラリ。画面・イベント・フォント・Clock などで使用

from src.config import (                                                    # 定数はすべてこのモジュールで参照。画面サイズ・FPS・色・状態名・フォント設定
    COLOR_BLACK,
    COLOR_WHITE,
    FONT_PATHS_TO_TRY,
    FONT_SIZE,
    FPS,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    STATE_TITLE,
    STATE_PLAYING
)


class Game:
    """
    ゲーム全体を管理するクラス。
    ・ウィンドウ（screen）と時計（clock）、フォントを持つ
    ・run() で「イベントを見る → 描画する → 60FPSで待つ」を繰り返す
    """

    def __init__(self) -> None:
        """ゲーム開始時に1回だけ実行される。Pygame とウィンドウの準備をする。"""
        pygame.init()                                                       # Pygame のサブシステムを初期化。以降 set_mode / Font / event などが使える

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                                                                       # 描画先ウィンドウ。_draw_title / 今後のプレイ描画で使用
        pygame.display.set_caption("純鬼")                                   # ウィンドウのタイトルバーに表示する文字

        self.clock = pygame.time.Clock()                                    # FPS 制御用。run() の clock.tick(FPS) で使用
        self.font = self._create_font()                                     # 文字描画用フォント。_draw_title → draw_title_screen に渡して使用
        self.state = STATE_TITLE                                            # 現在の画面状態。run() のイベント分岐・描画分岐（今後）で使用。起動時はタイトル

    def _create_font(self) -> pygame.font.Font:
        """日本語対応フォントを探して返す。見つからなければデフォルトフォント。"""
        project_root = Path(__file__).resolve().parent.parent               # プロジェクトルート（純鬼/）。config の次に src がある
        paths_to_try = list(FONT_PATHS_TO_TRY)                              # 試すフォントパスのリスト。下の for で順に存在チェック
        assets_fonts = project_root / "assets" / "fonts"                     # プロジェクト内フォントフォルダ。ここに .ttf 等があれば候補に追加
        if assets_fonts.exists():
            for ext in ("*.ttf", "*.ttc", "*.otf"):
                for f in assets_fonts.glob(ext):
                    paths_to_try.append(str(f))                             # 1つ見つかったらその拡張子では追加終了
                    break
        for path_str in paths_to_try:
            p = Path(path_str)
            if not p.is_absolute():                                         # 相対パスならプロジェクトルート基準にする
                p = project_root / path_str
            if p.exists():
                try:
                    return pygame.font.Font(str(p), FONT_SIZE)              # 日本語表示用フォントを返す。__init__ の self.font に代入される
                except OSError:
                    continue
        return pygame.font.Font(None, FONT_SIZE)                             # どれも使えなければデフォルト。日本語は文字化けする可能性あり

    def run(self) -> None:
        """
        メインループ。ウィンドウが閉じられるまで繰り返す。
        処理の流れ（02_メインゲームループ）:
          1. イベント取得（キー入力や×ボタンなど）
          2. 描画（今はタイトル画面）
          3. 画面を更新（flip）
          4. 60FPS になるよう待つ（tick）
        """
        running = True                                                      # ループを続けるか。QUIT で False になり while を抜ける

        while running:
            for event in pygame.event.get():                                # このフレームのイベントをすべて取得。キー・マウス・×ボタンなど
                if event.type == pygame.QUIT:                               # ウィンドウの×が押されたとき
                    running = False
                    break

            if not running:
                break

            self._draw_title()                                              # タイトル画面を描画。中で draw_title_screen(self.screen, self.font) を呼ぶ
            pygame.display.flip()                                           # 描画内容を画面に反映。毎フレーム必須
            self.clock.tick(FPS)                                            # 1秒あたり FPS 回になるよう待つ。ループが速くなりすぎないようにする

        pygame.quit()                                                       # ループ終了後の後処理。Pygame のリソースを解放

    def _draw_title(self) -> None:
        """
        タイトル画面を描画する。
        実際の描画は src.ui.draw の draw_title_screen に任せている。
        """
        from src.ui.draw import draw_title_screen                           # 関数内 import。draw_title_screen はこのメソッド内でのみ使用
        draw_title_screen(self.screen, self.font)                           # 黒背景・タイトル文字・メニュー文字を screen に描画

    def game_start(self) -> None:
        """
        新規ゲーム開始。タイトルで Enter が押されたときに呼ぶ想定。
        """
        self.state = STATE_PLAYING                                          # 状態をプレイ中に変更。run() の描画分岐でプレイ画面を描くようにする（今後実装）
