# 純鬼（じゅんき）

2D ホラーアドベンチャーゲーム。廃墟の美術館を舞台に、謎解きと追跡ホラーを融合した脱出ゲームです。

## 技術スタック

| 項目 | 技術 |
|------|------|
| 言語 | Python 3.14.2 |
| 仮想環境 | venv |
| ゲーム開発 | Pygame（2D、フレームワーク不要） |
| DB | SQLite（Python 標準 sqlite3） |

詳細は [docs/要件定義書.md](docs/要件定義書.md) を参照してください。

## venv 仮想環境の使い方

### 1. 仮想環境の作成（初回のみ）

```bash
cd /Users/fukumotoryou/projects/my-python/純鬼
python3 -m venv venv
```

### 2. 仮想環境の有効化

**macOS / Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

有効化するとプロンプトの先頭に `(venv)` が表示されます。

### 3. ライブラリのインストール

```bash
# requirements.txt から一括インストール
pip install -r requirements.txt

# 個別にライブラリをインストール（例）
pip install pygame

# インストール済みライブラリを requirements.txt に出力
pip freeze > requirements.txt
```

#### macOS で `SDL.h file not found` が出る場合

Pygame はビルド時に SDL2 が必要です。先に Homebrew で SDL2 を入れてから `pip install` してください。

```bash
# Homebrew が未導入なら https://brew.sh でインストール後、
brew install sdl2 sdl2_image sdl2_mixer sdl2_ttf pkg-config

# その後
pip install -r requirements.txt
```

参考: [Pygame MacCompile](https://pygame.org/wiki/MacCompile)

### 4. 仮想環境の無効化

```bash
deactivate
```

### 5. Python の実行

```bash
python main.py
```

## プロジェクト構成

```
純鬼/
├── venv/           # 仮想環境（.gitignore で除外）
├── main.py         # メインエントリーポイント
├── requirements.txt
├── docs/           # ドキュメント
│   ├── 要件定義書.md
│   ├── 処理フロー図.md
│   ├── 処理チェックリスト.md
│   ├── diagrams/   # draw.io 用フロー図（.drawio）
│   ├── 純鬼_オリジナルストーリー.md
│   └── 青鬼ストーリー.md
└── README.md
```
