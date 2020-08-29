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
Channel layers were mentioned in settings.py for it and port was also defined.


![](https://github.com/ambujalpha/Chat_platform/blob/master/images/redis.png)

# (III) WebSockets :

WebSocket is a computer communications protocol, providing full-duplex communication channels over a single TCP 
connection. The WebSocket protocol was standardized by the IETF as RFC 6455 in 2011, and the WebSocket API in Web IDL 
is being standardized by the W3C. WebSocket is distinct from HTTP.


![](https://github.com/ambujalpha/Chat_platform/blob/master/images/websocket.png)

# (IV) Website Overview : 

Font-end(User point of view):  One can enter web-app and enter name of the room to chat with other users and can chat.
2 html pages were design with scripting for working of chatting application, it also contained JS and have query handling capacity.

Back-end(working of webapp):  regardless of mock_app one main was created to handle the chatting part.

Routing:  Routing is the process of selecting a path for traffic in a network or between or across multiple networks.
One routing file was created in mock_up app to which will connect with main app.
Routing file in main file is containing a webscoket_pattern to reroute it common room linked with consumers file.

Consumers:  Consumers.py file is taking care of connection, disconnection, recieving of chat messages from websockets 
and sending to chat room and vice versa. 

ASGI:  ASGI, or the Asynchronous Server Gateway Interface, is the specification which Channels and Daphne are 
built upon, designed to untie Channels apps from a specific application server and provide a common way to write 
application and middleware code.

WSGI:  Django's primary deployment platform is WSGI, the Python standard for web servers and applications. 
Django's startproject management command sets up a minimal default WSGI configuration for us and it's enough here 
for this level implementation.


![](https://github.com/ambujalpha/Chat_platform/blob/master/images/webapp1.png)

![](https://github.com/ambujalpha/Chat_platform/blob/master/images/webapp2.png)

# (V) Conclusions :

So here, basic design was implemented which can be later upgraded with databases as storage for chats and users, friends list.
It can be furnished to inbox chat as well as group chat with various multiple features.




