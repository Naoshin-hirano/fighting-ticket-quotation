from group import Group
from sheet import Sheet
from goods import Goods

# 格闘団体
group_index = 0
group_status = ""
totalAmount = 0
group1 = Group("K-1", 20)
group2 = Group("Rizin", 19)
groups = [group1, group2]
for group in groups:
    print(str(group_index) + " :" + group.name)
    group_index += 1
print('--------------------')
group_list = int(input("団体名を選んでください> "))
select_group = groups[group_list]
if group_list == 0:
    group_status = "k1"
else:
    group_status = "rizin"


# シート選び
sheet_index = 0
if group_status == "k1":
    k1_sheet1 = Sheet("SRS", 20000, 20)
    k1_sheet2 = Sheet("RS", 15000, 20)
    k1_sheet3 = Sheet("S", 10000, 20)
    sheets = [k1_sheet1, k1_sheet2, k1_sheet3]
    for sheet in sheets:
        print(str(sheet_index) + " :" + sheet.type)
        sheet_index += 1
else:
    rizin_sheet1 = Sheet("SRS", 20000, 19)
    rizin_sheet2 = Sheet("RS", 15000, 19)
    rizin_sheet3 = Sheet("S", 10000, 19)
    sheets = [rizin_sheet1, rizin_sheet2, rizin_sheet3]
    for sheet in sheets:
        print(str(sheet_index) + " :" + sheet.type)
        sheet_index += 1
print('--------------------')
sheet_list = int(input("どの席にしますか?> "))
your_sheet = sheets[sheet_list]
totalAmount += your_sheet.add_extra_price()


# グッズ購入
if group_status == "k1":
    # K1
    k1_index = 0
    k1_1 = Goods("武尊応援シート", 5000)
    k1_2 = Goods("皇治応援シート", 4000)
    k1s = [k1_1, k1_2]
    for k1 in k1s:
        print(str(k1_index) + " :" + k1.goods + "(¥" + str(k1.addDotto(k1.price)) + ")")
        k1_index += 1
    print('--------------------')
    k1_goods_list = int(input("グッズはなに買いますか?> "))
    k1_goods = k1s[k1_goods_list]
    totalAmount += k1_goods.add_goods_price()
else:
    # Rizin
    rizin_index = 0
    rizin_1 = Goods("ミニyogi棒", 8000)
    rizin_2 = Goods("朝倉未来Tシャツ", 4000)
    rizins = [rizin_1, rizin_2]
    for rizin in rizins:
        print(str(rizin_index) + " :" + rizin.goods + "(¥" + str(rizin.addDotto(rizin.price)) + ")")
        rizin_index += 1
    print('--------------------')
    rizin_goods_list = int(input("グッズはなに買いますか?> "))
    rizin_goods = rizins[rizin_goods_list]
    totalAmount += rizin_goods.add_goods_price()

# 見積書表示
print(str(select_group.name) + "に参加予定")
add_dotto_price = your_sheet.addDotto(your_sheet.add_extra_price())
print(str(your_sheet.type) + "席で観戦" + "(¥" + str(add_dotto_price) + " <直近割高費用込み>" + ")")
if group_status == "k1":
    add_dotto_price = k1_goods.addDotto(k1_goods.add_goods_price())
    print("購入したK1グッズ: " + k1_goods.goods + "(¥" + str(add_dotto_price) + ")")
else:
    add_dotto_price = rizin_goods.addDotto(rizin_goods.add_goods_price())
    print("購入したRizinグッズ: " + rizin_goods.goods + "(¥" + str(add_dotto_price) + ")")

print("税抜き金額 : " + "¥" + str(your_sheet.addDotto(totalAmount)))

inc_tax = select_group.addTax(int(totalAmount))

print("合計金額（税込み）: " + "¥" + str(inc_tax))