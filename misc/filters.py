from pyrogram import filters
from pyrogram.types import Message


def in_message(text: str):
    async def filter(flt, _, message: Message):
        if message.text is None:
            return False
        return flt.text in message.text
    return filters.create(filter, text=text)


def startswith(target: str):
    async def filter(flt, _, message: Message):
        if message.text is None:
            return False
        return message.text.startswith(flt.target)
    return filters.create(filter, target=target)


