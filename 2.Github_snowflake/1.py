snowpark_df = session.table("COVID19_RECORDS")

print(type(snowpark_df) # snowflake.snowpark.table.Table
print(f"Size of the table object: {(sys.getsizeof(snowpark_df)/1e6)} MB")
#'Size of the table object: 4.8e-05 MB'
