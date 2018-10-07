'''
    #### Unicode Database in Python ###
    -Unicode Character Database (UCD) is defined by Unicode Standard Annex #44 which defines
    -the character properties for all unicode characters.
    -This module provides access to UCD and uses the same symbols
    -and names as defined by the Unicode Character Database.

    ## Function
        1-unicodedata.lookup(name)
        2-unicodedata.name(chr[, default])
        3-unicodedata.decimal(chr[, default])
        4-unicodedata.digit(chr[, default])
        5-unicodedata.numeric(chr[, default])
        6-unicodedata.category(chr)
        7-unicodedata.bidirectional(chr)
        8-unicodedata.normalize(form, unistr)
'''
import unicodedata

print (unicodedata.lookup('LEFT CURLY BRACKET'))
print (unicodedata.lookup('RIGHT CURLY BRACKET'))
print (unicodedata.lookup('ASTERISK'))
#############################
print (unicodedata.name(u'/'))
print (unicodedata.name(u'|'))
print (unicodedata.name(u':'))
################################
print (unicodedata.decimal(u'9'))
print (unicodedata.decimal(u'5'))
####################################
print (unicodedata.decimal(u'0'))
print (unicodedata.decimal(u'1'))
###################################
print(unicodedata.category(u'A'))
print(unicodedata.category(u'b'))
###################################
print(unicodedata.bidirectional(u'\u0660'))
