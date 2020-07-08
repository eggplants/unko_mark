require 'xslt'
# $ gem install libxslt-ruby

puts->(xsl, xml){
LibXSLT::XSLT::Stylesheet.new(
    LibXML::XML::Document.file(xsl)
).apply(
    XML::Document.file(xml)
)
}.call($*[0], $*[1])