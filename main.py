from concurrent.futures import ThreadPoolExecutor
import csv
from functions import push_config

csv_datas = []
with open('devices.csv') as csvfile:
    datas = csv.reader(csvfile, delimiter=';')
    for row in datas:
        csv_datas.append(row)

#loop without concurrency
# for csv_data in csv_datas:
#     print(push_config(csv_data))

#loop with concurrency
results = []
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(push_config, csv_data) for csv_data in csv_datas]
    print(futures)
    for future in futures:
        try:
            results.append(future.result())
        except TypeError as e:
            print (e)
print(results)
write_result = open('result.csv','w')
write_result.write('hostname,')
write_result.write('ip,')
write_result.write('status\n')
for result in results:
    write_result.write(str(result["devicename"])+',')
    write_result.write(str(result["ip"])+',')
    write_result.write(str(result["status"]))
    write_result.write('\n')
write_result.close()