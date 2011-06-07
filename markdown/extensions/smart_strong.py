'''
Smart_Strong Extension for Python-Markdown
==========================================

This extention as a smarter handleing of double underscores within words.

Simple Usage:

    >>> import markdown
    >>> markdown.markdown('Text with double__underscore__words.', \
                          extensions=['smart_strong'])
    u'<p>Text with double__underscore__words.</p>'
    >>> markdown.markdown('__Strong__ still works.', \
                          extensions=['smart_strong'])
    u'<p><strong>Strong</strong> still works.</p>'
    >>> markdown.markdown('__this__works__too__.', \
                          extensions=['smart_strong'])
    u'<p><strong>this__works__too</strong>.</p>'

Copyright 2011
[Waylan Limberg](http://achinghead.com)

'''

import re
import markdown
from markdown.inlinepatterns import SimpleTagPattern

SMART_STRONG_RE = r'(?<!\w)(_{2})(?!_)(.+?)(?<!_)\2(?!\w)'
STRONG_RE = r'(\*{2})(.+?)\2'

class SmartEmphasisExtension(markdown.extensions.Extension):
    """ Add smart_emphasis extension to Markdown class."""

    def extendMarkdown(self, md, md_globals):
        """ Modify inline patterns. """
        md.inlinePatterns['strong'] = SimpleTagPattern(STRONG_RE, 'strong')
        md.inlinePatterns['strong2'] = SimpleTagPattern(SMART_STRONG_RE, 'strong')

def makeExtension(configs={}):
    return SmartEmphasisExtension(configs=dict(configs))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
