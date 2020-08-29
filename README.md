# Chat Platform

![](https://github.com/ambujalpha/Chat_platform/blob/master/images/apps.jpg)

# (I) Introduction : 

This is a chatting platform app, basically replicating design of any social media messaging feature. Here one can join 
chatrooms with friends and can keep on chatting. The application is build on Django and with very basic UI and it uses 
websockets to connect and redis server via microsoft, as server is required for chatting application between users.

# (II) Resdis Server : 

Link to download - https://github.com/tporadowski/redis/releases
Further steps is to download and extract the files and paste it's path in path of your system.
Run redis-server.exe while running the app


![](https://github.com/ambujalpha/Chat_platform/blob/master/images/redis.png)

# (III) WebSockets :

WebSocket is a computer communications protocol, providing full-duplex communication channels over a single TCP 
connection. The WebSocket protocol was standardized by the IETF as RFC 6455 in 2011, and the WebSocket API in Web IDL 
is being standardized by the W3C. WebSocket is distinct from HTTP.


![](https://github.com/ambujalpha/Chat_platform/blob/master/images/websocket.png)

# (IV) Website Overview : 

Font-end(User point of view) - One can enter web-app and enter name of the room to chat with other users and can chat.

Back-end(working of webapp) - regardless of mock_app one main was created to handle the chatting part.

Routing: Routing is the process of selecting a path for traffic in a network or between or across multiple networks.
One routing file was created in mock_up app to which will connect with main app.
Routing file in main file is containing a webscoket_pattern to reroute it common room linked with consumers file.

Consumers: Consumers.py file is taking care of connection, disconnection, recieving of chat messages from websockets 
and sending to chat room and vice versa. 

# (V) Conclusions :

We were able to produce results which are consistent with the methodology proposed. Mainy the
focus was to integrate the machine learning algorithms with our website for the completion of this
project. This provides a powerful tool in the hands of a layman to observe predicted stocks and
invest accordingly. A user friendly terminal which shows when to invest and when to divest gives a
sense of trust to these predicted values. It is important to note that the results produced are likely to
be the trend in the next 20 days. That explains that in between this time period there might be days
which are not in resonance with the result but the end result is surely accurate to predict the trend.




