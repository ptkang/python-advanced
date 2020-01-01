# python为了将语义变得更加明确，就引入了async和await关键词用于定义原生协程
# async 和 await严格的将协程和生成器区分开来
# await可以将其理解为yield from

# await只能出现async里面
# async里面不能出现yield关键词
# 原生的协程不能使用next()来调用，要使用send()来调用
#

import types

# async def downloader(url):
#     return 'bobby'

@types.coroutine
def downloader(url):
    yield 'bobby'

async def download_url(url):
    # do something
    # yield 1 # SyntaxError: 'return' with value in async generator
    html = await downloader(url)
    return html

if __name__ == '__main__':
    coro = download_url('http://www.imooc.com')
    # next(coro) # TypeError: 'coroutine' object is not an iterator, sys:1: RuntimeWarning: coroutine 'download_url' was never awaited
    coro.send(None)