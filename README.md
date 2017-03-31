How to run : 
1. virtualenv env
2. . env/bin/activate
3. sudo pip install -r requirements.txt
4. cd twisted-websocket
5. python setup.py install
6. python manage.py runserver &
7. twistd -n -y chatserver.py (in a new Terminal)

To Use :
1. Go to http://127.0.0.1:8000/chats/ you can see the chat rooms
2. Go to http://127.0.0.1:8000/admin/ you can manage the chatrooms and user. 

