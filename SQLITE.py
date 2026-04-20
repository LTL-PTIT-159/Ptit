import sqlite3


conn = sqlite3.connect('university.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        major TEXT,
        gpa REAL
    )
''')
print("Bảng 'students' đã được tạo.")


students_data = [
    ('Nguyen Van A', 'CNTT', 3.5),
    ('Tran Thi B', 'Kinh Te', 2.8),
    ('Le Van C', 'CNTT', 3.9),
    ('Pham Thi D', 'Ngon Ngu', 1.9),
    ('Hoang Van E', 'Co Khi', 3.2)
]

cursor.executemany("INSERT INTO students (name, major, gpa) VALUES (?, ?, ?)", students_data)
conn.commit()
print("Đã thêm 5 sinh viên.")


print("\n--- Tất cả sinh viên ---")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)


print("\n--- Sinh viên có GPA > 3.0 ---")
cursor.execute("SELECT * FROM students WHERE gpa > 3.0")
for row in cursor.fetchall():
    print(row)


print("\n--- Cập nhật GPA ---")
cursor.execute("UPDATE students SET gpa = 3.8 WHERE name = 'Nguyen Van A'")
conn.commit()
print("Đã cập nhật GPA của Nguyen Van A thành 3.8.")


print("\n--- Xóa sinh viên GPA < 2.0 ---")
cursor.execute("DELETE FROM students WHERE gpa < 2.0")
conn.commit()
print("Đã xóa các sinh viên có GPA < 2.0.")

print("\n--- Dữ liệu cuối cùng ---")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

conn.close()
