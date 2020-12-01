import time


class cache_data:
    def __init__(self, time_to_live, data, address, mail_address, time_of_creation):
        self.time_to_live = time_to_live
        self.data = data
        self.address = address
        self.mail_address = mail_address
        self.time_of_creation = time_of_creation

    def check_time_to_live(self):
        time_lived = time.time() - self.time_of_creation
        return self.time_to_live > time_lived

    def get_dict(self):
        return {'time_of_creation': self.time_of_creation,
                'time_to_live': self.time_to_live,
                'data': self.data,
                'address': self.address,
                'mail_address': self.mail_address
                }
