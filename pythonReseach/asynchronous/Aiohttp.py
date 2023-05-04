import asyncio
import aiohttp

loop = asyncio.get_event_loop()

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://httpbin.org/get') as resp:
            print(await resp.status_code)
            print(await resp.text())
            print(await resp.read()) # access response body as bytes


# Passing Parameters In URLs
# params = {'key1': 'value1', 'key2': 'value2'}
# async with session.get('http://httpbin.org/get',
#                        params=params) as resp:
#     expect = 'http://httpbin.org/get?key1=value1&key2=value2'
#     assert str(resp.url) == expect



# other http methods available
# session.delete('http://httpbin.org/delete')
# session.head('http://httpbin.org/get')
# session.options('http://httpbin.org/get')
# session.patch('http://httpbin.org/patch', data=b'data')

# Typically, you want to send some form-encoded data – much like an HTML form. To do this, simply pass a dictionary to the data argument.
# payload = {'key1': 'value1', 'key2': 'value2'}
# async with session.post('http://httpbin.org/post',
#                         data=payload) as resp:
#     print(await resp.text())

# if you want to use JSON data
# async with session.post(url, json={'example': 'test'}) as resp:
#     ...


loop.run_until_complete(main)