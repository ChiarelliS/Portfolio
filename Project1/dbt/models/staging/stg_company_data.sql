{{
    config(
        materialized='view'
    )
}}

with companydata  as 
(
  select *,
    row_number() over(partition by cik, year) as rn
  from {{ source('staging','sec_company_data_ext') }}
  where cik is not null 
)
select
    -- identifiers
    {{ dbt_utils.generate_surrogate_key('cik') }} as company_id,

    -- company details
    {{ dbt.safe_cast("name", api.Column.translate_type("string")) }} as company_name,
    {{ dbt.safe_cast("ticker", api.Column.translate_type("string")) }} as company_name_shorter,
    {{ dbt.safe_cast("street1", api.Column.translate_type("string")) }} as company_address_main_street,
    {{ dbt.safe_cast("street2", api.Column.translate_type("string")) }} as company_address_second_street,
    {{ dbt.safe_cast("city", api.Column.translate_type("string")) }} as company_address_city,
    {{ dbt.safe_cast("zipCode", api.Column.translate_type("string")) }} as company_address_zipcode,
    {{ dbt.safe_cast("country", api.Column.translate_type("string")) }} as company_address_country,
    {{ dbt.safe_cast("street1", api.Column.translate_type("string")) }} as company_address_main_street,
    {{ dbt.safe_cast("isForeignLocation", api.Column.translate_type("string")) }} as is_company_not_from_usa,

from companydata
where rn = 1


-- dbt build --select <model_name> --vars '{'is_test_run': 'false'}'
{% if var('is_test_run', default=true) %}

  limit 100

{% endif %}