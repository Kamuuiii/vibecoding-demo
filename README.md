# Vibe Palette Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

「静かな森」「未来都市の夜」のような雰囲気やテーマを言葉で伝えるだけで、AIがインスピレーション溢れるカラーパレットを生成してくれるデスクトップ・アプリケーションです。



---

## ## 概要

**Vibe Palette Generator** は、デザイナーやクリエイターの創造的な活動をサポートするツールです。抽象的なイメージから具体的な配色パターンを提案することで、アイデア出しやデザイン作業の初期段階をスムーズにします。

このアプリケーションは、以下の2つの強力なAPIを連携させて動作します。
1.  **Unsplash API**: 入力されたキーワードに最適な画像を検索します。
2.  **Imagga API**: 見つかった画像を解析し、その画像から象徴的なカラーパレットを抽出します。

---

## ## 主な機能

* **キーワード入力**: 雰囲気やテーマを自由にテキストで入力できます。
* **画像ベースの配色生成**: 入力されたキーワードに合った画像をAIが探し出し、その画像の色構成に基づいた調和の取れたカラーパレットを生成します。
* **ビジュアル表示**: 生成されたカラーパレットと、インスピレーションの元になった画像が並べて表示され、直感的に結果を把握できます。
* **カラーコード表示**: 各色のHEXコードやRGB値を表示し、デザインツールへ簡単にコピー＆ペーストできます。

---

## ## 使用技術

* **言語**: Python
* **ライブラリ**: `requests`, `tkinter`
* **外部API**:
    * [Unsplash API](https://unsplash.com/developers) (画像検索)
    * [Imagga API](https://imagga.com/) (色抽出)

---

## ## セットアップ & 実行方法

このアプリケーションを実行するには、以下の手順に従ってください。

### ### 1. リポジトリのクローン
```bash
git clone [https://github.com/your-username/vibe-palette-generator.git](https://github.com/your-username/vibe-palette-generator.git)
cd vibe-palette-generator
```

### ### 2. 必要なライブラリのインストール
```bash
pip install requests
```

### ### 3. APIキーの設定
このアプリケーションを実行するには、**Unsplash**と**Imagga**のAPIキーが必要です。

1.  プロジェクトのルートディレクトリに `.env` という名前のファイルを作成します。
2.  以下の内容をコピー＆ペーストし、ご自身が取得したAPIキーに書き換えてください。

    ```.env
    UNSPLASH_ACCESS_KEY="YOUR_UNSPLASH_ACCESS_KEY"
    IMAGGA_API_KEY="YOUR_IMAGGA_API_KEY"
    IMAGGA_API_SECRET="YOUR_IMAGGA_API_SECRET"
    ```
    * *注意: `.env` ファイルを `git` の管理対象に含めないように、`.gitignore` ファイルに `.env` と追記することを推奨します。*
    * *APIキーの読み込みには `python-dotenv` などのライブラリを追加でインストールするか、直接コードに書き込む方法があります。*

### ### 4. アプリケーションの実行
以下のコマンドでアプリケーションを起動します。

```bash
python main.py
```
起動するとウィンドウが表示され、キーワードを入力してカラーパレットを生成できます。

---

## ## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細については `LICENSE` ファイルをご覧ください。