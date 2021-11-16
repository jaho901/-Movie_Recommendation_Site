# 2021 Movie Website Project

> SSAFY 1학기 최종 프로젝트로 영화 추천 사이트를 구현하는 과정을 README로 작성한다.



## Project Period

2021.11.17~2021.11.25(18:00)



## Contributors

- 박동준 (팀장)
- 정재호

## ❗시작 전 Check List



### ☑️ pip 설치

> 프로젝트에 필요한 pip를 설치한다.

- `final-pjt-server/requirements.txt` 파일을 참조한다.



### ☑️ npm 설치

- npm 사용을 위해서 `node.js`와 `Vue Cli`가 설치되어 있는지 확인한다.
- `final-pjt-client` 폴더 안에서 아래의 명령어를 실행해본다.

```
$ node -v
$ vue --version
```

- 이후 아래의 npm을 설치한다.

```
$ npm install
```

- 기본 Vue 프로젝트 생성 이후, 추가적으로 설치한 npm은 아래와 같다.

```
$ npm install axios
$ npm install lodash
$ npm install vue bootstrap-vue bootstrap
```

- vue bootstrap 설치 후, 해당 패키지를 등록한다. 자세한 내용은 [공식홈페이지](https://bootstrap-vue.org/docs)를 참조한다.

```
 # vue bootstrap 사용예시

<template>
  <div id="app">
    <b-button>Button</b-button>
    <b-button variant="danger">Button</b-button>
    <b-button variant="success">Button</b-button>
    <b-button variant="outline-primary">Button</b-button>
  </div>
</template>
```



### ☑️ Crawling Data 관리

--간단하게 설명 추가 해 주세요



---

## 1. 팀원 정보 및 업무 분담 내역



### 박동준 : Front-end

- Vue 클라이언트 구현
- css-modeling
- web-design
- 추



### 정재호 : Back-end

- Web crawling을 통한 DB 구축

- **DRF 서버 로직 구현**
- 추천알고리즘 설계
- 가



## 2. 목표 서비스

> 현재 기획안

```
#### 최우선순위 ####
## 1. 영화 조회 서비스
- 전체 영화 조회
- 장르별 영화 조회
- 등급별 영화 조회
- 영화 상세 조회
- 영화 예고편 제공 (미확정)
- 배우 프로필 (미확정)

## 2. 영화 추천 서비스
- 장르별 추천 -> 랜덤별 추천
			-> 평점별 추천
- 등급별 추천 -> 랜덤별 추천
			-> 평점별 추천

## 3. 커뮤니티
- 영화 리뷰 작성

------- 아이디어 모음(우선순위 후위) ---------- 
- 시청한 기록 캘린더 만들기 (프로필)
- 시청한 혹은 커뮤니티 남긴거 갤러리 느낌
- 요일별 추천기능 --> 월요병을 퇴치할 호러영화
			   --> 화요일을 화끈하게 액션영화
			   --> 수요일을 
			   --> 목요일을 
			   --> 금요일을 화끈하게 에로영화 (부끄러워하는사진)
			   --> 토요일을 
			   --> 일요일을 
- 
```



## 3. 프로젝트 구조

### 3-1) 컴포넌트 구조

뷰 다 짜고나서 작성

### 3-2) DB model( ERD )

예시) 다하고나서 작성

![Database Design Project | 잡다한 IT 개발 이야기](https://hwanine.github.io/assets/images/erd.bmp)

---

구현과정 작성





---

## 오류과정 및 디버깅



## 느낀점 및 배운점

