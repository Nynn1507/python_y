import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

# ====================== KẾT NỐI DATABASE ======================
def connect_mysql():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="qlthuocankhang"
        )
        return connection
    except mysql.connector.Error as e:
        messagebox.showerror("Lỗi", f"Không thể kết nối MySQL: {e}")
        return None


# ====================== HÀM XỬ LÝ ======================
def load_data():
    for i in tree.get_children():
        tree.delete(i)
    conn = connect_mysql()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM danhmuc")
        for row in cursor.fetchall():
            tree.insert("", "end", values=row)
        conn.close()


def add_danhmuc():
    ten = entry_ten.get()
    mota = entry_mota.get()
    if not ten:
        messagebox.showwarning("Thiếu dữ liệu", "Vui lòng nhập tên danh mục!")
        return

    conn = connect_mysql()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO danhmuc (ten_danhmuc, mo_ta) VALUES (%s, %s)", (ten, mota))
        conn.commit()
        conn.close()
        messagebox.showinfo("Thành công", "Đã thêm danh mục mới!")
        load_data()


def delete_danhmuc():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Chọn danh mục", "Vui lòng chọn danh mục cần xóa!")
        return

    id = tree.item(selected[0])["values"][0]
    conn = connect_mysql()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM danhmuc WHERE id = %s", (id,))
            conn.commit()
            messagebox.showinfo("Thành công", "Đã xóa danh mục!")
        except mysql.connector.Error as e:
            messagebox.showerror("Lỗi", f"Không thể xóa: {e}")
        finally:
            conn.close()
            load_data()


def update_danhmuc():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Chọn danh mục", "Vui lòng chọn danh mục cần cập nhật!")
        return

    id = tree.item(selected[0])["values"][0]
    ten = entry_ten.get()
    mota = entry_mota.get()
    if not ten:
        messagebox.showwarning("Thiếu dữ liệu", "Tên danh mục không được để trống!")
        return

    conn = connect_mysql()
    if conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE danhmuc SET ten_danhmuc = %s, mo_ta = %s WHERE id = %s", (ten, mota, id))
        conn.commit()
        conn.close()
        messagebox.showinfo("Thành công", "Đã cập nhật danh mục!")
        load_data()


def on_select(event):
    selected = tree.selection()
    if selected:
        values = tree.item(selected[0])["values"]
        entry_ten.delete(0, tk.END)
        entry_mota.delete(0, tk.END)
        entry_ten.insert(0, values[1])
        entry_mota.insert(0, values[2])


# ====================== GIAO DIỆN CHÍNH ======================
root = tk.Tk()
root.title("Quản lý danh mục - By Nynn ✨")
root.geometry("600x400")
root.config(bg="#F7F9FB")

frame_form = tk.Frame(root, bg="#F7F9FB")
frame_form.pack(pady=10)

tk.Label(frame_form, text="Tên danh mục:", bg="#F7F9FB").grid(row=0, column=0, padx=10, pady=5)
entry_ten = tk.Entry(frame_form, width=40)
entry_ten.grid(row=0, column=1)

tk.Label(frame_form, text="Mô tả:", bg="#F7F9FB").grid(row=1, column=0, padx=10, pady=5)
entry_mota = tk.Entry(frame_form, width=40)
entry_mota.grid(row=1, column=1)

frame_btn = tk.Frame(root, bg="#F7F9FB")
frame_btn.pack(pady=10)

tk.Button(frame_btn, text="➕ Thêm", command=add_danhmuc, bg="#A7E9AF").grid(row=0, column=0, padx=5)
tk.Button(frame_btn, text="✏️ Sửa", command=update_danhmuc, bg="#FFD580").grid(row=0, column=1, padx=5)
tk.Button(frame_btn, text="🗑️ Xóa", command=delete_danhmuc, bg="#FF9B9B").grid(row=0, column=2, padx=5)
tk.Button(frame_btn, text="🔄 Làm mới", command=load_data, bg="#B5EAEA").grid(row=0, column=3, padx=5)

tree = ttk.Treeview(root, columns=("ID", "Tên danh mục", "Mô tả"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Tên danh mục", text="Tên danh mục")
tree.heading("Mô tả", text="Mô tả")
tree.pack(fill="both", expand=True, padx=10, pady=10)
tree.bind("<<TreeviewSelect>>", on_select)

load_data()
root.mainloop()
