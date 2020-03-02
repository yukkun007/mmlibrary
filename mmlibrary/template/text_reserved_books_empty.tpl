{%- if header -%}􀁡予約状況􀁡

{% endif -%}
{%- if reserved_books.filter_type == "reserved_normal" -%}
{{ user.disp_name }}({{ user.id }})の予約本はありません。
{%- elif reserved_books.filter_type == "reserved_prepared" -%}
{{ user.disp_name }}({{ user.id }})の予約本で到着している本はありません。
{%- endif %}