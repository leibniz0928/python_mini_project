import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime

# ------------------- 설정 -------------------
DATA_FILE = "diary_data.json"

# ------------------- 기능 -------------------

def save_diary():
    # 1. 내용 가져오기
    content = txt_input.get("1.0", tk.END).strip()
    
    if not content:
        messagebox.showwarning("경고", "내용을 써주세요!")
        return

    # 2. 기존 파일 읽기 (with 문 사용)
    # with 블록을 빠져나오면 파일이 자동으로 닫힙니다.
    with open(DATA_FILE, "a+", encoding="utf-8") as f:
        f.seek(0) # a+ 모드는 커서가 끝에 있어서 앞으로 옮겨야 함
        file_content = f.read()

    # 파일 내용이 비어있으면 빈 리스트, 아니면 JSON 불러오기
    if file_content == "":
        data_list = []
    else:
            data_list = json.loads(file_content)

    # 3. 새 데이터 만들기
    new_data = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "text": content
    }
    data_list.append(new_data)

    # 4. 파일에 저장하기 (with 문 사용)
    # 쓰기 모드('w')로 열어서 저장
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data_list, f, ensure_ascii=False, indent=4)

    # 5. 저장 완료 알림
    messagebox.showinfo("성공", "일기가 저장되었습니다!")
    
    # 입력창 비우기
    txt_input.delete("1.0", tk.END)

# ------------------- 화면(GUI) -------------------
root = tk.Tk()
root.title("나만의 일기장 (With ver.)")
root.geometry("400x300")

tk.Label(root, text="오늘의 일기", font=("bold", 12)).pack(pady=10)

txt_input = tk.Text(root, height=10, width=40)
txt_input.pack(padx=10)

btn = tk.Button(root, text="저장하기", command=save_diary, bg="lightgreen", height=2)
btn.pack(pady=15, fill="x", padx=20)

root.mainloop()