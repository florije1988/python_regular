# -*- coding: utf-8 -*-
__author__ = 'florije'

import re

# pattern = re.compile(r'<HTML>')
# res = pattern.match("<HTML>")
# print res
#
# pattern = re.compile(r'(this is inside)')
# res = pattern.match('this is outside (this is inside)')
# print res

# pattern = re.compile(r'hello')
# m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
#
# print "m.string:", m.string
# print "m.re:", m.re
# print "m.pos:", m.pos
# print "m.endpos:", m.endpos
# print "m.lastindex:", m.lastindex
# print "m.lastgroup:", m.lastgroup
#
# print "m.group(1,2):", m.group(1, 2)
# print "m.groups():", m.groups()
# print "m.groupdict():", m.groupdict()
# print "m.start(2):", m.start(2)
# print "m.end(2):", m.end(2)
# print "m.span(2):", m.span(2)
# print r"m.expand(r'\2 \1\3'):", m.expand(r'\2 \1\3')

# import re
#
# # 将正则表达式编译成Pattern对象
# pattern = re.compile(r'world')
# # 使用search()查找匹配的子串，不存在能匹配的子串时将返回None
# # 这个例子中使用match()无法成功匹配
# match = re.match(pattern,'hello world!')
# if match:
#     # 使用Match获得分组信息
#     print match.group()
# ### 输出 ###
# # world

# pattern = re.compile(r'\d+')
# print re.split(pattern,'one1two2three3four4')
#
# pattern = re.compile(r'\d+')
# print re.findall(pattern,'one1two2three3four4')
#
# pattern = re.compile(r'\d+')
# for m in re.finditer(pattern,'one1two2three3four4'):
#     print m.group(),


# pattern = re.compile(r'(\w+) (\w+)')
# s = 'i say, hello world!'
#
# print re.sub(pattern,r'\2 \1', s)
#
# def func(m):
#     return m.group(1).title() + ' ' + m.group(2).title()
#
# print re.sub(pattern,func, s)


# pattern = re.compile(r'(\w+) (\w+)')
# s = 'i say, hello world!'
#
# print re.subn(pattern,r'\2 \1', s)
#
# def func(m):
#     return m.group(1).title() + ' ' + m.group(2).title()
#
# print re.subn(pattern,func, s)


# str = 'an example word:cat!!'
# match = re.search(r'\^word', str)  # \w\w\w
# # If-statement after search() tests if it succeeded
# if match:
#     print 'found', match.group() ## 'found word:cat'
# else:
#     print 'did not find'
#
# match = re.search(r'^pii', 'piigpii')
# print match.group()

# pattern = re.compile(r'\w[tr]{2,}ing')
# match = re.search(pattern, 'T_&&his is b a string.&&#')
# if match:
#     print match.group()
# else:
#     print 'Not matched.'
#
# match = re.search(r'pi?g', 'piiiigpigpg')
# print match.group()
#
# string = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
# res = re.findall(r'[\w.-]+@[\w]+\.[\w]+', string)
# for item in res:
#     print item


# match = re.search(r'f[a|b]+b+', 'sdfaabnbd')
# if match:
#     print match.group()

match = re.search(r'([1-9])(\d{2})-(\d{4})', 'Doe, John: 555-1212')
if match:
    print match.group(0)

contactInfo = 'Doe, John: 555-1212'
match = re.search(r'(?P<last>\w+), (?P<first>\w+): (?P<phone>\S+)', contactInfo)
if match:
    print match.groups()
    print match.group(), match.group('last'), match.group('first'), match.group('phone')

res = re.findall(r'[1-9]\d{2}-\d{4}', 'Doe, John: 555-1212, 342-1234')
if res:
    print res

res = re.findall(ur'\d+', 'one12two23three3four4')
print res

res = re.findall(r'\b\w{5}\b', 'Once you have accomplished small things, you may attempt great ones safely.')
print res

person = re.findall(ur"\[P\] (.+?) \[/P\]+?", "President [P] Barack Obama [/P] met Microsoft founder [P] Bill Gates [/P], yesterday.")
print person
