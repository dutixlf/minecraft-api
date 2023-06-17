
# Minecraft API

My first attempt to make a public module.
This project is designed to interact with the minecraft server on a basic level.
## Connection
- The first thing to do is to make sure that rcon is enabled in server.properties

```properties
enable-rcon=true
```

- To connect to the server, use the `minecraft_api.Connect(session)` method

```python
import minecraft_api

mc = minecraft_api.Connect('ruparasha')
```
_* here we connect/create a session. The session is the file where the RCON data is stored_
## Methods

### Default library

##### **Connection**

```python
import minecraft_api

mc = minecraft_api.Connect(session)
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `session` | `string` | **Required**. Session filename |

##### **Send Command**

```python
mc.sendCommand(command)
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `command` | `string` | **Required**. The command you send |

### Message library

##### **Create message**

```python
import minecraft_api.message

message = message_api.message.Message()
```

##### **Run command after click**

```python
message.runCommand(text, command, hover)
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `text` | `string` | **Required**. The text you send |
| `command` | `string` | **Required**. Command executed after clicking |
| `hover` | `string` | Text that is visible on hovering |

##### **Suggest command after click**

```python
message.suggestCommand(text, command, hover)
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `text` | `string` | **Required**. The text you send |
| `command` | `string` | **Required**. Command suggested after clicking |
| `hover` | `string` | Text that is visible on hovering |

##### **Suggest message after click**

```python
message.suggestMessage(text, message, hover)
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `text` | `string` | **Required**. The text you send |
| `message` | `string` | **Required**. Message suggested after clicking |
| `hover` | `string` | Text that is visible on hovering |

##### **Suggest message after click**

```python
message.copyToClipboard(text, clipboard, hover)
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `text` | `string` | **Required**. The text you send |
| `clipboard` | `string` | **Required**. What will be copied after clicking |
| `hover` | `string` | Text that is visible on hovering |

##### **Suggest to open url after click**

```python
message.openUrl(text, url, hover)
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `text` | `string` | **Required**. The text you send |
| `url` | `string` | **Required**. Url will be opened after clicking |
| `hover` | `string` | Text that is visible on hovering |

##### **Default text**

```python
message.default(text, hover)
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `text` | `string` | **Required**. The text you send |
| `hover` | `string` | Text that is visible on hovering |

##### **Send Message**

```python
import minecraft_api as mine
import minecraft_api.message

mc = mine.Connect('ruparasha')
message.sendMessage(mc, players)
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `mc` | `func` | **Required**. Server connection |
| `players` | `list` | Who to send the message to |

### Server library

##### **Get players**

```python
import minecraft_api as mine

mc = mine.Connect('ruparasha')
mc.Server.players()
```

##### **Kick player**

```python
mc.Server.kick(players, reason)
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `players` | `list` | **Required**. Who gets kicked |
| `reason` | `str` | Kick reason |

##### **Ban player**

```python
mc.Server.ban(players, reason)
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `players` | `list` | **Required**. Who gets banned |
| `reason` | `str` | Ban reason |

##### **Ban player**

```python
mc.Server.unban(players)
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `players` | `list` | **Required**. Who gets unbanned |

##### **Return plugins**

```python
mc.Server.Plugins() => {'enabled': [], 'disabled': []}
```

### World library

##### **Set world**

```python
mc.World.setWorld(world='overworld')
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `world` | `str` | Which world to set |

##### **Set block**

```python
mc.World.setBlock(x, y, z, block, data)
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `x` | `int` | X coordinate |
| `y` | `int` | Y coordinate |
| `z` | `int` | Z coordinate |
| `block` | `str` | Blockid _(minecraft:block) / (block)_ |
| `data` | `str` | replace/keep/destroy |

##### **Fill**

```python
mc.World.fill(x1, y1, z1, x2, y2, z2, block, data)
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `x1` | `int` | X1 coordinate |
| `y1` | `int` | Y1 coordinate |
| `z1` | `int` | Z1 coordinate |
| `x2` | `int` | X2 coordinate |
| `y2` | `int` | Y2 coordinate |
| `z2` | `int` | Z2 coordinate |
| `block` | `str` | Blockid _(minecraft:block) / (block)_ |
| `data` | `str` | replace/keep/destroy |

## Authors

- [@dutixlf](https://www.github.com/dutixlf)

