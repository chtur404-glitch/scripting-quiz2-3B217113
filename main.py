order = []
while True:
    func = input("--- 消費紀錄統計系統 ---\n1. 新增消費\n2. 顯示消費明細\n3. 顯示統計\n4. 退出系統\n------------------------\n請選擇功能: ").strip()
    if func=="":
        print("請輸入內容")
        continue
    if not func.isdigit() and not func.isascii():
        print("請輸入半形數字")
        continue
    if int(func)>4 or int(func)<1:
        print("選項錯誤，請重新選擇")
        continue

    if func=="1":
        # 新增消費
        purchase_itmes = input("請輸入消費項目:").strip()
        if len(purchase_itmes)!=2:
            print("請盡量輸入2個字的內容，不然會很醜ww")
        while True:
            purchase_amounts = input("請輸入消費金額: ").strip()
            if purchase_amounts=="":
                print("請輸入內容")
                continue
            if not purchase_amounts.isdigit() or not purchase_amounts.isascii():
                print("請輸入半形數字")
                continue
            if purchase_amounts.count(".")>1:
                print("請輸入有效的小數點格式")
                continue
            if float(purchase_amounts)<=0:
                print("請輸入大於0的數字")
                continue
            o = {"purchase_itmes":purchase_itmes,"purchase_amounts":float(purchase_amounts)}
            order.append(o)
            # print(order)
            print("新增成功\n")
            break

    elif func=="2":
        print("--- 消費明細 ---")
        if not order:
            print("目前沒有消費紀錄\n")
            continue
        print("編號  項目          金額\n------------------------")
        for ind,o in enumerate(order):
            print(f"{ind+1:>4d} {o.get('purchase_itmes'):>3s} {o.get('purchase_amounts'):>13.2f}")
        print()
        
    elif func=="3":
        print("--- 消費統計 ---")
        if not order:
            print("目前沒有消費紀錄\n")
            continue
        c = len(order)
        total = 0
        for o in order:
            total+=o.get('purchase_amounts')
        average = total/c
        if total>=500:
            mes = "已達提醒門檻"
        elif total>=300:
            mes = "注意控制消費"
        else:
            mes = "消費不多"
        print(f"消費筆數: {c}")
        print(f"總金額: {total:.2f} 元")
        print(f"平均每筆金額: {average:.2f} 元")
        print(f"消費提醒: {mes}\n")

    elif func=="4":
        print("系統已退出")
        break
