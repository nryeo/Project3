# Project3_Movie Recommendation(localization)</br>for student practice

### Project Background
- 추천시스템 실습으로 TMDB 영화 데이터 주로 이용
- TMDB는 글로벌 사이트로 한국의 실정과 차이 존재
- 예시로, TMDB 랭킹1위는 대부, 네이버 영화 랭킹1위는 탑건:매버릭

### Project Goal
- 한국인들이 평가한 한국 자료로, 국내 현지화된 영화 추천 시스템 개발

### Data
- [네이버 영화](https://movie.naver.com)(2023.03.31부로 운영 종료됨)에서 다음 정보를 BeautifulSoup를 이용, 스크레이핑
  - 평점 기반 랭킹 2000위(네이버에서 제공하는 랭킹 전체)
    - 기본적으로 어느정도 대중적으로 관람되었고, 좋아하는 영화 2000개
    - 각 영화의 제목, 영화코드, 별점 수집
    - 네이버 기준: 각 300개 이상의 평점을 보유한 영화 대상 랭킹 집계한 것
    </br>
  - 개별 페이지(위 영화코드 이용 접속)
    - 영화제목
    - 영화장르
    - 감독
    - 출연(배우)
    - 제작진(감독, 각본)
    - 관람 연령 비율
    
- 데이터 처리
  - 자료 통합
  - 결측치(성인인증이 필요한 영화로 수집이 이루어지지 않음) 행 삭제
  - 차지하는 비율이 가장 높은 관람 연령만 이용
  - 스페이스 삭제
  - 장르, 감독, 배우, 각본 bag of words 생성

### Content-Based Filtering
- 단어 벡터화
  - sklearn의 CountVectorizer 이용
- 단어 유사도
  - sklearn의 cosine_similarity 이용
  - 영화 제목을 입력받으면 가장 유사도가 높은 영화 3개 목록을 반환하는 함수

### pickle
### Streamlit
- 좋아하는 영화를 선택 시 유사한 영화 반환(영화제목, 평점, 장르, 배우, 감독 정보 노출)

### 보완할 점
- 관람 연령 데이터를 뽑았는데, 이용하지 못함
- 사용자 정보_나이를 입력받아 활용하는 방안 모색

---
### Reference 
['나도코딩' youtube (kaggle TMDb 5000 used)](https://www.youtube.com/watch?v=TNcfJHajqJY)
