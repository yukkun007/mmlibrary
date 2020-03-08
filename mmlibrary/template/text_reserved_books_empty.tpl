───────────
{% if reserved_books.is_prepared %}􀁹{% else %}􀂐{% endif %}{{ user.disp_name }}({{ user.id }})
───────────
􀁡予約状況􀁡
{% if reserved_books.filter_type == "reserved_normal" -%}
予約本はありません。
{%- elif reserved_books.filter_type == "reserved_prepared" -%}
予約本で到着している本はありません。
{%- endif -%}