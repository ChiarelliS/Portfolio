## Data Transformation

To prepare the data loaded in the Cloud Storage for analytics, I queried the data using dbt. 


I first created two staging views, cleaning the data, adjusting the field names to make them more insightful.


I then created a core model to create a dimensional table, that contains informations about the sum of revenue per U.S. city. This could be insightful for further analysis.

Here the DAG of my models.

![alt text](dbt-dag.png "Title")
