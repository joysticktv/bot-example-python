import re

MAGIC_WORD = 'tacos'
GATEWAY_IDENTIFIER = '{"channel":"GatewayChannel"}'

class Bot:
    @classmethod
    def handle_messages(cls, ws, recieved_message):
        print("\n\nMESSAGE {}".format(recieved_message))

        if recieved_message['type'] == 'ping':
            return
        if 'message' in recieved_message:
            message = recieved_message['message']
            channel_id = recieved_message['channelId']
            if message['type'] == 'new_message':
                if message['text'].lower() == 'hello bot':
                    response = {
                        "command": "message",
                        "identifier": GATEWAY_IDENTIFIER,
                        "data": json.dumps({
                            "action": "send_message",
                            "text": "Hello, @{}!".format(message["author"]["username"]),
                            "channelId": channel_id
                        })
                    }
                    ws.send(json.dumps(response))

                pattern = re.compile(MAGIC_WORD)
                if pattern.match(message['text']):
                    response = {
                        "command": "message",
                        "identifier": GATEWAY_IDENTIFIER,
                        "data": json.dumps({
                            "action": "send_message",
                            "text": "You said @{}'s magic word!".format(message["streamer"]["username"]),
                            "channelId": channel_id
                        })
                    }
                    ws.send(json.dumps(response))
