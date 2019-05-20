{"stages": [
{%- for cell in nb.cells -%}
  {%- if cell.cell_type == "code" -%}
    {%- if not cell.source.lstrip().startswith( "%" ) -%}
      {{ cell.source.lstrip().rstrip() }}{{ "," if not loop.last }}
    {%- endif -%}
    {%- if cell.source.lstrip().startswith( "%arc" ) -%}
      {{ cell.source.lstrip().rstrip() | replace("%arc", "") }}{{ "," if not loop.last }}
    {%- endif -%}    
  {%- endif -%}
{%- endfor -%}
]}