select 
    dt_sgmt,
    count(DISTINCT seller_id)
from tb_seller_sgmt
GROUP BY dt_sgmt;

