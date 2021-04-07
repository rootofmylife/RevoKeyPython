# RevoKey

Hướng dẫn sử dụng phần mềm chuyển đổi văn tự tiếng Việt.

## Lưu ý

Không thể sử dụng nhiều bộ gõ lên 1 chữ. Ví dụ: 'quân' -> ta gõ như sau: gõ chữ 'q', phần mềm sẽ dịch sang chữ 'k', sau đó cần cách ra (spacebar) để gõ nốt chữ 'uân'. 

Khi gõ sai 1 ký tự, phải gõ lại từ đầu thì bộ gõ mới nhận dạng được chữ đó.

## Cách sử dụng

- Với các chữ như `q`, `c`, `ch` v.v., thao tác phím như bình thường
- Với các chữ như `ia`, `ua` v.v., cần có thêm dấu câu, vì vậy, để xử lý trường hợp này, phần mềm giải quyết như sau:

	Đối với người sử dụng bảng gõ VNI

		- dấu huyền: gõ chữ `f` 
		- dấu sắc: gõ chữ `s`
		- dấu hỏi: gõ chữ `w`
		- dấu ngã: gõ chữ `o`
		- dấu nặng: gõ chữ `j`
		- dấu ngang: gõ dấu `=`

	Đối với người sử dụng bảng gõ Telex:

		- dấu huyền: gõ số `2` 
		- dấu sắc: gõ số `1`
		- dấu hỏi: gõ số `3`
		- dấu ngã: gõ số `4`
		- dấu nặng: gõ số `5`
		- dấu ngang: gõ dấu `=`
- Ví dụ: 
		- gõ chữ `i` sau đó đến chữ `a`, rồi gõ thêm dấu `=`, máy tính sẽ hiển thị là `iê`
		- gõ chữ `i` sau đó đến chữ `a`, rồi gõ thêm dấu `j`, máy tính sẽ hiển thị là `iệ`
		- gõ chữ `u` sau đó đến chữ `a`, rồi gõ thêm dấu `=`, máy tính sẽ hiển thị là `uô`
		- gõ chữ `u` sau đó đến chữ `a`, sau đó gõ thêm `i`, rồi gõ thêm dấu `s`, máy tính sẽ hiển thị là `uá`
- Riêng với chữ `uyê`, chỉ cần gõ là `uye` là máy tính tự động hiểu.
- Ví dụ:
		- gõ chữ `u` sau đó đến chữ `y`, sau đó gõ thêm `e`, rồi gõ thêm số `2`, máy tính sẽ hiển thị là `uiề`
