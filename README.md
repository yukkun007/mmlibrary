# mmlibrary

[![CircleCI](https://circleci.com/gh/yukkun007/mmlibrary/tree/master.svg?style=svg)](https://circleci.com/gh/yukkun007/mmlibrary/tree/master)
[![Build Status](https://travis-ci.org/yukkun007/mmlibrary.svg?branch=master)](https://travis-ci.org/yukkun007/mmlibrary)
[![codecov](https://codecov.io/gh/yukkun007/mmlibrary/branch/master/graph/badge.svg)](https://codecov.io/gh/yukkun007/mmlibrary)
[![Maintainability](https://api.codeclimate.com/v1/badges/3cfd46f37e08d3772808/maintainability)](https://codeclimate.com/github/yukkun007/mmlibrary/maintainability)
[![Requirements Status](https://requires.io/github/yukkun007/mmlibrary/requirements.svg?branch=master)](https://requires.io/github/yukkun007/mmlibrary/requirements/?branch=master)

図書館で借りた本, 予約した本の状況を取得するライブラリ。

## 必要な環境変数

プロジェクトディレクトリ直下に.envファイルを配置して下記を記載。

```(sh)
USER1='{"name": "yukkun007", "disp_name": "表示する名前", "id": "1111111", "password": "xxxxxxx"}'
USER2='......'
USER3='......'
USER4='......'
CHROME_BINARY_LOCATION='/usr/bin/google-chrome'
CHROME_DRIVER_LOCATION='/usr/local/bin/chromedriver'
```

## 依存

下記が必要。  
バージョンを合わせる必要がある。  

- Chrome(headless-chromium)
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

### Chrome

AWS(lambda)で動作させる場合、[serverless-chrome](https://github.com/adieuadieu/serverless-chrome/releases)が使える。
[ここ](https://hacknote.jp/archives/49974/)の通り、lambda layerにあげて使う。
lambda layerにはChromeDriverも合わせてあげる。
layerでは/opt/に配置されるので、それぞれ下記環境変数で場所を指定する。  

```(sh)
CHROME_BINARY_LOCATION='/opt/headless/python/bin/headless-chromium'
CHROME_DRIVER_LOCATION='/opt/headless/python/bin/chromedriver'
```

#### [serverless-chrome](https://github.com/adieuadieu/serverless-chrome/releases)のChromeバージョン

[ここ](https://github.com/adieuadieu/serverless-chrome/issues/133)の通り、最新のバージョン(1.0.0-55)では動かせなかった。以下の組み合わせしか動かない。

- selenium==3.141.0
- chromedriver==2.37
- [severless-chrome](https://github.com/adieuadieu/serverless-chrome/releases)==1.0.0-37 (64.0.3282.167 stable channel)

### ChromeDriver

ChromeDriverはpythonモジュール([chromedriver-binary](https://pypi.org/project/chromedriver-binary/#history))でも導入出来るが複雑になるのでやってない。

## インストール

```(sh)
pip install git+https://github.com/yukkun007/mmlibrary
```

## アップグレード

```(sh)
pip install --upgrade git+https://github.com/yukkun007/mmlibrary
```

## 使い方 (コードからモジュールを利用)

[参照](#モジュールを利用)

## 使い方 (コマンドラインアプリ)

```(sh)
mmlibrary --help
```

## アンインストール

```(sh)
pip uninstall mmlibrary
```

## 開発フロー

### 環境構築

1. プロジェクトディレクトリに仮想環境を作成するために下記環境変数を追加

   - Linux

     ```(sh)
     export PIPENV_VENV_IN_PROJECT=true
     ```

   - Windows

     ```(sh)
     set PIPENV_VENV_IN_PROJECT=true
     ```

1. `pip install pipenv`
1. `git clone git@github.com:yukkun007/mmlibrary.git`
1. `pipenv install --dev`

### install package

下記は編集可能モードでインストールされる。

```(sh)
pip install -e .
```

通常のインストールは下記だがソース編集の都度`upgrade package`が必要なので基本は`-e`をつける。

```(sh)
pip install .
```

### upgrade package

```(sh)
pip install --upgrade . (もしくは-U)
```

## 開発行為

### モジュールを利用

```(python)
$ python
>>> import mmlibrary
>>> messages = mmlibrary.search_rental({
    "mode": "rental",
    "all_user": False,
    "users": ["hoge"],
    "debug": False,
    "zero_behavior": "message",
    "separate": False
})
>>> import pprint
>>> pprint.pprint(messages)
```

### コマンドラインアプリを実行

```(sh)
pipenv run start (もしくはmmlibrary)
```

### unit test

```(sh)
pipenv run ut
```

### lint

```(sh)
pipenv run lint
```

### create api document (sphinx)

```(sh)
pipenv run doc
```

## 配布物関連

<details>

### ソースコード配布物の作成

dist/ 以下に mmlibrary-0.0.1.tar.gz が生成される。

```(sh)
python setup.py sdist
```

### ソースコード配布物から pip でインストール

```(sh)
pip install mmlibrary-0.0.1-tar.gz
```

### ビルド済み配布物(wheel 形式)の作成

dist/ 以下に mmlibrary-0.0.1-py3-none-any.whl が生成される。

```(sh)
python setup.py bdist_wheel (wheelパッケージが必要)
```

### ビルド済み配布物(wheel 形式)から pip でインストール

```(sh)
pip install mmlibrary-0.0.1-py3-none-any.whl
```

</details>

## 参考

<details>

### パッケージング/開発環境

- <https://techblog.asahi-net.co.jp/entry/2018/06/15/162951>
- <https://techblog.asahi-net.co.jp/entry/2018/11/19/103455>

### コマンドライン引数のパース

- <https://qiita.com/kzkadc/items/e4fc7bc9c003de1eb6d0>

### 環境変数の定義

- <https://pod.hatenablog.com/entry/2019/04/29/164109>

### TravisCIでファイルを(簡単に)暗号化して使用する

- <https://qiita.com/kmats@github/items/d22fd856883e6c16d7ea>

</details>
