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
                    <option value="year">年</option>
                    <option value="isbn">説明</option>
                    <option value="keyword">キーワード</option>
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
xslt.xsl = "detail.xsl"
xslt.parameters = 
    cgi.params.map {|k, v|
        [k, v[0].to_s]
    }.to_h
puts xslt.serve

puts <<~HTML
        </div>
    </body>
</html>
HTML