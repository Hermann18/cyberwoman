from random import randint
import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

love = open('base.txt', 'r' ,encoding="utf-8").read().split('/')
vk_session = vk_api.VkApi(token = '#')
longpoll = VkBotLongPoll(vk_session, 201700275)
vk = vk_session.get_api()
while True:
    try:
        for event in longpoll.listen():
             vk.messages.send(
                peer_id = event.message.get('peer_id'),
                random_id = get_random_id(),
                message = love[randint(0, len(love)-1)],
            )
    except Exception as e:
        print(e)
