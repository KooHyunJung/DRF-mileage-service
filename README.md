# DRF-mileage-service
## 프로젝트 환경
- Mac(M1)
- Pycham(IDE)
- DRF(Django REST Framework) 3.13.1
- poetry(Dependency Manager)
- python 3.9
- MySQL 8.0.25

## DB 설계
![스크린샷 2022-06-27 오후 9 02 09](https://user-images.githubusercontent.com/96563289/176197986-b59a6ecf-db21-446a-a66a-29affa255439.png)

user 모델 따로 생성하지 않고 진행
- `Event` : post/events 저장 테이블. even 모든 내역(생성, 수정, 삭제) 저장
- `Place` : 장소 정보 테이블
- `PlaceHistory` : `Place` 1 : 1 장소 리뷰 count -> 처음 리뷰 작성인지 아닌지 판별
- `Review` : Event 내용 정규화 + 최신 상태 반영 테이블
- `Point` : user에 해당하는 총 point 조회 가능 테이블
- `PointHistory` : Review, Point 1 : N 연결, 리뷰에 대한 point 정보

##  API


![스크린샷 2022-06-28 오후 11 30 30](https://user-images.githubusercontent.com/96563289/176206858-18eb9265-64af-4685-a391-654ba0910334.png)
