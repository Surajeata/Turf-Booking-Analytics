import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('turf_bookings_synthetic.csv')
sport_bookings = data['sport'].value_counts()
plt.figure(figsize=(8, 5))
sport_bookings.plot(kind='bar')
plt.title('Bookings by Sport')
plt.xlabel('Sport')
plt.ylabel('Number of Bookings')
plt.tight_layout()
plt.show()



hour_bookings = data['hour'].value_counts().sort_index()
plt.figure(figsize=(10, 5))
hour_bookings.plot(kind='bar')
plt.title('Bookings by Hour')
plt.xlabel('Hour')
plt.ylabel('Number of Bookings')
plt.tight_layout()
plt.show()



booking_type_revenue = (
    data.groupby('booking_type')['total_amount']
    .sum()
    .sort_values(ascending=False)
)
plt.figure(figsize=(8, 5))
booking_type_revenue.plot(kind='bar')
plt.title('Revenue by Booking Type')
plt.xlabel('Booking Type')
plt.ylabel('Revenue (₹)')
plt.tight_layout()
plt.show()




weather_analysis = data.groupby('weather').agg(
    total_bookings=('booking_id', 'count'),
    cancelled_bookings=(
        'booking_status',
        lambda x: (x == 'Cancelled').sum()
    )
)
weather_analysis['cancellation_rate'] = (
    weather_analysis['cancelled_bookings']
    / weather_analysis['total_bookings']
    * 100
)
plt.figure(figsize=(8, 5))
weather_analysis['cancellation_rate'].plot(kind='bar')
plt.title('Cancellation Rate by Weather')
plt.xlabel('Weather')
plt.ylabel('Cancellation Rate (%)')
plt.tight_layout()
plt.show()




month_order = [
    'January', 'February', 'March', 'April',
    'May', 'June', 'July', 'August',
    'September', 'October', 'November', 'December'
]
monthly_revenue = (
    data.groupby('month')['total_amount']
    .sum()
    .reindex(month_order)
)
plt.figure(figsize=(10, 5))
monthly_revenue.plot(kind='bar')
plt.title('Monthly Revenue')
plt.xlabel('Month')
plt.ylabel('Revenue (₹)')
plt.tight_layout()
plt.show()





sport_hour = (
    data.groupby(['hour', 'sport'])
    .size()
    .unstack(fill_value=0)
)
plt.figure(figsize=(12, 6))
sport_hour.plot(kind='bar', figsize=(12, 6))
plt.title('Bookings by Sport and Hour')
plt.xlabel('Hour')
plt.ylabel('Number of Bookings')
plt.tight_layout()
plt.show()





monthly_analysis = data.groupby('month').agg(
    bookings=('booking_id', 'count'),
    revenue=('total_amount', 'sum')
).reindex(month_order)

print("\nMONTHLY BOOKINGS VS REVENUE")
print(monthly_analysis)
monthly_analysis.plot(
    kind='bar',
    figsize=(12, 6),
    secondary_y='revenue'
)
plt.title('Monthly Bookings vs Revenue')
plt.xlabel('Month')
plt.ylabel('Number of Bookings')
plt.tight_layout()
plt.show()