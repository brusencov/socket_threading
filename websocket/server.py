from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

clients = []


class Chat(WebSocket):

    def handleMessage(self):
        for client in clients:
            if client != self:
                client.sendMessage(self.data)

    def handleConnected(self):
        print(self.address, 'connected')
        for client in clients:
            client.sendMessage(self.address[0] + u' - connected')
        clients.append(self)

    def handleClose(self):
        clients.remove(self)
        print(self.address, 'closed')
        for client in clients:
            client.sendMessage(self.address[0] + u' - disconnected')


server = SimpleWebSocketServer('localhost', 8001, Chat)
server.serveforever()
