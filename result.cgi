#!/usr/bin/ruby
require 'cgi'
require 'xml/xslt'

cgi = CGI.new

# Content-Type
puts cgi.header("text/html; charset=UTF-8")

# metaとか
puts <<~HTML
<html>
    <head>
        <title>検索結果 - はい</title>
        <meta name="description" content="かんたん検索" />
        <meta name="keywords" content="ゴミ,筑波大学" />
        <meta name="author" content="春名" />
        <meta name="twitter:card" content="summary" />
        <meta name="twitter:creator" content="@egpl0">
        <meta name="twitter:site" content="@egpl0" />
        <meta property="og:url" content="logo.png" />
        <meta property="og:title" content="かんたん検索" />
        <meta property="og:description" content="かんたんに書誌を検索." />
        <meta property="og:image" content="https://cgi.u.tsukuba.ac.jp/~s1811528/unko_mark/logo.png">
        <link rel="icon" href="favicon.ico" />
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
        integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous" />
    </head>
    <body>
        <nav class="navbar navbar-light bg-light">
            <a class="navbar-brand" href="index.html">かんたん検索</a>
        </nav>
        <div class="container">
            <h1>検索結果</h1>
HTML

## 外部関数の定義
XML::XSLT.registerExtFunc("http://my.func", "get-bookimg") {|isbn|
    "https://cover.openbd.jp/#{isbn[0]}.jpg"
}
XML::XSLT.registerExtFunc("http://my.func", "split") {|text|
    a = text[0].force_encoding('UTF-8')
    a.split(/(，|,|、)\s*/)
    .map {|t|
        REXML::Document.new("<t>#{t}</t>").root
    }
}
XML::XSLT.registerExtFunc("http://my.func", "searchform") {
    puts  <<~HTML
        <form action="result.cgi" method="GET" role="form" class="form-horizontal">
            <div class="input-group justify-content-center">
                <input type="text" name="keyword" class="form-control" placeholder="Please Input" />
                <select class="custom-select" name="type">
                    <option value="title" selected>書名</option>
                    <option value="creator">作者</option>
                    <option value="publisher">出版者</option>
                    <option value="description">説明</option>
                    <option value="price">価格</option>
                    <option value="date">年</option>
                    <option value="isbn">ISBN</option>
                    <option value="keywords">キーワード</option>
                </select>
                <span class="input-group-btn">
                    <button type="submit" class="btn btn-primary">検索</button>
                </span>
            </div>
        </form>
HTML
}

# 検索件数&&検索結果リスト
xslt = XML::XSLT.new
xslt.xml = "data0511.xml"
xslt.xsl = "search.xsl"
xslt.parameters = 
    cgi.params.map {|k, v|
        [k, v[0].to_s]
    }.to_h
puts xslt.serve

puts <<~HTML
        </div>
        <footer class="page-footer font-small white">
            <div class="footer-copyright text-center py-3">
                &copy; 2020 Copyright: Haruna(eggplants)
                Repository: <a href="https://github.com/eggplants/unko_mark">Here.</a>
            </div>
        </footer>
    </body>
</html>
HTML