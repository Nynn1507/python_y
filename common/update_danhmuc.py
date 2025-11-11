from ketnoidb.ketnoi_mysql import connect_mysql
from mysql.connector import Error

def update_danhmuc(id_danhmuc, ten_moi, mo_ta_moi):
    try:
        # Kết nối MySQL
        connection = connect_mysql()
        if connection is None:
            print("⚠️ Không thể kết nối tới MySQL.")
            return

        cursor = connection.cursor()

        # Câu lệnh UPDATE
        sql = """
        UPDATE danhmuc 
        SET ten_danhmuc = %s, mo_ta = %s 
        WHERE id = %s
        """
        data = (ten_moi, mo_ta_moi, id_danhmuc)

        cursor.execute(sql, data)
        connection.commit()

        # Kiểm tra kết quả
        if cursor.rowcount > 0:
            print(f"✅ Đã cập nhật danh mục ID {id_danhmuc} thành công!")
        else:
            print(f"⚠️ Không tìm thấy danh mục có ID {id_danhmuc}.")

    except Error as e:
        print("❌ Lỗi khi cập nhật danh mục:", e)

    finally:
        # Đóng kết nối
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
