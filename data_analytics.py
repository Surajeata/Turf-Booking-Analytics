import pandas as pd 
data = pd.read_csv('turf_bookings_synthetic.csv')
print(data.shape)
data.info()
print(data.isnull().sum())
print(data.duplicated().sum())

print("\nBookings with missing ratings ")
missing_rating = data[data['customer_rating'].isna()]
print(missing_rating[['booking_type', 'booking_status', 'total_amount' , 'booking_id' ]])

print("\nMissing ratings by booking status ")
print(missing_rating['booking_status'].value_counts())

print("\nMissing rating by booking_status and total_amount ")
print(missing_rating.groupby(['booking_status', 'total_amount']).size())

print("\n REVENUE VALIDATION ")
data['calculated_amount'] = data['duration_hours'] * data['hourly_rate']
data['amount_difference'] = data['total_amount'] - data['calculated_amount']
print(data['amount_difference'].value_counts().head(10))

print("\n COMPLETED BOOKING REVENUE CHECK ")
completed = data[data['booking_status'] == 'Completed'].copy()
completed['expected_amount'] = (
    completed['duration_hours'] * completed['hourly_rate']
)
print("Completed bookings:", len(completed))

print(
    "Incorrect amounts:",
    (completed['total_amount'] != completed['expected_amount']).sum()
)

print("\nUnique values")
print(data['sport'].value_counts())
print(data['booking_type'].value_counts())
print(data['payment_method'].value_counts())
print(data['booking_status'].value_counts())
print(data['weather'].value_counts())
print(data['day_of_week'].value_counts())
print(data['month'].value_counts())

print("\nNumerical data summary ")
print(data[['hour','duration_hours','players','hourly_rate','total_amount','customer_rating']].describe())

print("\nPLAYERS AND HOURLY RATE ")
print(
    data[
        ['players', 'hourly_rate']
    ].describe()
)

print("\n RANGE CHECK ")
print("Minimum players:", data['players'].min())
print("Maximum players:", data['players'].max())

print("Minimum hourly rate:", data['hourly_rate'].min())
print("Maximum hourly rate:", data['hourly_rate'].max())

print("Minimum hour:", data['hour'].min())
print("Maximum hour:", data['hour'].max())

print("Minimum duration:", data['duration_hours'].min())
print("Maximum duration:", data['duration_hours'].max())

print("Minimum rating:", data['customer_rating'].min())
print("Maximum rating:", data['customer_rating'].max())



print("\n KEY BUSINESS KPIs ")


total_bookings = len(data)


completed_bookings = (
    data['booking_status'] == 'Completed'
).sum()


cancelled_bookings = (
    data['booking_status'] == 'Cancelled'
).sum()


no_show_bookings = (
    data['booking_status'] == 'No-show'
).sum()


total_revenue = data['total_amount'].sum()


average_booking_value = (
    data.loc[
        data['booking_status'] == 'Completed',
        'total_amount'
    ].mean()
)

average_rating = data['customer_rating'].mean()

cancellation_rate = (
    cancelled_bookings / total_bookings
) * 100

no_show_rate = (
    no_show_bookings / total_bookings
) * 100


print("Total bookings:", total_bookings)
print("Completed bookings:", completed_bookings)
print("Cancelled bookings:", cancelled_bookings)
print("No-show bookings:", no_show_bookings)
print("Total revenue: ₹", total_revenue)
print(
    "Average completed booking value: ₹",
    round(average_booking_value, 2)
)
print(
    "Average customer rating:",
    round(average_rating, 2)
)
print(
    "Cancellation rate:",
    round(cancellation_rate, 2),
    "%"
)
print(
    "No-show rate:",
    round(no_show_rate, 2),
    "%"
)


print("\n SPORT-WISE ANALYSIS ")

sport_analysis = data.groupby('sport').agg(
    bookings=('booking_id', 'count'),
    revenue=('total_amount', 'sum'),
    average_booking_value=('total_amount', 'mean'),
    average_rating=('customer_rating', 'mean')
)

print(sport_analysis)


print("\nHOURLY BOOKING ANALYSIS ")

hourly_analysis = data.groupby('hour').agg(
    bookings=('booking_id', 'count'),
    revenue=('total_amount', 'sum'),
    average_booking_value=('total_amount', 'mean')
)

print(hourly_analysis)



print("\n BOOKING TYPE ANALYSIS ")

booking_type_analysis = data.groupby('booking_type').agg(
    bookings=('booking_id', 'count'),
    revenue=('total_amount', 'sum'),
    average_booking_value=('total_amount', 'mean'),
    average_rating=('customer_rating', 'mean')
)

