# 初始化一個空列表來存儲所有人員記錄
records = []

def display_menu():
    """顯示主選單"""
    print("\n--- 人事資料管理系統 ---")
    print("1. 新增資料")
    print("2. 查詢資料")
    print("3. 修改資料")
    print("4. 刪除資料")
    print("5. 顯示所有資料")
    print("6. 退出系統")
    print("------------------------")

def add_record():
    """新增資料功能"""
    while True:
        department = input("請輸入部門: ")
        name = input("請輸入姓名: ")
        age = input("請輸入年齡: ")
        phone = input("請輸入手機號碼: ")

        # 將輸入的資料存入字典
        record = {
            "部門": department,
            "姓名": name,
            "年齡": age,
            "手機": phone
        }

        # 將字典加入到記錄列表中
        records.append(record)

        # 詢問是否繼續新增
        continue_add = input("是否繼續新增資料? (y/n): ").lower()
        if continue_add != 'y':
            break

def search_record():
    """查詢資料功能"""
    name = input("請輸入要查詢的姓名: ")
    found = False
    for record in records:
        if record["姓名"] == name:
            print("\n--- 查詢結果 ---")
            display_table([record])
            found = True
            break
    if not found:
        print("查無此人。")

def modify_record():
    """修改資料功能"""
    name = input("請輸入要修改的姓名: ")
    for record in records:
        if record["姓名"] == name:
            print("當前資料:")
            display_table([record])

            print("\n1. 修改部門")
            print("2. 修改姓名")
            print("3. 修改年齡")
            print("4. 修改手機")
            choice = input("請選擇要修改的欄位: ")

            if choice == "1":
                record["部門"] = input("請輸入新的部門: ")
            elif choice == "2":
                record["姓名"] = input("請輸入新的姓名: ")
            elif choice == "3":
                record["年齡"] = input("請輸入新的年齡: ")
            elif choice == "4":
                record["手機"] = input("請輸入新的手機: ")
            else:
                print("無效的選擇。")
                return

            print("\n--- 更新後的資料 ---")
            display_table([record])
            return
    print("查無此人。")

def delete_record():
    """刪除資料功能"""
    name = input("請輸入要刪除的姓名: ")
    for record in records:
        if record["姓名"] == name:
            confirm = input(f"確定要刪除 {name} 的資料嗎? (y/n): ").lower()
            if confirm == 'y':
                records.remove(record)
                print(f"{name} 的資料已刪除。")
                print("\n--- 剩餘的所有資料 ---")
                display_all_records()
            return
    print("查無此人。")

def display_all_records():
    """顯示所有資料功能"""
    if records:
        display_table(records)
    else:
        print("目前沒有任何資料")

def display_table(data):
    """以表格形式顯示資料"""
    print("{:<10} {:<10} {:<10} {:<15}".format("部門", "姓名", "年齡", "手機"))
    print("-" * 45)
    for record in data:
        print("{:<10} {:<10} {:<10} {:<15}".format(
            record["部門"], record["姓名"], record["年齡"], record["手機"]))

def main():
    """主程序"""
    while True:
        display_menu()
        choice = input("請選擇功能: ")

        if choice == "1":
            add_record()
        elif choice == "2":
            search_record()
        elif choice == "3":
            modify_record()
        elif choice == "4":
            delete_record()
        elif choice == "5":
            display_all_records()
        elif choice == "6":
            print("系統已退出。")
            return
        else:
            print("無效的選擇，請重新輸入。")

if __name__ == "__main__":
    main()
