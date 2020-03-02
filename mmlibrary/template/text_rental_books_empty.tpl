{%- if header -%}􀁢貸出状況􀁢

{% endif -%}
{%- if rental_books.filter_type == "rental_normal" -%}
{{ user.disp_name }}({{ user.id }})の貸出本はありません。
{%- elif rental_books.filter_type == "rental_expired" -%}
{{ user.disp_name }}({{ user.id }})の貸出本で延滞している本はありません。
{%- elif rental_books.filter_type == "rental_expire" -%}
{{ user.disp_name }}({{ user.id }})の貸出本で{{ rental_books.filter_param["xdays"] }}日以内に延滞する本はありません。
{%- endif %}