print(booking_type_analysis)



print("\n COMPLETED BOOKING TYPE ANALYSIS ")
completed_booking_type = (
    data[data['booking_status'] == 'Completed']
    .groupby('booking_type')
    .agg(
        completed_bookings=('booking_id', 'count'),
        revenue=('total_amount', 'sum'),
        average_booking_value=('total_amount', 'mean'),
        average_rating=('customer_rating', 'mean')
    )
)
print(completed_booking_type)


print("\n===== CANCELLATION RATE BY BOOKING TYPE =====")
cancellation_by_type = (
    data.groupby('booking_type')
    .agg(
        total_bookings=('booking_id', 'count'),
        cancelled_bookings=(
            'booking_status',
            lambda x: (x == 'Cancelled').sum()
        )
    )
)
cancellation_by_type['cancellation_rate'] = (
    cancellation_by_type['cancelled_bookings']
    / cancellation_by_type['total_bookings']
    * 100
)
print(cancellation_by_type)



print("\n BOOKING TYPE STATUS ANALYSIS ")
booking_status_by_type = (
    data.groupby(['booking_type', 'booking_status'])
    .size()
    .unstack(fill_value=0)
)
print(booking_status_by_type)


print("\n WEATHER ANALYSIS ")
weather_analysis = data.groupby('weather').agg(
    bookings=('booking_id', 'count'),
    revenue=('total_amount', 'sum'),
    average_booking_value=('total_amount', 'mean'),
    average_rating=('customer_rating', 'mean')
)
print(weather_analysis)


print("\n CANCELLATION RATE BY WEATHER ")

cancellation_by_weather = (
    data.groupby('weather')
    .agg(
        total_bookings=('booking_id', 'count'),

        cancelled_bookings=(
            'booking_status',
            lambda x: (x == 'Cancelled').sum()
        ),

        no_show_bookings=(
            'booking_status',
            lambda x: (x == 'No-show').sum()
        )
    )
)

cancellation_by_weather['cancellation_rate'] = (
    cancellation_by_weather['cancelled_bookings']
    / cancellation_by_weather['total_bookings']
    * 100
)

cancellation_by_weather['no_show_rate'] = (
    cancellation_by_weather['no_show_bookings']
    / cancellation_by_weather['total_bookings']
    * 100
)

print(cancellation_by_weather)



print("\n DAY-OF-WEEK ANALYSIS ")
day_analysis = data.groupby('day_of_week').agg(
    bookings=('booking_id', 'count'),
    revenue=('total_amount', 'sum'),
    average_booking_value=('total_amount', 'mean'),
    average_rating=('customer_rating', 'mean')
)
print(day_analysis)



print("\n SPORT BY DAY OF WEEK ")
sport_day_analysis = (
    data.groupby(['day_of_week', 'sport'])
    .agg(
        bookings=('booking_id', 'count'),
        revenue=('total_amount', 'sum')
    )
)
print(sport_day_analysis)



print("\n SPORT BY HOUR ")
sport_hour_analysis = (
    data.groupby(['hour', 'sport'])
    .agg(
        bookings=('booking_id', 'count'),
        revenue=('total_amount', 'sum'),
        average_booking_value=('total_amount', 'mean')
    )
)
print(sport_hour_analysis)


print("\n MONTH-WISE ANALYSIS ")
month_analysis = data.groupby('month').agg(
    bookings=('booking_id', 'count'),
    revenue=('total_amount', 'sum'),
    average_booking_value=('total_amount', 'mean'),
    average_rating=('customer_rating', 'mean')
)
print(month_analysis)



print("\n PLAYERS ANALYSIS ")
players_analysis = data.groupby('players').agg(
    bookings=('booking_id', 'count'),
    revenue=('total_amount', 'sum'),
    average_booking_value=('total_amount', 'mean'),
    average_duration=('duration_hours', 'mean')
)
print(players_analysis)



print("\n DURATION ANALYSIS ")
duration_analysis = data.groupby('duration_hours').agg(
    bookings=('booking_id', 'count'),
    revenue=('total_amount', 'sum'),
    average_booking_value=('total_amount', 'mean'),
    average_hourly_rate=('hourly_rate', 'mean'),
    average_players=('players', 'mean')
)
print(duration_analysis)



print("\n HOURLY RATE ANALYSIS ")
rate_analysis = data.groupby('hourly_rate').agg(
    bookings=('booking_id', 'count'),
    revenue=('total_amount', 'sum'),
    average_booking_value=('total_amount', 'mean'),
    average_duration=('duration_hours', 'mean'),
    average_players=('players', 'mean')
)
print(rate_analysis)





