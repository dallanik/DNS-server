import pickle
import os
import CacheData


class Cache:
    def __init__(self):
        self.domein_name_data = {}

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
        data = self.domein_name_data.get(name)
        return CacheData.cache_data(data['ttl'], data['data'], data['create_time'])

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
