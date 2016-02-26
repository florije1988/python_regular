# -*- coding: utf-8 -*-
__author__ = 'florije'

import re

pattern = re.compile(r'<HTML>')
res = pattern.match("<HTML>")
print res

pattern = re.compile(r'(this is inside)')
res = pattern.match('this is outside (this is inside)')
print res