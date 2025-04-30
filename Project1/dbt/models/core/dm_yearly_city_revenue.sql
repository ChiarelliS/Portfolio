{{ config(materialized='table') }}

with companydata as (
    select * from {{ ref('stg_company_data') }}
),
revenue_data as (
    select * from {{ ref('stg_revenue_data') }}
),
joined_data as (
    select
        c.company_name,
        c.cik_company_id,
        c.company_address_city as revenue_city,
        r.total_revenue,
         
    from revenue_data r
    inner join companydata c
        on r.cik_company_id = c.cik_company_id
)

select 
    revenue_city,
    sum(total_revenue) as revenue_total,

from joined_data
group by revenue_city
