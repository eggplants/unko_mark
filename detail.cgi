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
        <title>詳細表示 - はい</title>
        <meta name="description" content="かんたん検索" />
        <meta name="keywords" content="ゴミ,筑波大学" />
        <meta name="author" content="春名" />
        <meta name="twitter:card" content="summary" />
        <meta name="twitter:creator" content="@egpl0">
        <meta name="twitter:site" content="@egpl0" />
        <meta property="og:url" content="" />
        <meta property="og:title" content="かんたん検索" />
        <meta property="og:description" content="かんたんに書誌を検索." />
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
        integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous" />
    </head>
    <body>
        <nav class="navbar navbar-light bg-light">
            <a class="navbar-brand" href="index.html">かんたん検索</a>
        </nav>
        <div class="container">
HTML

# 外部関数の定義
XML::XSLT.registerExtFunc("http://my.func", "get-bookimg") {|isbn|
    "https://cover.openbd.jp/#{isbn[0]}.jpg"
}

# 詳細リスト
xslt = XML::XSLT.new
xslt.xml = "data0511.xml"
xslt.xsl = "detail.xsl"
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