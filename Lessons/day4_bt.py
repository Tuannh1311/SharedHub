# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 17:02:02 2019

@author: MabuXayda
"""

"""

6.1 Viết function truyền vào số nguyên dương n. Trả về list bình phương của
các số từ 1->n.
VD: 
input: 4
output: [1, 4, 9, 16]


7. Viết function truyền vào 2 tham số m: số dân hiện tại và n: số năm
trả về dân số của 1 nước sau n năm, tì lệ tăng dân số là 1.8%

8. Viết function cho người dùng nhập chỉ số điện mới và cũ từ bàn phím.
In ra màn hình chỉ số cũ, chỉ số mới, tiền trả định mức, 
tiền trả vượt định mức, tổng tiền phải trả. 

Định mức sử dụng điện cho mỗi hộ là: 50 KW với giá 230đ/KW
Nếu phần vượt định mức <= 50KW thì tính giá 480đ/KW
Nếu 50KW < phần vượt định mức < 100KW thì tính giá 700đ/KW 
Nếu phần vượt định mức >= 100KW thì tính giá 900đ/KW 

9. Viết function trả về kết quả xếp loại học lực của học sinh. 
Giả sử học sinh chỉ có bốn cột điểm Toán (T), Lý (L), Hóa (H) và Anh văn (AV). 
Điểm 4 môn được nhập vào từ bàn phím và theo thang điểm 100. 

Qui tắc xếp loại như sau:
    + Nếu trung bình 4 môn lớn hơn hoặc bằng 80 và không có môn nào nhỏ hơn 65, 
    thì xếp loại Giỏi.
    + Nếu học sinh không đủ điều kiện đạt loại giỏi, mà có trung bình 4 môn 
    lớn hơn hoặc bằng 65 và không có môn nào nhỏ hơn 50, thì xếp loại Khá.
    + Nếu học sinh không đủ điều kiện đạt loại Khá, mà có trung bình 4 môn 
    lớn hơn hoặc bằng 50 và không có môn nào nhỏ hơn 20, thì xếp loại 
    Trung bình.
    + Nếu học sinh không đạt 3 loại trên thì xếp loại Yếu.

10. Viêt function truyền vào 2 số A, B < 2000, trả về danh sách chứa tất cả
các số chia hết cho 7 nhưng không chia hết cho 5, nằm trong đoạn từ A 
đến B(tính cả A và B)

11. Viết function in ra màn hình xem chuỗi kí tự nhập vào từ người dùng có hợp
lệ hây không. Chuỗi hợp lệ là chuỗi có chiều dài ít nhất 8 kí tự, chứa ít nhất
một chữ in hoa, chứ ít nhất một kí tự dạng số.

12. Tạo danh sách các số nguyên dương nhỏ hơn 60000 có đặc điểm sau: số đó 
gồm n chữ số, tổng lũy thừa bậc n của các chữ số đó bằng chính số đó
VD: 
    153 là số có 3 chữ số, 
    và 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
    
13. Cho trước 2 dictionary, viết chương trình kết hợp 2 dictionary đó, đối với 
các item có cùng key thì cộng value lại với nhau.
VD
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
output: {'a': 400, 'b': 400, 'd': 400, 'c': 300}


14. Viết function truyền vào số nguyên dương n <= 30, trả về dictionary có độ 
dài = n sao cho mỗi cặp item có dạng (x:x*x).
VD: 
với n = 5
output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}



"""