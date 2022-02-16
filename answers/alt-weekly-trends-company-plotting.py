alt.Chart(logins_sample).mark_bar().encode(
    x='day(login_date):O',
    y='sum(full)',
    color='company'
).properties(
    width=800,
    height=300
)