import asyncio
from pycallgraph2 import PyCallGraph
from pycallgraph2.output import GraphvizOutput


async def gen_1():
    for value in range(0, 10):
        await asyncio.sleep(1)  # Could be a slow HTTP request
        yield value

async def gen_2(it):
    async for value in it:
        await asyncio.sleep(1)  # Could be a slow HTTP request
        yield value * 2

async def gen_3(it):
    async for value in it:
        await asyncio.sleep(1)  # Could be a slow HTTP request
        yield value + 3
        
        


async def run():
    file_path = '/'.join([
            'data/output/images',
            '0201_0101_asyncio.png'
        ])
    graphviz = GraphvizOutput()
    graphviz.output_file = file_path
    with PyCallGraph(output=graphviz):
        it_1 = gen_1()
        it_2 = gen_2(it_1)
        it_3 = gen_3(it_2)
        
        async for val in it_3:
            print(val)
        


if __name__ == '__main__':
    asyncio.run(run())
    