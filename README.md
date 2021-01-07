# bot_for_crypto
This is a Telegram Bot for Crypto Exchange ... 

## How to use ?

First, Generate Flask SECRET_KEY 

```
# ==== generate SECRET_KEY ====
# $ flask shell
# >>> import os
# >>> import base64
# >>> a = os.urandom(24)
# >>> base64.b64encode(a)
```

Create ```app/config.py```

```
import os

class Config:
    DEBUG = False
    TESTING = False
    JSON_AS_ASCII = False
    SECRET_KEY = 'This is a Key HAHA'
    ExchangeName_API_KEY = "This is ExchangeName_API_KEY"
    ExchangeName_SECRET_KEY = "This is ExchangeName_SECRET_KEY"
    BOT_API_KEY = "This is Telegram Bot API_KEY"


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'pro': ProductionConfig,
    'dev': DevelopmentConfig,
}
```