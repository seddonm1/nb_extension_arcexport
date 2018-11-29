{"stages": [
{%- for cell in nb.cells -%}
  {%- if cell.cell_type == "code" -%}
    {%- if not cell.source.lstrip().startswith( '%%' ) -%}
      {{ cell.source.lstrip().rstrip() }}{{ "," if not loop.last }}
    {%- endif -%}
  {%- endif -%}
{%- endfor -%}
]}