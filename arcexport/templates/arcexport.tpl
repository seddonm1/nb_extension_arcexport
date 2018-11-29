{"stages": [
{%- for cell in nb.cells -%}
  {%- if not cell.source.lstrip().startswith( '%%' ) -%}
    {{ cell.source.lstrip().rstrip() }}{{ "," if not loop.last }}
  {%- endif -%}
{%- endfor -%}
]}