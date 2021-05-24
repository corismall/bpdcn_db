import datapane as dp
import seaborn as sns
import altair as alt 
import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect(dbname = 'BPDCN', user = 'postgres', password = 'ohgami')

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
#cur.execute('CREATE TABLE summary_data_schema.test (id serial PRIMARY KEY, num integer, data varchar);')
#cur.execute("INSERT INTO summary_data_schema.test (num, data) VALUES (%s, %s)", (100, "abc'def")) # Pass data to fill a query placeholders and let Psycopg perform the correct conversion (no more SQL injections!)
#cur.execute("\copy test(num,data) FROM '/Users/corinnsmall/Documents/BPDCN/spreadsheets' DELIMITER ',' CSV")
cur.execute("SELECT * FROM granular_case_data_schema.cd_markers;")

tuple_ = cur.fetchone()
print(tuple_)

conn.commit()
cur.close()
conn.close()

# Retrieve query results
records = cur.fetchall()
print(records)


#dp.ping()


#titanic = sns.load_dataset("titanic")

'''points = alt.Chart(records).mark_point().encode(
    x='age:Q',
    color='class:N',
    y='fare:Q',
).interactive().properties(width='container')

dp.Report(
  dp.Page(
    label="Titanic Dataset",
    blocks=["### Dataset", titanic]
  ),
  dp.Page(
    label="Titanic Plot",
    blocks=["### Plot", points]
  )
).publish(name='altair_example_pages')'''