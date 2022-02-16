selector = alt.selection_single(encodings=['x', 'color'])

alt.Chart(logins_sample).mark_bar().encode(
    x='day(login_date):O',
    y='sum(full)',
    color=alt.condition(selector, 'company', alt.value('lightgray'))
).properties(
    width=800,
    height=300
).add_selection(
    selector
)