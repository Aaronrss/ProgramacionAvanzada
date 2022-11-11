import plotly.express as px

df = px.data.iris()
print(df.head())
print(df['species'].unique())

fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")

fig.show()

fig2 = px.scatter(df, x="sepal_width", y="sepal_length", color="species", marginal_y="violin", marginal_x="box", trendline="ols")

fig2.show()

df['error'] = df['sepal_length'] / 100

fig3=px.scatter(df, x="sepal_width", y="sepal_length", color="species", error_y="error", error_x="error")

fig3.show()

df = px.data.tips()
df.head()

fig4 = px.bar(df, x="sex", y="total_bill", color="smoker", barmode="group")
fig4.show()

car_order = {
    "Day": ["Thur", "Fri", "Sat", "Sun"],
    "Time": ["Lunch", "Dinner"]
}

fig5 = px.bar(df, x="sex", y="total_bill", color="smoker", barmode="group", facet_col="time", facet_row="day", category_orders=car_order)

fig5.show()


df = px.data.iris()
features = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
fig6 = px.scatter_matrix(df, dimensions=features, color="species")
fig6.show()

df = px.data.gapminder()
df.query("year==2007").head() # pandas query

fig7 = px.scatter(df.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent", hover_name="country", log_x=True, size_max=60)

fig7.show()


df['year'].unique()
fig8 = px.scatter(df, x="gdpPercap", y="lifeExp", size="pop",animation_frame="year", animation_group="country", facet_col="continent", color="continent", hover_name="country", log_x=True, size_max=45, range_x=[100,100000], range_y=[25,90])


fig8.show()