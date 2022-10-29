from ttt import sinhvien

ds = []

while True:
    print(f'''\n

    1. Thêm Sinh Viên, Math_Point, Physics_Point, Chemistry_Point
    2. Xóa sinh viên
    3. Chỉnh sửa thông tin
    4. Xem thông tin tất cả sinh viên
    5. Thoát Chương trình

    ''')
    select = input("Mời chọn chức năng:  ")

    if str(select).isdigit():
        select = int(select)
        if select == 5:
            break
        elif select == 1:
            while True:
                id = int(input("Nhập Id Sinh viên:  "))
                if 0 < id < 100:
                    break
                else:
                    print('nhập lại id từ 0-->100  ')
                    continue
            name = input("Nhập Tên Sinh viên:  ")
            name.strip()
            while True:
                print('mời nhập các điểm số từ 1-->10')
                Math_Point = int(input('nhập điểm môn Toán:'))
                Physics_Point = int(input('nhập điểm môn Lý:'))
                Chemistry_Point = int(input('nhập điểm môn Hóa'))
                if 0 <= Math_Point <= 10 and 0 <= Physics_Point <= 10 and 0 <= Chemistry_Point <= 10:
                    break
                else:
                    print('mời nhập lại điểm các môn học từ 1-->10')
                    continue
            sv = sinhvien(id, name, Math_Point, Physics_Point, Chemistry_Point)
            ds.append(sv)



        elif select == 4:
            if len(ds) == 0:
                print("\n hiện không có sinh viên . Bạn vui lòng thêm sinh viên mói vào danh sách !")
            else:
                print(f"\nHiện có {len(ds)} Sinh viên ")
                for i in ds:
                    i.show_info()
        elif select == 3:
            id = input("Nhập Id sinh Viên bạn cần sửa :  ")
            for i in ds:
                if i.get_id() == id:
                    i.set_Name(input("Nhập vào tên mới:  "))

                    i.show_info()
                else:
                    print('không có sinh viên tồn tại')


        elif select == 2:
            id = input("Nhập Id Sinh viên cần xóa :  ")

            for i in ds:
                ds.remove(i)
                print("Bạn đã xóa sinh viên thành công ")
                continue





    else:
        print("\nBạn phải nhập số. Vui Lòng nhập lại !")