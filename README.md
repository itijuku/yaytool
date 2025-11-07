# A simple document
## import
```python
import yaytool as yt
```

## createBot
```python
bot = yt.Login("yourMailAddress","yourPassword")
```

## methods
```python
bot.follow("userId")
bot.unfollow("userId")
bot.like("postId")
bot.post("text")
bot.repost("text")
bot.gettimeline(numbers:int=100)
bot.block(userId)
bot.unblock(userId)

etc.
```
