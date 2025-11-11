from ketnoidb.ketnoi_mysql import connect_mysql
from mysql.connector import Error

def get_all_danhmuc():
    try:
        connection = connect_mysql()
        if connection is None:
            return

        cursor = connection.cursor(dictionary=True)  # Trả kết quả dạng dict
        sql = "SELECT * FROM danhmuc"
        cursor.execute(sql)
        result = cursor.fetchall()

        if result:
            print("📋 Danh sách danh mục:")
            for row in result:
                print(f"- ID: {row['id']}, Tên: {row['ten_danhmuc']}, Mô tả: {row['mo_ta']}")
        else:
            print("⚠️ Không có danh mục nào trong cơ sở dữ liệu.")

    except Error as e:
        print("❌ Lỗi khi lấy danh mục:", e)

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
