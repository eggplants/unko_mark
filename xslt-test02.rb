require 'cgi'
require 'xslt'

cgi = CGI.new

puts cgi.header("text/html; charset=UTF-8"), ->(xsl, xml){
LibXSLT::XSLT::Stylesheet.new(
    LibXML::XML::Document.file(xsl)
).apply(
    XML::Document.file(xml)
)
}.call($*[0], $*[1])