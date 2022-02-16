alt.Chart(logins_sample).mark_line().encode(
    x='hours(login_date)',
    y='sum(full)',
    color='day(login_date)'
).add_selection(
    selector
)