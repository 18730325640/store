date1="1号"
clothing1="羽绒服"
price1=253.6
stock1=500
sales1=10
date2="2号"
clothing2="牛仔裤"
price2=86.3
stock2=600
sales2=60
date3="3号"
clothing3="风衣"
price3=96.8
stock3=335
sales3=43
date4="4号"
clothing4="皮草"
price4=135.9
stock4=855
sales4=63
date5="5号"
clothing5="T恤"
price5=65.8
stock5=632
sales5=63
date6="6号"
clothing6="衬衫"
price6=49.3
stock6=562
sales6=120
date7="7号"
sales7=72
date8="8号"
sales8=69
date9="9号"
sales9=35
date10="10号"
sales10=140
date11="11号"
sales11=90
date12="12号"
sales12=24
date13="13号"
sales13=45
date14="14号"
sales14=25
date15="15号"
sales15=60
date16="16号"
sales16=129
date17="17号"
sales17=10
date18="18号"
sales18=43
date19="19号"
sales19=63
date20="20号"
sales20=60
date21="21号"
sales21=63
date22="22号"
sales22=60
date23="23号"
sales23=58
date24="24号"
sales24=140
date25="25号"
sales25=48
date26="26号"
sales26=43
date27="27号"
sales27=57
date28="28号"
sales28=10
date29="29号"
sales29=63
date30="30号"
sales30=78
A=(price1*sales1+price2*sales2+price3*sales3+price4*sales4+price5*sales5+price6*sales6+price2*sales7+price1*sales8+price2*sales9+price1*sales10+price2*sales11+price4*sales12+price5*sales13+price3*sales14+price2*sales15+price5*sales16+price1*sales17+price3*sales18+price5*sales19+price2*sales20+price4*sales21+price3*sales22+price5*sales23+price2*sales24+price5*sales25+price3*sales26+price4*sales27+price3*sales30+price1*sales28+price5*sales29)
yuzong=price1*(sales1+sales8+sales10+sales17+sales28)
niuzong=price2*(sales2+sales7+sales9+sales11+sales15+sales20+sales24)
fengzong=price3*(sales3+sales14+sales18+sales22+sales26+sales30)
pizong=price4*(sales4+sales12+sales21+sales27)
Tzong=price5*(sales5+sales13+sales16+sales19+sales23+sales25+sales29)
chenzong=price6*sales6
print("日期\t\t服装名称\t\t价格/件\t\t库存数量\t\t销售量/每日")
print(date1,"\t",clothing1,"\t\t",price1,"\t\t",stock1,"\t\t",sales1)
print(date2,"\t",clothing2,"\t\t",price2,"\t\t",stock2,"\t\t",sales2)
print(date3,"\t",clothing3,"\t\t",price3,"\t\t",stock3,"\t\t",sales3)
print(date4,"\t",clothing4,"\t\t",price4,"\t\t",stock4,"\t\t",sales4)
print(date5,"\t",clothing5,"\t\t",price5,"\t\t",stock5,"\t\t",sales5)
print(date6,"\t",clothing6,"\t\t",price6,"\t\t",stock6,"\t\t",sales6)
print(date7,"\t",clothing2,"\t\t",price2,"\t\t",stock2,"\t\t",sales7)
print(date8,"\t",clothing1,"\t\t",price1,"\t\t",stock1,"\t\t",sales8)
print(date9,"\t",clothing2,"\t\t",price2,"\t\t",stock2,"\t\t",sales9)
print(date10,"\t",clothing1,"\t\t",price1,"\t\t",stock1,"\t\t",sales10)
print(date11,"\t",clothing2,"\t\t",price2,"\t\t",stock2,"\t\t",sales11)
print(date12,"\t",clothing4,"\t\t",price4,"\t\t",stock4,"\t\t",sales12)
print(date13,"\t",clothing5,"\t\t",price5,"\t\t",stock5,"\t\t",sales13)
print(date14,"\t",clothing3,"\t\t",price3,"\t\t",stock3,"\t\t",sales14)
print(date15,"\t",clothing2,"\t\t",price2,"\t\t",stock2,"\t\t",sales15)
print(date16,"\t",clothing5,"\t\t",price5,"\t\t",stock5,"\t\t",sales16)
print(date17,"\t",clothing1,"\t\t",price1,"\t\t",stock1,"\t\t",sales17)
print(date18,"\t",clothing3,"\t\t",price3,"\t\t",stock3,"\t\t",sales18)
print(date19,"\t",clothing5,"\t\t",price5,"\t\t",stock5,"\t\t",sales19)
print(date20,"\t",clothing2,"\t\t",price2,"\t\t",stock2,"\t\t",sales20)
print(date21,"\t",clothing4,"\t\t",price4,"\t\t",stock4,"\t\t",sales21)
print(date22,"\t",clothing3,"\t\t",price3,"\t\t",stock3,"\t\t",sales22)
print(date23,"\t",clothing5,"\t\t",price5,"\t\t",stock5,"\t\t",sales23)
print(date24,"\t",clothing2,"\t\t",price2,"\t\t",stock2,"\t\t",sales24)
print(date25,"\t",clothing5,"\t\t",price5,"\t\t",stock5,"\t\t",sales25)
print(date26,"\t",clothing3,"\t\t",price3,"\t\t",stock3,"\t\t",sales26)
print(date27,"\t",clothing4,"\t\t",price4,"\t\t",stock4,"\t\t",sales27)
print(date28,"\t",clothing1,"\t\t",price1,"\t\t",stock1,"\t\t",sales28)
print(date29,"\t",clothing5,"\t\t",price5,"\t\t",stock5,"\t\t",sales29)
print(date30,"\t",clothing3,"\t\t",price3,"\t\t",stock3,"\t\t",sales30)
print("总金额:￥%.2f"%A)
print("羽绒服销售额占比:%.2f%%"%(yuzong/A))
print("牛仔裤销售额占比:%.2f%%"%(niuzong/A))
print("风衣销售额占比:%.2f%%"%(fengzong/A))
print("皮草销售额占比:%.2f%%"%(pizong/A))
print("T恤销售额占比:%.2f%%"%(Tzong/A))
print("衬衫销售额占比:%.2f%%"%(chenzong/A))