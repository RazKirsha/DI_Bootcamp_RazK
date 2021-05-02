class Phone:

    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self, other_phone):
        print(f'{other_phone.phone_number} Calls')
        self.call_history.append(other_phone.phone_number)

    def show_call_history(self):
        for call in self.call_history:
            print(call)

    def send_message(self, send_to, got_from, message):
        send_new_message = {
            'to': send_to,
            'from_who': got_from,
            'content': message
        }
        self.messages.append(send_new_message)

    def show_outgoing_messages(self):
        for message in self.messages:
            if message['from_who'] == self.phone_number:
                print(message)

    def show_incoming_messages(self):
        for message in self.messages:
            if message['to'] == self.phone_number:
                print(message)

    def show_messages_from(self, from_number):
        for message in self.messages:
            if message['from_who'] == from_number:
                print(message)


phone1 = Phone(111 - 111 - 111)
phone2 = Phone(222 - 222 - 222)
phone3 = Phone(333 - 333 - 333)
phone4 = Phone(444 - 444 - 444)

phone1.send_message(phone2.phone_number, phone1.phone_number, 'AAA')
phone1.send_message(phone3.phone_number, phone1.phone_number, 'BBB')
phone1.send_message(phone1.phone_number, phone4.phone_number, 'CCC')

phone1.show_incoming_messages()
phone1.show_outgoing_messages()
phone1.show_messages_from(phone2)

