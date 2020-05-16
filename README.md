# Rolex 프로젝트 소개 _ BackEnd

롤렉스 시계 스토리와 제작과정 및 롤렉스 시계 제품들을 소개하고 원하는 옵션을 선택하여 나만의 롤렉스 시계 설정하기 등을 제공하는 Rolex 클론 프로젝트

<br>

## 개발 인원 및  기간

- 기간 : 10일
- 인원 : 프론트엔드 3명, 벡엔드 3명
- [프론트엔드 GitHub](https://github.com/wecode-bootcamp-korea/Rolex-frontend)

<br>

## 목적
- 웹페이지의 구조를 파악하여 modeling 구현
- modeling을 통해 model 및 view 코딩
- 팀프로젝트를 통한 프론트엔드와 백엔드간의 의사소통

<br>

## 적용 기술 및 구현 기능

<br>

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

<br>

### 구현 기능

#### User
- 회원가입 및 로그인 기능 구현
  (Bcrypt 암호화 및 JWT Access Token 사용)
- 회원가입 유효성 검사 기능 구현
- 좋아요 클릭으로 마이페이지에서 내가 선택한 시계 보기 구현

<br>

#### Product
- 롤렉스 컬렉션 상품 상세 페이지 메뉴 목록 구현
- 상품 전체리스트 옵션에 따른 필터 구현
- 상품 옵션에 선택에 따른 롤렉스 시계 제품 구현

<br>

#### 인프라
- Amazon AWS를 통한 배포
- EC2 인스턴스에 RDS서버에 설치된 mysql 연동

<br>

## API documents(POSTMAN)
[회원가입, 로그인, 좋아요](https://interstellar-sunset-788761.postman.co/collections/7338957-fceb2bce-0c66-4d27-82fe-479806136a99?version=latest&workspace=9e529a22-5100-4f53-85c7-608a41491819)

[PRODUCT 상세페이지 및 설정하기](https://interstellar-sunset-788761.postman.co/collections/10871481-cdba486f-5c26-4d62-8e16-d4464932eda3?version=latest&workspace=9e529a22-5100-4f53-85c7-608a41491819)

[DAY-DATE LIST](https://interstellar-sunset-788761.postman.co/collections/10871815-34aa5019-5c1b-4596-9fcf-a17a7bbf6023?version=latest&workspace=9e529a22-5100-4f53-85c7-608a41491819#e1a2af48-fdf1-4e74-8c93-1c5bc30ffa93)
