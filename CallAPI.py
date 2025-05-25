import requests
import UI

a = UI.get_input()  # UI 모듈에서 사용자 입력 받기
c = 0 
b = 0
def to_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None

def main():
    global  c, b
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
             c = 1
        elif 30<avg_pm10<80:
             c = 2
        elif 80<avg_pm10<150:
             c = 3
        elif 150<avg_pm10:
             c = 4
        
        if 0<avg_pm25<15:
             b = 1
        elif 15<avg_pm25<35:    
             b = 2
        elif 35<avg_pm25<75:
             b = 3
        elif 75<avg_pm25:
             b = 4
    else:
        print(f"API 요청 실패 (상태 코드: {response.status_code})")
    
    return c, b

