{%- if header -%}􀁢貸出状況􀁢

{% endif -%}
{%- if rental_books.filter_type == "rental_normal" -%}
貸出本はありません。
{%- elif rental_books.filter_type == "rental_expired" -%}
貸出本で延滞している本はありません。
{%- elif rental_books.filter_type == "rental_expire" -%}
貸出本で{{ rental_books.filter_param["xdays"] }}日以内に延滞する本はありません。
{%- endif %}