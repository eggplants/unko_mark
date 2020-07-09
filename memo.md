# 2020年度マークアップ言語 学期末課題

- 201811528 春名航亨 (知識情報・図書館学類)

## 0. システム図

![figure](repimg/figure.png)
図1: システムの全体図

## 1. 作成したXSLTスタイルシートと解説

### search.xsl

- 概要
  - `keyword`と`type`の2パラメータで書籍を検索
    - `type`は検索する要素
  - 件数と結果のtable要素を返す
- 工夫した点
  - 書影
    - 外部関数`my:get-bookimg(isbn)`
  - 検索フォームで再検索可能に
    - フォーム群を返す外部関数`my:searchform()`
  - 著者名から再検索可能にするに、各著者にリンクをつけた
    - 外部関数`my:split(text)`

### detail.xsl

- 概要
  - `item/@no`のパラメータで書籍を検索
- 工夫した点
  - 書影
    - 外部関数`my:get-bookimg(isbn)`

## 2. CGIプログラムと解説

### result.cgi

- 概要
  - `search.xsl`処理実行/検索結果表示
- 工夫した点
  - 便利な独自関数を定義
    - `get-bookimg(isbn)`, `split(text)`, `searchform`
  - ヒアドキュメントで可読性向上

### detail.cgi

- 概要
  - `detail.xsl`処理実行/書誌情報表示
- 工夫した点
  - 便利な独自関数を定義
  - `get-bookimg(isbn)`, `searchform`
  - ヒアドキュメントで可読性向上

## 3. ウェブブラウザで表示した実行画面とその解説

- https://cgi.u.tsukuba.ac.jp/~s1811528/unko_mark
  - 学外公開

![figure](repimg/index.png)
図2: トップページ
![figure](repimg/search.png)
図3: 検索結果ページ
![figure](repimg/search2.png)
図4: 著者選択->再検索
![figure](repimg/detail.png)
図5: 詳細ページ

## 4. 授業の感想

- XSLTをこの先使うことはないと思う。
- しかしXMLの形式やRubyでの処理に関しての知見が深まった。
