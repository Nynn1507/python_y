from common.update_danhmuc import update_danhmuc
while True:
    try:
        id_danhmuc = int(input("🔹 Nhập ID danh mục cần cập nhật: "))
        ten_moi = input("🔹 Nhập tên danh mục mới: ")
        mo_ta_moi = input("🔹 Nhập mô tả mới: ")

        update_danhmuc(id_danhmuc, ten_moi, mo_ta_moi)

    except ValueError:
        print("⚠️ ID phải là số nguyên!")

    con = input("👉 Tiếp tục (y), thoát thì nhấn ký tự bất kỳ: ")
    if con.lower() != "y":
        break
