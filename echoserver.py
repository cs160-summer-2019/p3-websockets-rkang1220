from websocket_server import WebsocketServer

# define function for new message
def new_msg(client, server, message):
    server.send_message_to_all(message)
# configure server
server = WebsocketServer(3000, host='0.0.0.0')
server.set_fn_message_received(new_msg)
# run server
server.run_forever()
