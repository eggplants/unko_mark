<?xml version="1.0" encoding="UTF-8" ?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <xsl:output method="text" encoding="utf-8" />
    <xsl:template match="/">
        <xsl:text>タイトル&#x9;著者&#x9;出版社&#x9;価格&#x9;出版年月日&#xa;</xsl:text>
        <xsl:apply-templates select="//item" />
    </xsl:template>

    <xsl:template match="item">
        <xsl:value-of select="normalize-space(title)" />
        <xsl:text>&#x9;</xsl:text>
        <xsl:value-of select="normalize-space(creator)" />
        <xsl:text>&#x9;</xsl:text>
        <xsl:choose>
            <xsl:when test="publisher[not(node())]">
                <xsl:text>NoData</xsl:text>
            </xsl:when>
            <xsl:otherwise>
                <xsl:value-of select="normalize-space(publisher)" />
            </xsl:otherwise>
        </xsl:choose>
        <xsl:text>&#x9;</xsl:text>
        <xsl:value-of select="price" />
        <xsl:text>&#x9;</xsl:text>
        <xsl:value-of select="concat(date/year,'-',
                                    format-number(date/month, '00'),'-',
                                    format-number(date/day, '00'))" />
        <xsl:text>&#xa;</xsl:text>
    </xsl:template>
</xsl:stylesheet>