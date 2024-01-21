# 기상청_지상(종관, ASOS) 일자료 조회서비스 수집 자동화

----

GitHub Action을 사용하여 [기상청_지상(종관, ASOS) 일자료 조회서비스 API](https://www.data.go.kr/data/15059093/openapi.do) 데이터 수집 자동화
- 기상대가 설치되어 있는 지점의 종관기상관측일자료 데이터 수집
- 해당 지역과 지점코드는 [관측지점코드](./input/관측지점코드.csv) 또는 공공데이터포털의 활용가이드 참고
- ```지점코드```를 디렉토리명으로 수집

아래와 같은 형식을 맞추어 csv 파일 형태로 사용할 수 있음

```https://raw.githubusercontent.com/jungjae0/Data-Weather/main/weather/{지점코드}/{연도}/{월}.csv```


----

| 항목명(영문)  | 항목명(국문) | 샘플데이터 | 항목설명         |
|----------|---------|-------|--------------|
| year     | 연도      | 1973  |              |
| month    | 월       | 1     |              |
| day      | 일       | 1     |              |
| tavg     | 일평균기온   | -7.6  | 평균 기온(°C)    |
| tmin     | 일최저기온   | -12.7 | 최저 기온(°C)    |
| tmax     | 일최고기온   | -3.6  | 최고 기온(°C)    |
| rain     | 일강수량    | 0     | 일강수량(mm)     |
| sunshine | 합계일조시간  | 7.3   | 합계 일조 시간(hr) |
| snow     | 일 최심신적설        | 25.8  | 일 최심신적설(cm)  |

일 최심신적설: 전에 내렸던 눈은 제거하고, 고려하고 있는 기간 동안, 새롭게 쌓인 눈이 가장 두껍게 쌓여 있을 때의 눈의 두께(깊이).

