Important
=========

This app has been discontinued and is no longer maintained.

Django Socketio Messenger
=========================

This is a small Django app that provides API enpoints that can be called to
send socket.io messages.

This approach is probably a bit silly - if we just wanted to forward messages,
we could just as well setup such a server with node.js. But we know Django and
not node.js so this is what got us up to speed the fastest :)

The reason why we need this is because we want to deploy our app on Webfaction.
There we would create a custom app listening to a custom port. This app would
be started via `./manage.py runserver_socketio`.

Our real Django app with all it's admin commands and views etc. would be able
to broadcast messages by sending POST requests to `IP:PORT`, where `IP` is
the IP of the Webfaction server and `PORT` is the port of the custom app.
