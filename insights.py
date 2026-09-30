import pandas as pd
data = pd.read_csv('turf_bookings_synthetic.csv')

busiest_hour = data['hour'].value_counts().idxmax()
print("Busiest hour:", busiest_hour)

popular_sport = data['sport'].value_counts().idxmax()
print("Most popular sport:", popular_sport)

monthly_revenue = data.groupby('month')['total_amount'].sum()
highest_revenue_month = monthly_revenue.idxmax()
highest_month_revenue = monthly_revenue.max()
print("Highest revenue month:", highest_revenue_month)
print("Revenue:", highest_month_revenue)



booking_type_revenue = data.groupby('booking_type')['total_amount'].sum()
highest_revenue_type = booking_type_revenue.idxmax()
highest_type_revenue = booking_type_revenue.max()
print("Highest revenue booking type:", highest_revenue_type)
print("Revenue:", highest_type_revenue)



sport_revenue = data.groupby('sport')['total_amount'].sum()
highest_revenue_sport = sport_revenue.idxmax()
highest_sport_revenue = sport_revenue.max()
print("Highest revenue sport:", highest_revenue_sport)
print("Revenue:", highest_sport_revenue)



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
highest_cancellation_weather = (
    weather_analysis['cancellation_rate'].idxmax()
)
highest_cancellation_rate = (
    weather_analysis['cancellation_rate'].max()
)
print("Highest cancellation weather:", highest_cancellation_weather)
print("Cancellation rate:", round(highest_cancellation_rate, 2), "%")



day_bookings = data['day_of_week'].value_counts()
busiest_day = day_bookings.idxmax()
busiest_day_bookings = day_bookings.max()
print("Busiest day:", busiest_day)
print("Bookings:", busiest_day_bookings)



print("\n" + "=" * 55)
print("          TURF BOOKING BUSINESS INSIGHTS")
print("=" * 55)

print(f"\nBusiest hour: {busiest_hour}:00")
print(f"Most popular sport: {popular_sport}")
print(f"Highest revenue month: {highest_revenue_month}")
print(f"Highest revenue booking type: {highest_revenue_type}")
print(f"Highest revenue sport: {highest_revenue_sport}")
print(f"Highest cancellation weather: {highest_cancellation_weather}")
print(f"Busiest day: {busiest_day}")

print("\n" + "=" * 55)