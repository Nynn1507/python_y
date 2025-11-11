# insertdanhmuc.py
# 💾 Hàm thêm danh mục mới

from ketnoidb.ketnoi_mysql import connect_mysql
from mysql.connector import Error

def insert_danhmuc(ten_danhmuc, mo_ta):
    try:
        connection = connect_mysql()
        if connection is None:
            print("❌ Không thể kết nối MySQL!")
            return

        cursor = connection.cursor()
        sql = "INSERT INTO danhmuc (ten_danhmuc, mo_ta) VALUES (%s, %s)"
        data = (ten_danhmuc, mo_ta)
        cursor.execute(sql, data)
        connection.commit()

        print(f"✅ Đã thêm danh mục: {ten_danhmuc}")
    except Error as e:
        print("❌ Lỗi khi thêm danh mục:", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

