#  AI 나만의 일기장 (AI Mood Diary)

Google Gemini API를 활용하여 작성한 일기를 분석하고, 감정에 맞는 색상과 코멘트를 생성해주는 나만의 일기장 프로젝트. 'Tkinter'에서 일기를 작성하고, 'Flask'를 통해 아름다운 카드 형태로 기록을 확인 가능함.

##  주요 기능

-   **일기 작성 및 AI 분석**: 일기를 작성하면 Gemini가 내용을 분석하여 제목, 한 줄 코멘트, 그리고 감정 색상(Hex Code)을 추출.
-   **데이터베이스 저장**: 분석된 데이터는 SQLite 데이터베이스(`diary.db`)에 안전하게 저장됨.
-   **감성적인 웹 뷰어**: 저장된 일기를 웹에서 카드 형태로 모아볼 수 있음. 각 카드는 AI가 분석한 감정 색상으로 디자인됨.



## 설치 및 실행 방법

### 1. 환경 설정

```bash
pip install flask google-generativeai python-dotenv
```

### 2. API 키 설정

프로젝트 루트 디렉토리에 `.env` 파일을 생성하고 Google Gemini API 키를 입력하세요.

```text
gemini_API_KEY=your_api_key_here
```

### 3. 데이터베이스 초기화 (최초 1회)

```bash
python init_db.py
```

### 4. 프로그램 실행

```bash
python app.py
```

## 사용 방법

1.  프로그램이 실행되면 "오늘의 일기"(tkinter) 창이 뜸.
2.  일기 내용을 입력하고 **"AI 분석 및 저장"** 버튼을 클릭.
3.  분석이 완료되면 알림창이 뜸.
4.  **"내 일기장 웹으로 보기"** 버튼을 클릭하면 웹 브라우저가 열리며 저장된 일기들을 확인 가능.

##  프로젝트 구조

```
app.py : GUI + Server
init_db.py : DB 초기화 스크립트
diary.db : SQLite 데이터베이스
.env : 환경 변수 (API Key)
templates/index.html : html 파일
static/style.css : 스타일
static/script.js : 스크립트
```
