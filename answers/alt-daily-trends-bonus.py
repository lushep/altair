selector = alt.selection_single(encodings=['x', 'color'])

alt.Chart(
    logins_sample
).mark_line(
    strokeWidth=3
).encode(
    x=alt.X('hours(login_date):T', axis=alt.Axis(title='Hours of the Day')),
    y=alt.Y('sum(full)', axis=alt.Axis(title='Total Logins')),
    color=alt.condition(selector, 'day(login_date):O', alt.value('lightgray'))
).transform_filter(
    alt.FieldOneOfPredicate(field='login_date', timeUnit='day', oneOf=['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])
).properties(
    height=300,
    width=600,
    title='Demand on logins over the Day'
).add_selection(
    selector
).interactive()