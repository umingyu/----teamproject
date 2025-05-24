from tkinter import *
from tkinter.simpledialog import *


def get_input():
    
    window = Tk()
    window.geometry("700x500")

    label1 = Label(window, text="")
    label1.pack()

    value1 = askstring("미세먼지 ","지금 위치하고계신 지역을 적으세용(예: 서울, 부산 등)")


    window.destroy()
    return value1

import requests
a = get_input()
def to_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None

def main():
    url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"

    params = {
        "sidoName": a,      # 지역 설정
        "pageNo": 1,
        "numOfRows": 100,
        "returnType": "json",    # JSON 형식 응답
        "serviceKey": "zt9i5U0hGr7/9nnYt96iOLIs/aoC68ZzkTzY0l9Ru3kFftxLjWOkT7I+fyU1diEqPrqg/tAxhslC99LcvOyWkQ==",  # 실제 서비스 키로 대체하세요.
        "ver": "1.0"
    }
    
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()

        # JSON 구조에 따라 items 리스트에 접근 (예: data["response"]["body"]["items"])
        items = data.get("response", {}).get("body", {}).get("items", [])
        if not items:
            print("API 응답에 데이터가 없습니다.")
            return

        # 합계 및 카운트를 저장할 변수 초기화
        sum_pm10 = 0.0
        count_pm10 = 0

        sum_pm10_24 = 0.0
        count_pm10_24 = 0

        sum_pm25 = 0.0
        count_pm25 = 0

        sum_pm25_24 = 0.0
        count_pm25_24 = 0

        for item in items:
            # pm10Value
            pm10_val = to_float(item.get("pm10Value"))
            if pm10_val is not None:
                sum_pm10 += pm10_val
                count_pm10 += 1

            # pm10Value24
            pm10_24 = to_float(item.get("pm10Value24"))
            if pm10_24 is not None:
                sum_pm10_24 += pm10_24
                count_pm10_24 += 1

            # pm25Value
            pm25_val = to_float(item.get("pm25Value"))
            if pm25_val is not None:
                sum_pm25 += pm25_val
                count_pm25 += 1

            # pm25Value24
            pm25_24 = to_float(item.get("pm25Value24"))
            if pm25_24 is not None:
                sum_pm25_24 += pm25_24
                count_pm25_24 += 1

        # 평균 계산 (유효한 값이 있을 때만)
        avg_pm10 = sum_pm10 / count_pm10 if count_pm10 > 0 else None
        avg_pm10_24 = sum_pm10_24 / count_pm10_24 if count_pm10_24 > 0 else None
        avg_pm25 = sum_pm25 / count_pm25 if count_pm25 > 0 else None
        avg_pm25_24 = sum_pm25_24 / count_pm25_24 if count_pm25_24 > 0 else None

        if 0<avg_pm10<30:
            print("오늘의",a,"의 미세먼지 농도는 좋음입니다.")
        elif 30<avg_pm10<80:
            print("오늘의",a,"의 미세먼지 농도는 보통입니다.")
        elif 80<avg_pm10<150:
            print("오늘의",a,"의 미세먼지 농도는 나쁨입니다.")
        elif 150<avg_pm10:
            print("오늘의",a,"의 미세먼지 농도는 매우 나쁨입니다.") 
        
        if 0<avg_pm25<15:
            print("오늘의",a,"의 초미세먼지 농도는 좋음입니다.")
        elif 15<avg_pm25<35:    
            print("오늘의",a,"의 초미세먼지 농도는 보통입니다.")
        elif 35<avg_pm25<75:
            print("오늘의",a,"의 초미세먼지 농도는 나쁨입니다.")
        elif 75<avg_pm25:
            print("오늘의",a,"의 초미세먼지 농도는 매우 나쁨입니다.")
    else:
        print(f"API 요청 실패 (상태 코드: {response.status_code})")

if __name__ == "__main__":
    main()  


