class sinhvien:

    count = 0

    def __init__(self , id , name,Math_Point, Physics_Point, Chemistry_Point):
        self.id = id
        self.name = name
        self.Math_Point = Math_Point
        self.Physics_Point = Physics_Point
        self.Chemistry_Point = Chemistry_Point


    def get_id(self):
        return self.id

    def set_Name(self, name):
        self.name = name

    def get_Name(self):
        return self.name

    def show_info(self):
        print(f"\nThông tin Sinh Viên :  \n")
        print(f"Id :  { self.get_id() }")
        print(f"Tên Sinh Viên :  { self.name }")
        print(f"điểm toán :  { self.Math_Point}")
        print(f"diểm Hóa :  {self.Physics_Point}")
        print(f"điểm Lý :  {self.Chemistry_Point}")
        print(f"điểm Trung Bình :  {int(self.Math_Point+self.Physics_Point+self.Chemistry_Point)/3}")







