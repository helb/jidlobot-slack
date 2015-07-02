Plugin for [python-rtmbot](https://github.com/slackhq/python-rtmbot) – get lunch menus sent into channel daily.

## Installation

Create environment:

```
$ virtualenv -p `which python2` jidlobot
$ cd jidlobot
$ source bin/activate
```

Install rtmbot:

```
$ git clone git@github.com:slackhq/python-rtmbot.git
$ cd python-rtmbot
$ pip install -r requirements.txt
```

Install plugin:

```
$ cd plugins
$ git clone git@github.com:helb/jidlobot.git
$ cd jidlobot
$ pip install -r requirements.txt
```

Edit `jidlobot.conf` file and set `CHANNEL` and `TIME`. Channel IDs can be found at `https://slack.com/api/channels.list?token=…`.

Configure rtmbot:

```
$ cd ../..
$ cp doc/example-config/rtmbot.conf .
```

Edit `rtmbot.conf` and set `SLACK_TOKEN`.

Run the bot:

```
$ ./rtmbot.py
```


## TODO

 - support for multiple channels
 - more pubs
