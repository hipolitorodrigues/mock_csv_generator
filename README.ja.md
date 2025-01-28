<div align="center">
   <img height="30" width="40" src="https://github.com/hipolitorodrigues/mock_csv_generator/blob/e3f4b6240ef8b99934e7383aeafac11e1c1819d2/assets/images/img-readme-ico.svg">
    <a href="./README.md">
      <img height="30" width="120" src="https://github.com/hipolitorodrigues/mock_csv_generator/blob/e3f4b6240ef8b99934e7383aeafac11e1c1819d2/assets/images/img-readme-en.svg">
   </a>
   <a href="./RREADME.ja.md">
      <img height="30" width="60" src="https://github.com/hipolitorodrigues/mock_csv_generator/blob/e3f4b6240ef8b99934e7383aeafac11e1c1819d2/assets/images/img-readme-ja.svg">
   </a>
   <a href="./README.hi.md">
      <img height="30" width="60" src="https://github.com/hipolitorodrigues/mock_csv_generator/blob/e3f4b6240ef8b99934e7383aeafac11e1c1819d2/assets/images/img-readme-hi.svg">
   </a>
   <a href="./README.pt-BR">
      <img height="30" width="60" src="https://github.com/hipolitorodrigues/mock_csv_generator/blob/e3f4b6240ef8b99934e7383aeafac11e1c1819d2/assets/images/img-readme-pt-br.svg">
   </a>
</div>

# モック CSV ジェネレーター

**モック CSV ジェネレーター** は、Python と Tkinter を使用して開発されたデスクトップアプリケーションです。ユーザーが定義した設定に基づいてカスタム CSV ファイルを作成できます。テストやプロトタイプ作成のためのモックデータ生成に最適です。

![alt text](https://github.com/hipolitorodrigues/mock_csv_generator/blob/88853b15db5302aba301f4e70edf7a7e2503a11f/assets/images/sampling.png)

![alt text](https://github.com/hipolitorodrigues/mock_csv_generator/blob/ad0ad82c9a6114ccceee7eed0f983b205cf64991/assets/images/screenshot.png)

## 特徴

1. **カスタム CSV 作成**:
   - カスタムヘッダーと値を使用して列を設定。
   - 生成する行数を指定可能。

2. **設定管理**:
   - **設定の保存**: 現在の設定（ヘッダーと列の値）を JSON ファイルに保存。
   - **設定の読み込み**: JSON ファイルまたは `DATA_CONFIG.py` モジュールから保存済みの設定を読み込み。
   - **設定のクリア**: すべての列を初期状態にリセット。

3. **ユーザーフレンドリーな GUI**:
   - Tkinter を使用した直感的なインターフェース。
   - 最大 8 列の設定をサポート。

## 使用方法

1. **列の設定**:
   - 各列にヘッダーを追加。
   - 各列に可能な値を入力。

2. **CSV の生成**:
   - 必要な行数を入力。
   - 「Generate CSV」をクリックすると、プログラムと同じディレクトリに `mokup-00.csv` ファイルが作成されます。

3. **設定管理**:
   - 設定の保存や読み込みには「Configuration」メニューを使用:
     - 「Load from JSON」: JSON ファイルから読み込む。
     - 「Load from DATA_CONFIG.py」: Python モジュールから読み込む（利用可能な場合）。
     - 「Save Configuration」: 現在の設定を保存。
     - 「Clear All」: すべての設定をリセット。

## 実行方法

1. **必要条件**:
   - Python 3.8 以上。
   - 標準ライブラリ（`tkinter`、`json`、`csv`）。

2. **実行**:
   - コードをダウンロード。
   - `main.py` を実行:
     ```bash
     python main.py
     ```

3. **生成されるファイル**:
   - 保存された設定は `column_config.json` に保存されます。
   - 生成された CSV ファイルは `mokup-00.csv` として保存されます。

## 使用技術

- **Python 3.13.1**: ロジックとバックエンド。
- **Tkinter**: シンプルでレスポンシブなグラフィカルインターフェース。

## プロジェクト構成

- `main.py`: メインアプリケーションコード。
- `column_config.json`: （オプション）ユーザーが保存した設定を格納。
- `DATA_CONFIG.py`: （オプション）Python モジュールを介してカスタム設定を読み込むためのファイル。

## 作者

- **開発者**: Hipolito Rodrigues  
- **作成日**: 2025年1月23日  
- **最終更新日**: 2025年1月27日  
- **現在のバージョン**: 1.3.4  

---

## ライセンス

このプロジェクトは [CC0 1.0 Universal (Public Domain)](https://creativecommons.org/publicdomain/zero/1.0/) ライセンスの下でライセンスされています。これにより、この作品をコピー、変更、配布、商業目的で使用することが、許可を求めることなく可能です。
