import PySimpleGUI as sg
from datetime import date
from logic import FinanceManager
from persistence import Persistence
from utils import parse_date_str, format_currency

class GUI:
    def __init__(self):
        self.persistence = Persistence()
        self.manager = FinanceManager(self.persistence)
        sg.theme("LightBlue")

        header = ["Fecha", "Titulo", "Monto", "Categoria", "Tipo"]
        layout = [
            [sg.Text("Finance Manager", font=("Any", 16))],
            [sg.Table(values=self._table_values(),
                    headings=header,
                    key= "-TABLE-",
                    auto_size_columns=True,
                    num_rows=10,
                    justification='left',
                    row_colors=self._row_colors()
                    )],
            [sg.Text("Totals:"), sg.Text(self._totals_str(), key= "-TOTALS-")],
            [sg.Button("Add Category"), sg.Button("Add Expense"), sg.Button("Add Income"),
            sg.Button("Export CSV"), sg.Button("Refresh"), sg.Button("Exit")]
        ]
        self.window = sg.Window("Finance Manager", layout, finalize=True)

    def _table_values(self):
        vals = []
        for t in self.manager.transactions:
            vals.append([t.date.strftime("%d/%m/%Y"), t.title, str(t.amount), t.category, t.type])
        return vals
    
    def _row_colors(self):
        colors = []
        for i, t in enumerate(self.manager.transactions):
            cat_color = None
            for c in self.manager.categories:
                if c.name == t.category and c.color:
                    cat_color = c.color
                    break
            if cat_color:
                colors.append((i, cat_color))
        return colors

    def _totals_str(self):
        tot = self.manager.totals()
        return f"Incomes: {format_currency(tot['incomes'])} | Expenses: {format_currency(tot['expenses'])} | Balance: {format_currency(tot['balance'])}"

    def run(self):
        while True:
            event, values = self.window.read()
            if event in (sg.WIN_CLOSED, "Exit"):
                break
            if event == "Add Category":
                self._open_add_category()
            elif event in ("Add Expense", "Add Income"):
                self._open_add_transaction("Expense" if event == "Add Expense" else "Income")
            elif event == "Export CSV":
                path = sg.popup_get_file("Save CSV", save_as=True, no_window=True, file_types=(("CSV Files","*.csv"),))
                if path:
                    try:
                        self.manager.export_csv(path)
                        sg.popup("Exported CSV")
                    except Exception as e:
                        sg.popup_error("Error exporting CSV", str(e))
            elif event == "Refresh":
                self._refresh_table()
        self.window.close()

    def _refresh_table(self):
        self.window["-TABLE-"].update(
            values=self._table_values(),
            row_colors=self._row_colors()  
        )
        self.window["-TOTALS-"].update(self._totals_str())

        
    def _open_add_category(self):
        layout = [
            [sg.Text("Category name:"), sg.Input(key="-CAT_NAME-")],
            [sg.Text("Color (optional):"), sg.Input(key="-CAT_COLOR-"), sg.ColorChooserButton("Choose", target="-CAT_COLOR-")],
            [sg.Button("Add"), sg.Button("Cancel")]
        ]
        w = sg.Window("Add Category", layout, modal=True)
        while True:
            e, v = w.read()
            if e in (sg.WINDOW_CLOSED, "Cancel"):
                break
            if e == "Add":
                try:
                    self.manager.add_category(v["-CAT_NAME-"], v["-CAT_COLOR-"] or None)
                    sg.popup("Category added")
                    self._refresh_table()
                    break
                except Exception as ex:
                    sg.popup_error("Error adding category", str(ex))
        w.close()

    def _open_add_transaction(self, type_):
        if not self.manager.categories:
            sg.popup_error("No categories available. Please add a category first.")
            return
        category_names = [c.name for c in self.manager.categories]
        layout = [
            [sg.Text("Title:"), sg.Input(key="-TITLE-")],
            [sg.Text("Amount:"), sg.Input(key="-AMOUNT-")],
            [sg.Text("Category:"), sg.Combo(category_names, key="-CATEGORY-")],
            [sg.Text("Date (dd/mm/YYYY):"), sg.Input(date.today().strftime("%d/%m/%Y"), key="-DATE-")],
            [sg.Button("Add"), sg.Button("Cancel")]
        ]
        w = sg.Window(f"Add {type_}", layout, modal=True)
        while True:
            e, v = w.read()
            if e in (sg.WINDOW_CLOSED, "Cancel"):
                break
            if e == "Add":
                try:
                    dt = parse_date_str(v["-DATE-"])
                    amount = float(v["-AMOUNT-"])
                    # If expense, optionally store negative amount — here we store amount positive and type_ distinguishes
                    self.manager.add_transaction(v["-TITLE-"], amount, v["-CATEGORY-"], type_, dt)
                    sg.popup(f"{type_} added")
                    self._refresh_table()
                    break
                except Exception as ex:
                    sg.popup_error("Error adding transaction", str(ex))
        w.close()
