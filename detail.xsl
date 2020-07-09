<?xml version="1.0" encoding="UTF-8" ?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:my="http://my.func" version="1.0">
    <xsl:output method="html" encoding="UTF-8" indent="yes" />
    <xsl:param name="dp" />

    <xsl:template match="/">
        <h1>「<xsl:value-of select="//item[@no=$dp]/title" />」の詳細ページ</h1>
        <!-- <xsl:value-of select="my:searchform()" /> -->
        <table class="table table-striped table-hover">
            <thead>
                <tr>
                    <th scope="col">属性</th>
                    <th scope="col">値</th>
                </tr>
            </thead>
            <tbody>
                <xsl:apply-templates
                select="//item[@no=$dp]" />
            </tbody>
        </table>
        <a href="javascript:history.back();">一つ前のページへ戻る</a>
    </xsl:template>

    <xsl:template match="item">
        <tr>
            <th>書名</th><td><xsl:value-of select="title" /></td>
        </tr>
        <tr>
            <th>作者</th><td><xsl:value-of select="creator" /></td>
        </tr>
        <tr>
            <th>出版者</th><td><xsl:value-of select="publisher" /></td>
        </tr>
        <tr>
            <th>ISBN</th><td><xsl:value-of select="isbn" /></td>
        </tr>
        <tr>
            <th>価格</th><td><xsl:value-of select="price" /></td>
        </tr>
        <tr>
            <th>年</th><td><xsl:value-of select="concat(date/year,'-',
                                    format-number(date/month, '00'),'-',
                                    format-number(date/day, '00'))" /></td>
        </tr>
        <tr>
            <th>キーワード</th><td><xsl:value-of select="translate(
                                    normalize-space(keywords), ' ', ', ')" /></td>
        </tr>
        <tr>
            <th>説明</th><td><details><summary>説明文(折りたたみ)</summary><xsl:value-of select="description" /></details></td>
        </tr>
        <tr>
            <th>外部リンク</th><td><a href="{url/@resource}">リンク</a></td>
        </tr>
    </xsl:template>
</xsl:stylesheet>