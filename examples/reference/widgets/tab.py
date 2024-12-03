import panel as pn
import pandas as pd

def cb(e):
  print(f'Menu clicked: {e}')

df = pd.DataFrame({
  'Name': ['Abc', 'Def', 'GHI Jkl'], 
  'Age': [23, 34, 53],
})
tab = pn.widgets.Tabulator(df, configuration={
  'rowContextMenu': [
    {'label': 'Add'},
    {'label': 'Remove'},
    {'separator': True},
    {'label': 'Print'},
  ]
})
tab.on_menu_click(cb)

tab.servable()
