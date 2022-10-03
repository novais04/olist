select t1.*,
    CASE WHEN   pct_receita <= 0.5 AND pct_freq <= 0.5 then "BAIXO VALOR"
    WHEN        pct_receita > 0.5  AND pct_freq <= 0.5 then "ALTO VALOR"
    WHEN        pct_receita <= 0.5 AND pct_freq > 0.5  then "ALTA FREQ"
    WHEN        pct_receita < 0.9  OR  pct_freq < 0.9  then "PRODUTIVO"
    ELSE        "SUPER PRODUTIVO"
    END AS semento_valor_freq
from
(
    select t1.*,
        percent_rank() OVER (order by receita_total asc) as pct_receita, 
        PERCENT_rank() over (order by qtde_pedidos asc) as pct_freq

    from(

        select
            t2.seller_id,
            sum(t2.price) as receita_total,
            count(DISTINCT t1.order_id) as qtde_pedidos,
            count(t2.product_id) as qtde_produtos,
            count(DISTINCT t2.product_id) as qtde_Uniq_produtos,
            min(julianday('2018-06-01') - julianday(t1.order_approved_at)) as qt_dias_ult_venda,
            max(cast(julianday('2018-06-01')- julianday(t3.dt_inicio) as int)) as qtde_dias_base

        from tb_orders as t1
        left join tb_order_items as t2
        on t1.order_id = t2.order_id

        left join ( 
            select 
                t2.seller_id,
                min( date(t1.order_approved_at)) as dt_inicio
            from tb_orders as t1
            left join tb_order_items as t2
            on t1.order_id = t2.order_id

            group by t2.seller_id 
        ) as t3
        on t2.seller_id = t3.seller_id

        where t1.order_approved_at BETWEEN '2017-06-01' and '2018-06-01'

        group by t2.seller_id
    ) as t1
) as t1



