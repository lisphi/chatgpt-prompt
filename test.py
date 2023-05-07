import sys
import time


content_format2 = """Summarize the highlights of the content which is delimited with triple backticks, 
generate a mind map, and output it in Markdown format, and the output language is {lang}. 
Content: ```{content}```"""


print(content_format2.format(content="aaa", lang="zh-CN"))