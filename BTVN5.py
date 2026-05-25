"""
Input:
user_choice_str: Chuỗi lựa chọn menu
search_serial: Chuỗi nhập 2 số cuối của serial (Chức năng 3)
Output: Chuỗi gốc, bảng báo cáo giải mã kèm tỷ lệ Pass/Reject, thông tin sản phẩm tìm theo đuôi serial

Luồng chương trình:
Bước 1: Vòng lặp vô hạn while hiển thị menu. Nhận user_choice_str, kiểm tra bằng .isdigit() 
nếu hợp lệ thì ép kiểu sang số nguyên user_choice
Bước 2: Phân nhánh xử lý bằng match user_choice
Case 1 In trực tiếp chuỗi dữ liệu gốc raw_batch
Case 2 Dùng .split(";") để tách chuỗi thành danh sách sản phẩm. Khởi tạo tổng số sản phẩm và số sản phẩm hợp lệ 
Duyệt từng sản phẩm, làm sạch khoảng trắng và viết hoa bằng .strip().upper()
Dùng .split("-") để bóc ra 4 thuộc tính
Chuyển đổi năm sản xuất sang dạng đầy đủ: nối chuỗi "20" + năm sản xuất.
Kiểm tra bằng .isdigit() trên thuộc tính serial. Nếu đúng, ghi nhận trạng thái "Pass" và tăng valid_products.
Nếu sai, ghi nhận "Lỗi Serial - Reject"
In dữ liệu căn lề bằng f-string và tổng kết tỷ lệ phần trăm
Case 3 Nhập search_serial và làm sạch bằng .strip()
Duyệt và tách chuỗi tương tự Case 2 để lấy mã serial chuẩn của từng sản phẩm
Dùng serial[-2:] để so sánh với search_serial. Nếu khớp thì in thông tin sản phẩm
Case 4 In thông báo kết thúc ca trực và dùng break thoát vòng lặp
"""
raw_batch = " LAP-VN-23-001 ; mou-us-24-012 ; KEY-vn-23-abc ; lap-JP-22-045 ; MOn-vn-24-099 "

while True:
    print("""
===== HỆ THỐNG GIẢI MÃ DỮ LIỆU KHO HÀNG =====
1. Hiển thị chuỗi mã vạch gốc
2. Giải mã, làm sạch và in báo cáo kiểm kê
3. Tra cứu nhanh theo đuôi Serial
4. Thoát chương trình
=============================================""")
    
    user_choice_str = input("Nhập lựa chọn của bạn (1-4): ").strip()
    
    if not user_choice_str.isdigit():
        print("Chức năng không tồn tại, vui lòng nhập số từ 1-4!")
        continue
        
    user_choice = int(user_choice_str)
    if user_choice < 1 or user_choice > 4:
        print("Chức năng không tồn tại, vui lòng nhập số từ 1-4!")
        continue
        
    match user_choice:
        case 1:
            print("\n--- CHUỖI MÃ VẠCH GỐC ---")
            print(raw_batch)
            
        case 2:
            print("\n--- BÁO CÁO KIỂM KÊ SAU GIẢI MÃ ---")
            print(f"{'MÃ SP':<15} | {'XUẤT XỨ':<8} | {'NĂM SX':<6} | {'SERIAL':<6} | {'TRẠNG THÁI'}")
            print("-" * 65)
            
            products_raw = raw_batch.split(";")
            total_products = len(products_raw)
            valid_products = 0
            
            for prod in products_raw:
                cleaned_prod = prod.strip().upper()
                if not cleaned_prod:
                    total_products -= 1  
                    continue
                    
                parts = cleaned_prod.split("-")
                if len(parts) < 4:
                    continue
                    
                product_type = parts[0]
                country = parts[1]
                year_raw = parts[2]
                serial = parts[3]
                
                full_year = f"20{year_raw}"
                
                if serial.isdigit():
                    status = "Pass"
                    valid_products += 1
                else:
                    status = "Lỗi Serial - Reject"
                    
                print(f"{cleaned_prod:<15} | {country:<8} | {full_year:<6} | {serial:<6} | {status}")
                
            print("-" * 65)
            print(f"Đã giải mã thành công {valid_products} sản phẩm hợp lệ / Tổng số {total_products} sản phẩm.")

        case 3:
            print("\n--- TRA CỨU NHANH THEO ĐUÔI SERIAL ---")
            search_serial = input("Nhập 2 số cuối của Serial cần tìm: ").strip()
            
            products_raw = raw_batch.split(";")
            found = False
            
            for prod in products_raw:
                cleaned_prod = prod.strip().upper()
                if not cleaned_prod:
                    continue
                    
                parts = cleaned_prod.split("-")
                if len(parts) < 4:
                    continue
                    
                serial = parts[3]
                
                if serial[-2:] == search_serial:
                    product_type = parts[0]
                    country = parts[1]
                    full_year = f"20{parts[2]}"
                    
                    print(
                        f"\n[SẢN PHẨM PHÙ HỢP]: {cleaned_prod}\n"
                        f"- Loại sản phẩm: {product_type}\n"
                        f"- Xuất xứ: {country}\n"
                        f"- Năm sản xuất: {full_year}\n"
                        f"- Số Serial: {serial}\n"
                    )
                    found = True
                    
            if not found:
                print("Không tìm thấy sản phẩm phù hợp")

        case 4:
            print("Tạm biệt!")
            break