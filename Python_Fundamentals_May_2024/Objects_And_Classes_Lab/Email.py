class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
indices_got = []
while True:
    command = input().split()
    if command[0] == 'Stop':
        break
    sender, receiver, content = command
    current_email = Email(sender, receiver, content)
    emails.append(current_email)

indices = list(map(int, input().split(", ")))
for index in indices:
    emails[index].send()

for el in emails:
    print(el.get_info())
