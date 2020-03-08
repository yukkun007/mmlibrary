───────────
􀂏{{ user.disp_name }}({{ user.id }})
───────────
􀁢貸出状況􀁢
{%- if rental_books.len > 0 -%}
{%- if rental_books.filter_type == "rental_normal" %}
　　　貸出：{{ rental_books.len }}冊
{%- elif rental_books.filter_type == "rental_expired" %}
　　　延滞：{{ rental_books.len }}冊
{%- elif rental_books.filter_type == "rental_expire" %}
　{{ rental_books.filter_param["xdays"] }}日以内で延滞：{{ rental_books.len }}冊
{%- endif %}
───────────
{%- else %}
{%- if rental_books.filter_type == "rental_normal" %}
　　　貸出：0冊
{%- elif rental_books.filter_type == "rental_expired" %}
　　　延滞：0冊
{%- elif rental_books.filter_type == "rental_expire" %}
　{{ rental_books.filter_param["xdays"] }}日以内で延滞：0冊
{%- endif %}
───────────
{% endif -%}
{%- for date, keyed_books in date_keyed_books_dict.items() %}
{% if keyed_books[0].is_expired() == True -%}􀂢{%- elif keyed_books[0].is_expire_in_xdays(2) == True -%}􀂤{%- else -%}􀀹{%- endif -%}{{ keyed_books[0].expire_date_text }}{{ keyed_books[0].get_expire_text_from_today() }}
{% for book in keyed_books -%}
 {%- if book.can_extend_period %}􀂥{%- else -%}􀂦{%- endif -%}{{ book.name }}
{% endfor -%}
{%- endfor -%}