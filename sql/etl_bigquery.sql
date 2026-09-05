-- ============================================================
1/ dim_customers:
select *
lpad(cast(customer_zip_code_prefix as string) , 5 , '0') as zip_code_prefix
from jda-k1.BVA_BIGPROJECT_2.olist_customers_dataset
-- ============================================================
2/ dim_products
select *except (product_category_name_english)
from (select product_id
  , a.product_category_name
  , case 
      when a.product_category_name = "Unknown" then coalesce (b.product_category_name_english, "Unknown")
      when a.product_category_name = "pc_gamer" then coalesce (b.product_category_name_english, "computer game")
      when a.product_category_name = "portateis_cozinha_e_preparadores_de_alimentos" then coalesce (b.product_category_name_english, "kitchen appliances and food prep")
      else a.product_category_name 
      end as product_category_name_english as english_name_new_version
  , b.product_category_name_english
  , product_name_lenght
  , product_description_lenght
  , product_photos_qty
  , product_weight_g
  , product_length_cm
  , product_height_cm
  , product_width_cm
from jda-k1.BVA_BIGPROJECT_2.Dim_Products_Olist as a
left join jda-k1.BVA_BIGPROJECT_2.product_category_name_translation as b
on a.product_category_name = b.product_category_name)
-- ============================================================
3/ dim_sellers
select *
lpad(cast(customer_zip_code_prefix as string) , 5 , '0') as zip_code_prefix
from jda-k1.BVA_BIGPROJECT_2.olist_sellers_dataset
-- ============================================================
4/ dim_geolocation
create or replace table jda-k1.BVA_BIGPROJECT_2.olist_geolocation_dataset_step1 as
select  *
lpad(cast(customer_zip_code_prefix as string) , 5 , '0') as newzip
from jda-k1.BVA_BIGPROJECT_2.olist_geolocation_dataset
-- ============================================================
select *except(freq,rn)
from(select new_zip 
  , count(*) as freq
  , avg(geolocation_lat) as geo_lat
  , avg(geolocation_lng) as geo_lng
  , city_norm 
  , geolocation_state
  , row_number() over(partition by new_zip order by count(*) desc ) as rn
from jda-k1.BVA_BIGPROJECT_2.olist_geolocation_dataset_step1 
where geo_lat between -33 and 5 
and geo_lng between -75 and -35
group by 1,5,6
qualify rn=1)
-- ============================================================
5/ dim_products_translation
Clean
-- ============================================================
6/ fact_orders
select *
  , case
      when order_delivered_customer_date is not null then date_diff(order_delivered_customer_date,order_purchase_timestamp, day) 
      else 0
      end as Total_delivered_day
  , case
      when order_delivered_customer_date is not null and order_delivered_customer_date > order_estimated_delivery_date  then date_diff(order_delivered_customer_date,order_estimated_delivery_date,day)
      else 0
    end as delivery_delay_days
from(select order_id
  , customer_id
  , order_status
  , safe_cast(order_purchase_timestamp as datetime) as order_purchase_timestamp
  , safe_cast(order_approved_at as datetime) as order_approved_at
  , safe_cast(order_delivered_carrier_date as datetime) as order_delivered_carrier_date
  , safe_cast(order_delivered_customer_date as datetime) as order_delivered_customer_date
  , safe_cast(order_estimated_delivery_date as datetime) as order_estimated_delivery_date
  , case
      when order_delivered_customer_date >  order_estimated_delivery_date then "Yes"
      else "No"
    end as is_late
  , case
      when order_status = "delivered" and order_delivered_customer_date is null then 'Yes'
      else 'No'
    end as data_abnormal
from jda-k1.BVA_BIGPROJECT_2.olist_orders_dataset)
-- ============================================================
7/ fact_order_items
select *
safe_cast(shipping_limit_date as date) as shipping_limit_date
from jda-k1.BVA_BIGPROJECT_2.olist_order_items_dataset
-- ============================================================
8/ fact_payments
select *
from jda-k1.BVA_BIGPROJECT_2.olist_order_payments_dataset
where payment_type not like " not_defined"
=> loại bỏ 3 dòng not_define vì tham số quá nhỏ, không ảnh hưởng đến bộ dữ liệu
-- ============================================================
9/ fact_reviews
Sử dụng hàm coalesce để xoá các giá trị null tại 2 cột comment để sửa thành unknown

create or replace table jda-k1.BVA_BIGPROJECT_2.done_olist_order_reviews_dataset as
select *
  , coalesce(review_comment_title, 'unknown') as review_comment_title
  , coalesce(review_comment_message, 'unknown') as review_comment_message
from jda-k1.BVA_BIGPROJECT_olist_order_reviews_dataset
-- ============================================================
Xoá các duplicate order_id chỉ giữ lại review mới nhất:
select *except(rn)
from (
select * 
  , row_number()over(partition by order_id order by review_answer_timestamp desc) as rn
from jda-k1.BVA_BIGPROJECT_2.done_olist_order_reviews_dataset)
where rn =1
