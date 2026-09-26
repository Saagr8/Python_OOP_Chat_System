class User:
    def __init__(self, username):
        self.username = username
        self.room = None

    def join_room(self, room):
        if self.room is None:
            self.room = room
            room.users.append(self)
            print(self.username, "joined", room.name)
        else:
            print(self.username, "is already in a room.")

    def leave_room(self):
        if self.room is not None:
            print(self.username, "left", self.room.name)
            self.room.users.remove(self)
            self.room = None
        else:
            print(self.username, "is not in a room.")

    def send_message(self, message):
        if self.room is not None:
            self.room.add_message(self.username, message)
        else:
            print(self.username, "is not in a room.")


class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.messages = []

    def add_message(self, username, message):
        self.messages.append(username + ": " + message)
        print(username + ":", message)

    def show_messages(self):
        print("\nChat history:")

        for message in self.messages:
            print(message)


# Create a chat room
room = ChatRoom("Friend_Hub")

# Create users
user1 = User("Sagar")
user2 = User("Asis")

# Users join the room
user1.join_room(room)
user2.join_room(room)

# Users send messages
user1.send_message("Hello, How you doing!")
user2.send_message("Hi Sagar, all good ")

# Show messages
room.show_messages()

# Users leave
user1.leave_room()
user2.leave_room()
