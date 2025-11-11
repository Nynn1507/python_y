import mysql.connector
from mysql.connector import Error

def connect_mysql():
    try:
        connection = mysql.connector.connect(
            host='localhost',       # hoặc 127.0.0.1
            user='root',            # tên user MySQL
            password='',            # mật khẩu (nếu có thì điền vào)
            database='qlthuocankhang'   # tên database của bạn
        )

        if connection.is_connected():
            print("✅ Kết nối MySQL thành công!")
            return connection

    except Error as e:
        print(f"❌ Lỗi khi kết nối MySQL: {e}")
        return None
