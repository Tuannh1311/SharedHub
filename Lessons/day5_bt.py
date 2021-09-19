# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 15:00:40 2019

@author: MabuXayda
"""

"""============================================================================
15. Viết function tính tần suất xuất hiện các từ(cách nhau bởi dấu cách " ") 
từ input. In ra màn hình kết quả sau khi đã sắp xếp theo bảng chữ cái.
VD Input: 
New to Python or choosing between Python 2 and Python 3? Read Python 2 or 
Python 3.
- Output: 2:2 , 3.:1 , 3?:1 , New:1 , Python:5 , Read:1 , and:1 , between:1 ,
 choosing:1 , or:2 , to:1
"""

"""============================================================================
16.Viết module triangle trong đó có các hàm:
- kiểm tra xem tam giác là tam giác cân, tam giác đều, tam giác vuông 
hay thường?
- tính chu vi tam giác
- tính diện tính tam giác.
input các hàm trên là chiều dài 3 cạnh tam giác.
"""

"""============================================================================
17. Xây dựng function trả về ma trận đơn vị kích thước N*N
VD Input: N = 3
Ouput = [[1,0,0],[0,1,0],[0,0,1]]
"""

"""============================================================================
18. Xây dựng module mymath.py gồm các function sau:
- xuất ra giá trị xuất hiện nhiều nhất trong 1 list số, trả về nhiều giá trị 
nếu có.(gọi ý dùng mode() trong statistics)
VD: Input:[1,2,5,7,3,7,7,5,8,5]
Output: 5, 7

- tính giai thừa 1 số nguyên.

- kiểm tra 1 số có phải là số nguyên tố hay không? 
(số nguyên tố là số chỉ chia hết cho 1 và chính nó.)

- kiểm tra 1 số có phải số chính phương hay không? 
(số chính phương là số có căn bậc 2 là số tự nhiên.)
Tạo 1 file main.py để gọi hàm từ module mymath
"""

"""============================================================================
19. In ra 10 file với cấu trúc file như sau: dòng đầu là id file(id = 1,2..10), 
tiếp theo là n dòng "Hello world!" với n = id.
vd file 1:
id 1
Hello world!
file 2:
id 2
Hello world!
Hello world!
file 3 :
id 3
Hello world!
Hello world!
Hello world!
"""

"""============================================================================
20.
Viết hàm nhận vào file transaction.txt với dòng đầu tiên là id của tài khoản, 
dòng thứ 2 là số tài khoản, dòng thứ 3 là số dư tài khoản, các dòng tiếp theo 
hiển thị nội dung giao dịch 
    + Với D,100 là nộp vào ngân hàng 100. 
    + Với W,100 là rút ra 100 từ tài khoản. 
Hàm trả về số dư cuối cùng của tài khoản
vd input:
Id1
Tk01
400
D,100
W,200
-> output: 300
"""

"""============================================================================
21.
File txt với nội dung file theo cú pháp sau: file gồm nhiều dòng, mỗi dòng 
tương ứng với tên học sinh và điểm số học Python được cách nhau bởi dấu phẩy.  
Ví  dụ:
Nam,10
Nữ,9

Viết hàm với input đầu vào là đường dẫn của file, hàm trả về danh sách các bạn 
được điểm cao nhất và điểm cao nhất
"""

"""============================================================================
22.
Một Robot di chuyển trong mặt phẳng bắt đầu từ điểm đầu tiên. 
Robot có thể di chuyển theo hướng UP, DOWN, LEFT và RIGHT với những bước 
nhất định. Dấu di chuyển của robot được lấy từ file txt đầu vào, với 2 dòng 
đầu tiên thể hiện vị trí điểm đầu tiên, các dòng tiếp theo thể hiện quá trình 
di chuyển trong đó các con số phía sau hướng di chuyển chính là số bước đi 
VD: Input: 
X0 4 
Y0 3 
UP 5 
DOWN 3 
LEFT 3 
RIGHT 3 

Hãy viết hàm trả về khoảng cách từ vị trí hiện tại đến vị trí đầu tiên, 
sau khi robot đã di chuyển một quãng đường với input là tên file txt.
"""
"""===========================================================================
23. Tìm số nguyên dương N bé nhất sao cho N chia hết cho tất cả các số trong 
đoạn [1, 20]
"""

"""============================================================================
24. Viết function kiểm tra chuỗi kí tự ng dùng nhập vào từ bàn phím, điều kiện
tương tự như bài 11. Bổ sung thêm chức năng nếu như không thỏa điều kiện thì
cho phép người dùng nhập lại, nhưng tối đa ng dùng chỉ được nhập 4 lần.
"""

"""============================================================================
25.
Viết function cho phép người dùng nhập ngày, tháng, năm từ bàn phím.
In ra màn hình kiểm tra ngày người dùng vừa nhập:
    + là ngày thứ mấy trong tuần
    + là ngày thứ bao nhiêu trong năm
    + tháng đó có bao nhiêu ngày
    + năm đó có phải là năm nhuận hay không
"""

