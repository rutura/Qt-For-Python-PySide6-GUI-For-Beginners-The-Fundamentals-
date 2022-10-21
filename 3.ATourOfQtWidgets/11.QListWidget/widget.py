from PySide6.QtWidgets import QWidget,  QCheckBox, QHBoxLayout, QVBoxLayout, QListWidget, QAbstractItemView, QPushButton,QButtonGroup

class Widget(QWidget):
    def __init__(self):
        super().__init__()
       
        self.setWindowTitle("QListWidget Demo")

        self.list_widget = QListWidget(self)
        self.list_widget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.list_widget.addItem("One")
        self.list_widget.addItems(["Two","Three"])
        self.list_widget.currentItemChanged.connect(self.current_item_changed)
        self.list_widget.currentTextChanged.connect(self.current_text_changed)


        button_add_item = QPushButton("Add Item")
        button_add_item.clicked.connect(self.add_item)

        button_delete_item = QPushButton("Delete Item")
        button_delete_item.clicked.connect(self.delete_item)

        button_item_count = QPushButton("Item Count")
        button_item_count.clicked.connect(self.item_count)

        button_selected_items = QPushButton("Selected Items")
        button_selected_items.clicked.connect(self.selected_items)


        v_layout = QVBoxLayout()
        v_layout.addWidget(self.list_widget)
        v_layout.addWidget(button_add_item)
        v_layout.addWidget(button_delete_item)
        v_layout.addWidget(button_item_count)
        v_layout.addWidget(button_selected_items)

        self.setLayout(v_layout)

    def current_item_changed(self, item):
        print("Current item : ",item.text())

    def current_text_changed(self,text):
        print("Current text changed : ",text)

    def add_item(self):
        self.list_widget.addItem("New Item")

    def item_count(self):
        print("Item count : ",self.list_widget.count())

    def delete_item(self):
        self.list_widget.takeItem(self.list_widget.currentRow())

    def selected_items(self):
        list = self.list_widget.selectedItems()
        for i in list : 
            print(i.text())