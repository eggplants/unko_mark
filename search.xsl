<?xml version="1.0" encoding="UTF-8" ?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:my="http://my.func" version="1.0">
    <xsl:output method="html" encoding="UTF-8" indent="yes" />
    <xsl:param name="keyword" />
    <xsl:param name="type" />

    <xsl:template match="/">
        <p>
        「<xsl:value-of select="$type" />:
        <xsl:value-of select="$keyword" />」の検索結果:
        <xsl:value-of select="count(//item[$keyword != '' and contains(creator, $keyword)])" />件
        </p>

        <xsl:value-of select="my:searchform()" />

        <table class="table table-striped table-hover">
            <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">書名</th>
                    <th scope="col">著者</th>
                </tr>
            </thead>
            <tbody>
                <!-- <xsl:apply-templates
                select="my:partial-match(//item, $type, $keyword)" /> -->
                <xsl:apply-templates
                select="//item[$keyword != '' and contains(creator, $keyword)]" />
            </tbody>
        </table>
    </xsl:template>

    <xsl:template match="item">
        <tr>
            <th scope="row"><xsl:value-of select="@no" /></th>
            <td><a href="detail.cgi?dp={@no}"><xsl:value-of select="title" /></a></td>
            <td><a href="result.cgi?keyword={creator}&amp;type=creator"><xsl:value-of select="creator" /></a></td>
        </tr>
    </xsl:template>
</xsl:stylesheet>