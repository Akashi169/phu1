import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from csv_utils import delete_row_by_over_id

df_details = pd.read_csv("E:\\phu1\\Details.csv", sep=",", header = 0)
df_orders = pd.read_csv("E:\\phu1\\Orders.csv", sep=",", header = 0)
df_merged = pd.merge(df_details, df_orders, on = 'Order ID', how = 'left')

df_sorted = df_merged.sort_values(by="Order ID")
     


df_sorted.head(30)
df_merged.head(30)

df_sorted.to_csv("onlinesales_sorted.csv", index=False)
df_online_sales = pd.read_csv("onlinesales_sorted.csv")

df_online_sales

# Information general del DataFrame
print("\nInformation general del DataFrame:")
print(df_online_sales.info())

total_sales = df_online_sales['Amount'].sum()
total_profit = df_online_sales['Profit'].sum()
total_customers = df_online_sales['CustomerName'].nunique()
total_oders = len(df_online_sales)



fig, ax = plt.subplots(2,2, figsize = (12,8))
ax[0,0].bar('Total Sales' , total_sales, color = 'blue')
ax[0,0].text('Total Sales', total_sales, str(total_sales), ha = 'center', va = 'bottom',fontsize = 10 ) 
ax[0,0].set_ylabel('Amount')
ax[0,0].set_title('Total Sales')

ax[0,1].bar('Total profitability', total_profit, color = 'green')
ax[0,1].text('Total profitability', total_profit,str(total_profit), ha = 'center', va = 'bottom', fontsize = 10)
ax[0,1].set_ylabel('Amount')
ax[0,1].set_title('Total profitability')

ax[1,0].bar('Total customers', total_customers, color='orange')
ax[1,0].text('Total customers', total_customers, str(total_customers), ha='center', va='bottom')
ax[1,0].set_ylabel('Amount')  
ax[1,0].set_title('Total customers')

ax[1,1].bar('Completed Sales', total_oders, color = 'red' )
ax[1,1].text('Completed Sales', total_oders, str(total_oders), ha = 'center', va = 'bottom', fontsize = 10)
ax[1,1].set_ylabel('Amount')
ax[1,1].set_title('Completed Sales')

#Điều chỉnh khoảng cách giữa các biểu đồ và hiển thị chúng.
plt.tight_layout()
plt.show()
#Đếm số lượng giao dịch theo thành phố và phương thức thanh toán, sau đó tìm phương thức phổ biến nhất ở mỗi thành phố.
city_payment_counts = df_online_sales.groupby(['City', 'PaymentMode']).size().reset_index(name = 'Count')
city_most_common_payment = city_payment_counts.loc[city_payment_counts.groupby('City')['Count'].idxmax()]
print(city_most_common_payment)
#Lọc dữ liệu về giao dịch thuộc danh mục "Clothing" và đếm số lượng giao dịch theo từng phương thức thanh toán.
clothing_transactions = df_online_sales[df_online_sales['Category'] == 'Clothing']
payment_mode_counts = clothing_transactions['PaymentMode'].value_counts()
print(payment_mode_counts)

#Nhóm và vẽ biểu đồ đường về số lượng mua hàng theo danh mục và từng tháng trong năm.

sales_by_month_category = df_online_sales.groupby([df_online_sales['Order Date'].dt.month, 'Category']).size().unstack()

sales_by_month_category.plot(kind='line', marker='o', figsize=(10, 6))
plt.title('Number of Purchases by Category and Months')
plt.xlabel('Months')
plt.ylabel('Number of Purchases ')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.legend(title='Categoría')
plt.grid(True)
plt.show()






while True:
    print('1.Delete row in Orders.csv and onlinesales_sorted.csv by Order ID')
    print('2.Delete row in Details.csv and onlinesales_sorted.csv by Order ID')
    print('Enter selection')
    selection = int(input())
    order_id = input("Enter Order ID")
    if selection == 1:
        df_orders = delete_row_by_over_id('Orders.csv',order_id)
        df_online_sales = delete_row_by_over_id('onlinesales_sorted.csv',order_id)
    elif selection == 2:
        df_details = delete_row_by_over_id('Details.csv',order_id)
        df_online_sales = delete_row_by_over_id('onlinesales_sorted.csv',order_id)
    else:
        print("Invalid selection. Please select 1 or 2.")
    







