import os
import json
import time
# import tqdm
# from unittest.mock import right

import requests
import pandas as pd
from datetime import datetime, timedelta
from urllib.parse import quote_plus, urlencode

def request_weather_api(output_dir, stn_Ids, year, yesterday):
    url = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'
    servicekey = os.environ['WEATHER_API_KEY']

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64)'
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132'
                             'Safari/537.36'}

    params = f'?{quote_plus("ServiceKey")}={servicekey}&' + urlencode({
        quote_plus("pageNo"): "1",  # 페이지 번호 // default : 1
        quote_plus("numOfRows"): "720",  # 한 페이지 결과 수 // default : 10
        quote_plus("dataType"): "JSON",  # 응답자료형식 : XML, JSON
        quote_plus("dataCd"): "ASOS",
        quote_plus("dateCd"): "DAY",
        quote_plus("startDt"): f'{year}0101',
        quote_plus("endDt"): yesterday,
        quote_plus("stnIds"): f"{stn_Ids}"
    })

    output_path = os.path.join(output_dir, f'{year}.csv')

    try:
        result = requests.get(url + params, headers=headers)
    except:
        time.sleep(3)
        result = requests.get(url + params, headers=headers)

    try:
        js = json.loads(result.content)
        df = pd.DataFrame(js['response']['body']['items']['item'])
        df.to_csv(output_path, index=False)

        return df
    except:
        pass

    time.sleep(2)


def main():
    info_data = pd.read_csv("./input/관측지점코드.csv")
    yesterday = (datetime.now() - timedelta(days=1))


    for idx, row in info_data.iterrows():
        code = row['지점']
        output_dir = f"./weather_data/{code}"
        os.makedirs(output_dir, exist_ok=True)
        request_weather_api(output_dir, code, yesterday.year, yesterday.strftime('%Y%m%d'))


if __name__ == '__main__':
    main()
