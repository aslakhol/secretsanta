import uuid


class Santa:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.id = uuid.uuid4()

    def describe(self):
        return '{}: {} has this email: {}'.format(self.id, self.name, self.email)

    def get_id(self):
        return self.id

    def set_receiver(self, receiver_id):
        self.receiver = receiver_id

    def get_receiver(self):
        return self.receiver

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email
