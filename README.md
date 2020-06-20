# Rolex 프로젝트 소개 _ BackEnd

롤렉스 시계 스토리와 제작과정 및 롤렉스 시계 제품들을 소개하고 원하는 옵션을 선택하여 나만의 롤렉스 시계 설정하기 등을 제공하는 Rolex 클론 프로젝트

<br>

## 개발 인원 및  기간

- 기간 : 10일(4월 23일 ~ 5월 1일)
- Back-end members : [Yeeunlee](https://github.com/yenilee), [Jeonginbak](https://github.com/Jeonginbak), [pyheejin](https://github.com/pyheejin)
- [Front-end GitHub](https://github.com/wecode-bootcamp-korea/Rolex-frontend)

<br>

## 데모 영상 
https://youtu.be/x_35Mi3LWTY
[![Video Label](https://i9.ytimg.com/vi/x_35Mi3LWTY/maxresdefault.jpg?time=1592667196038&sqp=CPjWuPcF&rs=AOn4CLBNZEveqgN9mVF0Cp152u1uTbWTrQ)](https://youtu.be/x_35Mi3LWTY)

<br>

## 목적
- 웹페이지의 구조를 파악하여 모델링
- 모델링을 기반으로 API 생성(model, view, url 작성)
- 팀프로젝트를 통한 프론트엔드와 백엔드간의 의사소통

<br>

## 적용 기술 및 구현 기능


### 적용 기술

- Python
- Django web framework
- Beautifulsoup
- Selenium
- Bcrypt
- Json Web Token
- AWS EC2, RDS
- CORS headers
- Gunicorn

<br>

### DB Modeling
![](https://images.velog.io/images/jeongin/post/42270f13-dc2a-4989-bea1-974b82cabb0b/image.png)


### 구현 기능

#### User
- 회원가입 및 로그인 (Bcrypt 암호화 및 JWT Access Token 전송) 기능 구현
- 회원가입 유효성 검사 기능 구현
- 로그인 검증을 통한 좋아요 기능(클릭/취소/리스트)



#### Product
- DAY-DATE 제품 [시계 골라보기](https://www.rolex.com/ko/watches/find-rolex.html#p=1) List Pagination 
- DAY-DATE 제품 옵션에 따른 중복 필터링 구현 (제품이 없을 시 400 error)
- 시계 이미지 좌측 상단의 하트 클릭 시 나의 셀렉션에서 시계 확인 기능 구현
- 제품 클릭 시 상세 페이지(가격, 설정 조합, 설명글 및 이미지) 라우팅
- DAY-DATE 제품 [시계 설정하기](https://www.rolex.com/ko/watches/configure.html#/day-date/m228238-0042/model): 쿼리스트링으로 단계별 옵션 저장하여 시계 조합 보여주기 기능 구현
- 시계 설정하기의 모든 시계 클릭 시 상세 페이지로 이동할 수 있도록 라우팅 
- 각 단계별 조합 페이지에서 이전 단계로 돌아갔을 때 선택 조합 저장하는 기능 구현



#### 인프라
- Amazon AWS를 통한 배포
- EC2 인스턴스에 RDS서버에 설치된 mysql 연동

<br>

## API documents(POSTMAN)
[회원가입, 로그인, 좋아요](https://interstellar-sunset-788761.postman.co/collections/7338957-fceb2bce-0c66-4d27-82fe-479806136a99?version=latest&workspace=9e529a22-5100-4f53-85c7-608a41491819)

[PRODUCT 상세페이지 및 설정하기](https://interstellar-sunset-788761.postman.co/collections/10871481-cdba486f-5c26-4d62-8e16-d4464932eda3?version=latest&workspace=9e529a22-5100-4f53-85c7-608a41491819)

[DAY-DATE LIST](https://interstellar-sunset-788761.postman.co/collections/10871815-34aa5019-5c1b-4596-9fcf-a17a7bbf6023?version=latest&workspace=9e529a22-5100-4f53-85c7-608a41491819#e1a2af48-fdf1-4e74-8c93-1c5bc30ffa93)
