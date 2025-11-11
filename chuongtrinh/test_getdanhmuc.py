from common.get_danhmuc import get_all_danhmuc

while True:
    get_all_danhmuc()
    con = input("TIẾP TỤC (y), THOÁT thì nhấn ký tự bất kỳ: ")
    if con.lower() != "y":
        break
