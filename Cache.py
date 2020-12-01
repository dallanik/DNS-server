import pickle
import tempfile
import os
import CacheData


class Cache:
    def __init__(self):
        self.domein_name_data = {}
        self.directory_name = os.path.join(tempfile.gettempdir(), 'path.data.name')

    def create(self):
        self.domein_name_data = self.get_name_data()

    def get_name_data(self):
        if not os.path.exists(self.directory_name):
            return {}
        else:
            with open(self.directory_name, 'rb') as f:
                rawData = f.read()
                if rawData:
                    return pickle.loads(rawData)
            return {}

    def get_data_by_domein_name(self, name):
        data = self.domein_name_data[name]
        return CacheData.cache_data(data['time_to_live'], data['data'], data['address'], data['mail_address'], data['time_of_creation'])

    def add_data_by_domein_name(self, name, data):
        self.domein_name_data[name] = data.get_dict()

    def save(self):
        with open(self.directory_name, 'wb') as f:
            pickle.dump(dict(self.domein_name_data), f)

    def check_and_clean(self):
        for ip, data in self.ip_data:
            if not data.check_time_to_live():
                self.ip_data.pop(ip, None)

    def clear_all(self):
        self.domein_name_data.clear()
        self.save()
