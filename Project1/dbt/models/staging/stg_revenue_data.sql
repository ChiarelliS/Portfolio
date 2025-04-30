{{
    config(
        materialized='view'
    )
}}

with revenue_data  as 
(
  select *,
    row_number() over(partition by cik, year) as rn
  from {{ source('staging','sec_company_data_ext') }}
  where cik is not null 
)
select
    -- company details
    {{ dbt.safe_cast("cik", api.Column.translate_type("string")) }} as cik_company_id,
    {{ dbt.safe_cast("form", api.Column.translate_type("string")) }} as revenue_form,
    {{ dbt.safe_cast("frame", api.Column.translate_type("string")) }} as revenue_form_frame,
    {{ dbt.safe_cast("val", api.Column.translate_type("integer")) }} as total_revenue,
    {{ dbt.safe_cast("unit", api.Column.translate_type("string")) }} as revenue_unit_of_currency,
    {{ dbt.safe_cast("year", api.Column.translate_type("integer")) }} as revenue_year,

from revenue_data
where rn = 1


-- dbt build --select <model_name> --vars '{'is_test_run': 'false'}'
{% if var('is_test_run', default=true) %}

  limit 100

{% endif %}