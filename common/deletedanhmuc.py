# 🗑️ Hàm xóa danh mục
from ketnoidb.ketnoi_mysql import connect_mysql
from mysql.connector import Error

def delete_danhmuc(id_danhmuc):
    try:
        connection = connect_mysql()
        if connection is None:
            return

        cursor = connection.cursor()
        sql = "DELETE FROM danhmuc WHERE id = %s"
        data = (id_danhmuc,)
        cursor.execute(sql, data)
        connection.commit()

        print(f"🗑️ Đã xóa danh mục có ID: {id_danhmuc}")


    except Error as e:

        if e.errno == 1451:

            print("⚠️ Không thể xóa: danh mục này đang được sử dụng trong bảng sản phẩm!")

        else:

            print("❌ Lỗi khi xóa danh mục:", e)


    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
