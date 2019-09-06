from telethon import TelegramClient, sync
from settings import API_HASH, API_ID
from telethon import TelegramClient, events
import asyncio

client = TelegramClient('session_name', API_ID, API_HASH)

@client.on(events.NewMessage(chats=('saleshero')))
async def normal_handler(event):
#    print(event.message)
    print(event.message.to_dict())
    #await client.send_message('BotZdimon77', 'Hello! Talking to you from Telethon')


client.start()
client.run_until_disconnected()

for dialog in client.iter_dialogs():
    if(dialog.title=='Sales Hero'):
        print(dialog)
        print(dialog.id)



'''
#print(client.get_me().stringify())
#for dialog in client.iter_dialogs():
#    print(dialog.title)

async def main():
    await client.start()

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

'''