import socket
import os
import subprocess
import CacheData as C_Data
import Cache
import time

IP = 'localhost'
PORT = 53

if __name__ == "__main__":
    os.popen("chcp 65001")
    cache = Cache.Cache()
    cache.create()
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((IP, PORT))
        print("Server is running...")
        while True:
            try:
                conn, addr = s.recvfrom(1024)
            except Exception:
                continue
            request = bytes.decode(conn)
            if request in cache.domein_name_data.keys():
                data = cache.get_data_by_domein_name(request)
                answer = data.data
            else:
                try:
                    process = subprocess.Popen(["nslookup", "-query=SOA", request], stdout=subprocess.PIPE)
                    answer = process.communicate()[0]
                except Exception:
                    s.sendto(answer, addr)
                    continue
                output = str(answer).split('\\r\\n')
                ttl = 0
                for i in output:    
                    if "ttl" in i.lower():
                        ttl = i.split('=')[1].split(' ')[1]
                data = C_Data.cache_data(ttl, answer, time.time())
                if ttl != 0:
                    cache.add_data_by_domein_name(request, data)
                    cache.save()
            s.sendto(answer.decode().encode(), addr)


