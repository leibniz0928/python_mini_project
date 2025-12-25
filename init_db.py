import sqlite3

conn = sqlite3.connect('diary.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT DEFAULT (datetime('now', 'localtime')), -- 작성 날짜
    content TEXT NOT NULL,                            -- 일기 본문
    mood_color TEXT,                                  -- Gemini가 분석한 색상
    comment TEXT,                                     -- Gemini의 한줄 평
    title TEXT                                    -- 제목
)
''')

conn.commit()
conn.close()
print("일기 DB 초기화 완료!")