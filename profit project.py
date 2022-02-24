from tkinter import *
import random

root=Tk()

root.title("random 5 letters")
root.geometry("500x510")
root.configure(background="yellow")
label_month=Label(root)
label_profits=Label(root)
label_max_profit=Label(root)
label_min_profit=Label(root)

month = (" January "," Febuary "," March "," April "," May "," June "," July "," August "," September "," October "," November "," December ",)


profits = ( 912 , 40 , 73 , 6 , 4 , 5 , 65 , 2 , 10 , 31 , 30 , 22)
label_month["text"]="months:"+str(month)
label_profits["text"]="profits:"+str(profits)


def maxprofit():
    max_profit = max(profits)
    max_profit_index = profits.index(max_profit)
    max_profit_month = month[max_profit_index]
    label_max_profit["text"]= "maximum profit of"+str(max_profit)+"Was given in the month of"+str(max_profit_month)
def minprofit():
    min_profit = min(profits)
    min_profit_index = profits.index(min_profit)
    min_profit_month = month[min_profit_index]
    label_min_profit["text"]= "minimum profit of"+str(min_profit)+"Was given in the month of"+str(min_profit_month)






btn_min = Button(root, text = "Profit button" , command = minprofit , bg = "powderblue" , fg = "azure3")
btn_max = Button(root, text = "Profit button" , command = maxprofit , bg = "tan" , fg = "salmon")


btn_min.place(relx=0.5,rely= 0.4, anchor = CENTER )
btn_max.place(relx=0.5,rely= 0.1, anchor = CENTER )
label_month.place(relx=0.5,rely= 0.2, anchor = CENTER )
label_profits.place(relx=0.5,rely= 0.3, anchor = CENTER )
label_max_profit.place(relx=0.5,rely=0.6, anchor = CENTER )
label_min_profit.place(relx=0.5,rely=0.7, anchor = CENTER )

root.mainloop()