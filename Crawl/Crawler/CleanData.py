# -*- coding: utf-8 -*-
from heapq import heappushpop
import pandas as pd
import numpy as np


def clean_data(data):
    data = data.replace("---", np.nan)
    data = data.replace("_", np.nan)

    # xu li dien tich
    Square = data['DT']
    Square1 = []
    for square in Square:
        square = str(square).replace(",", ".")
        Square1.append(float(square.replace("m", "")))
    duongtruocnha = data['Đường trước nhà']
    duongtruocnha1 = []
    for dtn in duongtruocnha:
        dtn = str(dtn).replace(",", ".")
        duongtruocnha1.append(float(dtn.replace("m", "")))
    # Price = data["Giá"]
    # i = 0
    # Price1 = []
    # price=Price[i]
    # area=Square[i]
    # if 'tỷ' in price:
    #     replacePrice=price.replace(",",".")
    #     changeToMoney=float(replacePrice[:replacePrice.find('t')-1])*1000000000
    #     Price1.append(changeToMoney)
    # elif '/ m' in price:
    #     replacePrice=price.replace(",",".")
    #     changeToMoney=float(replacePrice[:replacePrice.find('t')-1])*1000000*int(Square[:area.find('m')-1])
    #     Price1.append(changeToMoney)
    # else:
    #     changeToMoney=float(price[:price.find('t')-1])*1000000
    #     Price1.append(changeToMoney)
    price = data["Giá"]
    i = 0
    price1 = []
    for p in price:
        p = str(p).replace(",", ".")
        print(i)
        if "tỷ" in str(p):
            p = float(p.replace("tỷ", ""))
            p = p * 1000000000
        elif "triệu" in str(p):
            p = float(p.replace("triệu", ""))
            p = p * 1000000
        i = i + 1
        price1.append(float(p))
    phaply = data['Pháp lý']
    phaply1 = []
    for pl in phaply:
        if pl == '---':
            phaply1.append("")
        else:
            phaply1.append(pl)
    santhuong = data['Sân thượng']
    santhuong1 = []
    for st in santhuong:
        if st == '---':
            santhuong1.append("")
        else:
            santhuong1.append(st)
    chinhchu = data['Chính chủ']
    chinhchu1 = []
    for st in chinhchu:
        if st == '---':
            chinhchu1.append("")
        else:
            chinhchu1.append(st)
    chieungang = data['Chiều ngang']
    chieungang1 = []
    for cn in chieungang:
        if cn != np.nan:
            cn = str(cn).replace(",", ".")
            cn = str(cn).replace("m", "")
        chieungang1.append(float(cn))
    solau = data['Số lầu']
    solau1 = []
    for cn in solau:
        if cn == '---':
            solau1.append("")
        else:
            solau1.append(cn)
    huong = data['Hướng']
    huong1 = []
    for cn in huong:
        if cn == '_':
            huong1.append("")
        else:
            huong1.append(cn)
    bedroom = data['Số phòng ngủ']
    bedroom1 = []
    for cn in bedroom:
        if cn == '---':
            bedroom1.append("")
        else:
            bedroom1.append(cn)
    diningroom = data['Phòng ăn']
    diningroom1 = []
    for cn in diningroom:
        if cn == '---':
            diningroom1.append("")
        else:
            diningroom1.append(cn)
    kitchen = data['Nhà bếp']
    kitchen1 = []
    for cn in kitchen:
        if cn == '---':
            kitchen1.append("")
        else:
            kitchen1.append(cn)
    parking = data['Chổ để xe hơi']
    parking1 = []
    for cn in parking:
        if cn == '---':
            parking1.append("")
        else:
            parking1.append(cn)

    chieudai = data['Chiều dài']
    chieudai1 = []
    for cd in chieudai:
        if cd != np.nan:
            cd = str(cd).replace(",", ".")
            cd = str(cd).replace("m", "")
        chieudai1.append(float(cd))

    duong = data['Đường']
    phuongxa = data['Phường-Xã']
    quanhuyen = data['Quận-Huyện']
    typeofnew = data['Loại tin']
    typeofEstate = data['Loại BDS']
    df = pd.DataFrame({'Route': duong, 'Ward': phuongxa, 'District': quanhuyen, 'Price': price1, 'Type Of New': typeofnew, 'Type Of Estate': typeofEstate, 'Owned': chinhchu1, 'Legal': phaply1, 'Square': Square1, 'Width': chieungang1, 'Length': chieudai1,
                       'Floors': solau1, 'Bedrooms': bedroom1, 'Direction': huong1, 'Road': duongtruocnha1, 'DinningRoom': diningroom1, 'Kitchen': kitchen1, 'Terrace': santhuong1, 'Garage': parking1, })
    df.to_csv('Data/data1.csv', index=True, encoding='utf-8-sig')
    return data


data = pd.read_csv("DataScience/data.csv")
# data = pd.read_csv("D:/Ky6/KHDL/Data_Crawl_lan3/data")
data = clean_data(data)
print(data)
