import sqlite3
import threading
import google.generativeai as genai
from flask import Flask, render_template, g
import tkinter as tk
from tkinter import messagebox
import webbrowser
import os
from dotenv import load_dotenv

# 세팅
load_dotenv()
genai.configure(api_key=os.getenv('gemini_API_KEY'))
model = genai.GenerativeModel('gemini-2.5-flash')
app = Flask(__name__)
PORT = 3000

# DB 관리
def get_db_connection():
    conn = sqlite3.connect('diary.db')
    conn.row_factory = sqlite3.Row
    return conn

# db , gemini 저장
def analyze_and_save():
    content = txt_input.get("1.0", tk.END).strip()
    
    if not content:
        messagebox.showwarning("경고", "내용을 입력하세요.")
        return

    try:
        prompt = f"""
        아래 일기를 읽고 분석해서 '색상코드, 제목, 코멘트' 순서로 답변해줘.
        색상은 일기 분위기에 어울리는 HEX 코드로, 제목은 일기의 내용을 아우르는 간단한 제목으로,코멘트는 친구처럼 다정하게 한 문장으로 일기 쓴 사람에게 하는 위로의 한 마디.
        형식: #FFFFFF | 제목 | 코멘트
        일기 내용: {content}
        """
        response = model.generate_content(prompt)
        
        analysis = response.text.split('|')
        mood_color = analysis[0].strip()
        title = analysis[1].strip()
        comment = analysis[2].strip()

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO entries (content, mood_color, title, comment)
            VALUES (?, ?, ?, ?)
        ''', (content, mood_color, title, comment))
        conn.commit()
        conn.close()

        messagebox.showinfo("성공", f"분석 완료: {title}\n일기가 저장되었습니다!")
        txt_input.delete("1.0", tk.END)

    except Exception as e:
        messagebox.showerror("에러", f"분석 중 오류 발생: {e}")

# 간단 flask server
@app.route('/')
def index():
    conn = get_db_connection()
    entries = conn.execute('SELECT * FROM entries ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('index.html', entries=entries)

def run_flask():
    app.run(port=PORT, debug=False, use_reloader=False)


def open_browser():
    webbrowser.open(f"http://127.0.0.1:{PORT}")

# GUI 화면
def start_gui():
    global root, txt_input
    root = tk.Tk()
    root.title("Gemini AI 일기장")
    root.geometry("450x500")

    tk.Label(root, text="오늘의 일기", font=("bold", 12)).pack(pady=10)
    txt_input = tk.Text(root, height=10, width=50)
    txt_input.pack(padx=20)

    btn_save = tk.Button(root, text="AI 분석 및 저장", command=analyze_and_save, bg="skyblue", height=2)
    btn_save.pack(pady=10, fill="x", padx=20)

    tk.Label(root, text="내 일기장").pack(pady=5)
    btn_web = tk.Button(root, text="내 일기장 웹으로 보기", command=open_browser, bg="lightgray")
    btn_web.pack(fill="x", padx=20)
    
    root.mainloop()

if __name__ == '__main__':
    threading.Thread(target=run_flask, daemon=True).start()
    start_gui()
    