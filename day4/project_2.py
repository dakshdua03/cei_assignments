import requests
import pandas as pd
import json
from datetime import date, timedelta

# headers = {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate, br, zstd",
#     "Accept-Language": "en-US,en;q=0.5",
#     "Connection": "keep-alive",
#     "Cookie": "_ga_2RYZG7Y4NC=GS1.1.1720781374.2.1.1720781401.0.0.0; _ga=GA1.1.1293574285.1720725767; __gads=ID=431183c1bf976469:T=1720725771:RT=1720781377:S=ALNI_MaJY6KpsIuUFKNtOz1ZCtpkSxbr0Q; __gpi=UID=00000e8da5f09e0f:T=1720725771:RT=1720781377:S=ALNI_MYTU3WK-zKVX806cO9rZ1-R0jgjPA; __eoi=ID=19bb55a6aae93306:T=1720725771:RT=1720781377:S=AA-AfjYYi3ingEvf9nqNyDhgd6Qo; JSESSIONID=566DC7F732A3152C708BBAF6B1510C31; FCNEC=%5B%5B%22AKsRol-EB0qmR7T9dSLatMxOsnzdpOqzAr35ScMIZOzL0sndv7MPKmEgviLEJRYe83JvdG71ZQO6pb_fz0BajtmxjBKn272cIE0Ro1UC3rzWY8QvOzFpPo8xYYEpsK47xOIs0WcPEhoAuy_9PzKhZa9Pmrx9z09dbA%3D%3D%22%5D%5D",
#     "Host": "vegetablemarketprice.com",
#     "Priority": "u=0",
#     "Referer": "https://vegetablemarketprice.com/market/uttarpradesh/today",
#     "Sec-Fetch-Dest": "empty",
#     "Sec-Fetch-Mode": "cors",
#     "Sec-Fetch-Site": "same-origin",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0"
# }

url_template = "https://vegetablemarketprice.com/api/dataapi/market/uttarpradesh/daywisedata?date={date}"


start_date = date(2024, 5, 1)
end_date = date(2024, 6, 30)

data = []

current_date = start_date
while current_date <= end_date:

    formatted_date = current_date.strftime('%Y-%m-%d')
    url = url_template.format(date=formatted_date)

    response = requests.get(url)
    js_data = json.loads(response.text)

    for vegetable in js_data['data']:

        dict_veg = {}

        dict_veg['date'] = formatted_date
        dict_veg['state'] = 'Uttar Pradesh' 
        dict_veg['name'] = vegetable['vegetablename']
        dict_veg['wholesalePrice'] = vegetable['price'] #-> 'wholesale price'
        dict_veg['retailPrice'] = vegetable['retailprice']
        dict_veg['shoppingmallPrice'] = vegetable['shopingmallprice']
        dict_veg['units'] = vegetable['units']
        dict_veg['image'] = vegetable['table']['table_image_url']

        # print(dict_veg)
        data.append(dict_veg)
        print(f"Data fetched successfully for the date {formatted_date}")

    current_date += timedelta(days=1)

# start_date = date(2024, 5, 1)
# end_date = date(2024, 6, 30)

# current_date = start_date
# while current_date <= end_date:
#     print(current_date)
#     current_date += timedelta(days=1)

# print(data)
# print(response)

df = pd.DataFrame(data)
df.to_csv('extracted_data.csv')
print("Data Extracted Successfully")

