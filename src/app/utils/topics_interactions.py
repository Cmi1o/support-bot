import aiohttp

from aiohttp import ClientResponse


async def create_topic(bot_token: str, forum_id: int | str, name: str) -> ClientResponse:
    '''Create new topic in the forum
    
    Parameters
    ----------
    forum_id : int | str
        id of the forum main chat. id < 0
    name : str
        name of the topic
    
    Returns
    -------
    ClientResponse
        ClientResponse object of the created topic
    '''
    async with aiohttp.ClientSession() as session:
        response = await session.post(
            url=f'https://api.telegram.org/bot{bot_token}/createForumTopic',
            json={
                'chat_id': forum_id,
                'name': name
            }
        )
        return response


async def delete_topic(
    bot_token: str, 
    forum_id: int | str, 
    message_thread_id: int
) -> aiohttp.ClientResponse:
    async with aiohttp.ClientSession() as session:
        return await session.post(
            url=f'https://api.telegram.org/bot{bot_token}/deleteForumTopic',
            json={
                'chat_id': forum_id,
                'message_thread_id': message_thread_id
            }
        )
