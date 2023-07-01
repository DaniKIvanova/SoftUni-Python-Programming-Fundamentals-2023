class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []

line = input()
while line != "Stop":
    sender, receiver, content = line.split(" ")
    email = Email(sender, receiver, content)
    emails.append(email)
    line = input()

send_emails = [int(el) for el in input().split(", ")]

for x, email in enumerate(emails):
    if x in send_emails:
        emails[x].send()
    print(f"{email.sender} says to {email.receiver}: {email.content}. Sent: {email.is_sent}")
