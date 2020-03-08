───────────
{% if reserved_books.is_prepared %}􀁹{% else %}􀂐{% endif %}{{ user.disp_name }}({{ user.id }})
───────────
􀁡予約状況􀁡
{%- if reserved_books.len > 0 %}
　　　対象：{{ reserved_books.len }}冊
───────────
{%- else %}
　　　対象：0冊
───────────
{% endif -%}
{%- for book in reserved_books.list %}
􀁬{{ book.title }}
{% if book.is_prepared == True %}􀁠{% elif book.is_dereverd == True %}􀁉{% else %}■{% endif %}状況：{{ book.status }}
■受取館：{{ book.receive_lib }}
■取置期限日：{{ book.torioki_date }}
■順位：{% if book.is_prepared == True %}-{% elif book.is_dereverd == True %}-{% else %}{{ book.order }}{% endif %}
{% endfor -%}