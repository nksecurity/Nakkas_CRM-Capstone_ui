import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow, QPushButton,
    QStackedWidget, QTableWidget, QVBoxLayout, QWidget
)

# ---------------------------------------------------------
# GENEL STİL PALETİ VE QSS TANIMLARI
# ---------------------------------------------------------
BASE_STYLE = """
    QWidget {
        font-family: 'Segoe UI', Arial, sans-serif;
        font-size: 13px;
        color: #ECF0F1;
        background-color: #1E1E2E;
    }
    QLineEdit {
        background-color: #2A2A3D;
        border: 2px solid #3B3B54;
        border-radius: 8px;
        padding: 8px 12px;
        color: #FFFFFF;
    }
    QLineEdit:focus { border: 2px solid #89B4FA; }
    QPushButton {
        background-color: #3B3B54;
        border: none;
        border-radius: 8px;
        padding: 10px 18px;
        font-weight: bold;
        color: #FFFFFF;
    }
    QPushButton:hover { background-color: #4A4A6A; }
    QPushButton:pressed { background-color: #2A2A3D; }
    QTableWidget {
        background-color: #252538;
        border: 1px solid #3B3B54;
        border-radius: 8px;
        gridline-color: #3B3B54;
    }
    QHeaderView::section {
        background-color: #181825;
        padding: 8px;
        font-weight: bold;
        border: none;
        border-bottom: 2px solid #3B3B54;
    }
    QComboBox {
        background-color: #2A2A3D;
        border: 2px solid #3B3B54;
        border-radius: 8px;
        padding: 6px 12px;
        color: #FFFFFF;
    }
"""

# ---------------------------------------------------------
# 1. LOGIN WINDOW
# ---------------------------------------------------------
class LoginWindow(QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        frame = QFrame()
        frame.setStyleSheet("QFrame { background-color: #252538; border: 2px solid #45475A; border-radius: 16px; padding: 24px; }")
        frame_layout = QVBoxLayout(frame)

        title = QLabel("CRM Portal Login")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold; color: #89B4FA; margin-bottom: 12px;")

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username (Type 'admin' for Admin view)")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.warning_label = QLabel("")
        self.warning_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.warning_label.setStyleSheet("color: #F38BA8; font-size: 12px;")

        btn_login = QPushButton("Login")
        btn_login.setStyleSheet("background-color: #89B4FA; color: #11111B;")
        btn_login.clicked.connect(self.handle_login)

        btn_close = QPushButton("Close")
        btn_close.setStyleSheet("background-color: #F38BA8; color: #11111B;")
        btn_close.clicked.connect(QApplication.instance().quit)

        frame_layout.addWidget(title)
        frame_layout.addWidget(self.username_input)
        frame_layout.addWidget(self.password_input)
        frame_layout.addWidget(self.warning_label)
        frame_layout.addWidget(btn_login)
        frame_layout.addWidget(btn_close)

        layout.addWidget(frame)
        self.setLayout(layout)

    def handle_login(self):
        user = self.username_input.text().strip().lower()
        if user == "admin":
            self.main_app.is_admin = True
            self.main_app.show_page("admin_preferences")
        else:
            self.main_app.is_admin = False
            self.main_app.show_page("user_preferences")

# ---------------------------------------------------------
# 2. PREFERENCES MENU
# ---------------------------------------------------------
class UserPreferencesWindow(QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        frame = QFrame()
        frame.setStyleSheet("QFrame { background-color: #1E2D2F; border: 2px solid #A6E3A1; border-radius: 16px; padding: 24px; }")
        frame_layout = QVBoxLayout(frame)

        title = QLabel("Preferences Menu")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 18px; font-weight: bold; color: #A6E3A1; margin-bottom: 16px;")

        btn_apps = QPushButton("Applications")
        btn_apps.clicked.connect(lambda: self.main_app.show_page("applications"))

        btn_mentor = QPushButton("Mentor Interview")
        btn_mentor.clicked.connect(lambda: self.main_app.show_page("mentor_interview"))

        btn_interviews = QPushButton("Interviews")
        btn_interviews.clicked.connect(lambda: self.main_app.show_page("interviews"))

        btn_close = QPushButton("Close")
        btn_close.setStyleSheet("background-color: #F38BA8; color: #11111B;")
        btn_close.clicked.connect(lambda: self.main_app.show_page("login"))

        frame_layout.addWidget(title)
        frame_layout.addWidget(btn_apps)
        frame_layout.addWidget(btn_mentor)
        frame_layout.addWidget(btn_interviews)
        frame_layout.addWidget(btn_close)

        layout.addWidget(frame)
        self.setLayout(layout)

# ---------------------------------------------------------
# 3. PREFERENCES — ADMIN MENU
# ---------------------------------------------------------
class AdminPreferencesWindow(QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        frame = QFrame()
        frame.setStyleSheet("QFrame { background-color: #2D1E2F; border: 2px solid #F5C2E7; border-radius: 16px; padding: 24px; }")
        frame_layout = QVBoxLayout(frame)

        title = QLabel("Preferences — Admin Menu")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 18px; font-weight: bold; color: #F5C2E7; margin-bottom: 16px;")

        btn_apps = QPushButton("Applications")
        btn_apps.clicked.connect(lambda: self.main_app.show_page("applications"))

        btn_mentor = QPushButton("Mentor Interview")
        btn_mentor.clicked.connect(lambda: self.main_app.show_page("mentor_interview"))

        btn_interviews = QPushButton("Interviews")
        btn_interviews.clicked.connect(lambda: self.main_app.show_page("interviews"))

        btn_admin = QPushButton("Admin")
        btn_admin.setStyleSheet("background-color: #F5C2E7; color: #11111B;")
        btn_admin.clicked.connect(lambda: self.main_app.show_page("admin_menu"))

        btn_close = QPushButton("Close")
        btn_close.setStyleSheet("background-color: #F38BA8; color: #11111B;")
        btn_close.clicked.connect(lambda: self.main_app.show_page("login"))

        frame_layout.addWidget(title)
        frame_layout.addWidget(btn_apps)
        frame_layout.addWidget(btn_mentor)
        frame_layout.addWidget(btn_interviews)
        frame_layout.addWidget(btn_admin)
        frame_layout.addWidget(btn_close)

        layout.addWidget(frame)
        self.setLayout(layout)

# ---------------------------------------------------------
# 4. APPLICATIONS PAGE
# ---------------------------------------------------------
class ApplicationsWindow(QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        frame = QFrame()
        frame.setStyleSheet("QFrame { background-color: #1E1E2E; border: 2px solid #89B4FA; border-radius: 12px; padding: 16px; }")
        frame_layout = QVBoxLayout(frame)

        search_layout = QHBoxLayout()
        search_input = QLineEdit()
        search_input.setPlaceholderText("Search Applications...")
        btn_search = QPushButton("Search")
        search_layout.addWidget(search_input)
        search_layout.addWidget(btn_search)

        filter_layout = QHBoxLayout()
        btn_all = QPushButton("All Applications")
        btn_defined = QPushButton("Mentor Meeting Defined")
        btn_not_defined = QPushButton("Mentor Meeting Not Defined")
        filter_layout.addWidget(btn_all)
        filter_layout.addWidget(btn_defined)
        filter_layout.addWidget(btn_not_defined)

        table = QTableWidget()
        table.setColumnCount(7)
        table.setHorizontalHeaderLabels([
            "ID", "Name", "Email", "Application Date", 
            "Mentor Status", "Interview Status", "Notes"
        ])
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        btn_return = QPushButton("Return to Preferences Screen")
        btn_return.setStyleSheet("background-color: #FAB387; color: #11111B;")
        btn_return.clicked.connect(self.main_app.return_to_preferences)

        frame_layout.addLayout(search_layout)
        frame_layout.addLayout(filter_layout)
        frame_layout.addWidget(table)
        frame_layout.addWidget(btn_return)

        layout.addWidget(frame)
        self.setLayout(layout)

# ---------------------------------------------------------
# 5. MENTOR INTERVIEW PAGE
# ---------------------------------------------------------
class MentorInterviewWindow(QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        frame = QFrame()
        frame.setStyleSheet("QFrame { background-color: #1E1E2E; border: 2px solid #A6E3A1; border-radius: 12px; padding: 16px; }")
        frame_layout = QVBoxLayout(frame)

        top_layout = QHBoxLayout()
        search_input = QLineEdit()
        search_input.setPlaceholderText("Search Conversations...")
        btn_search = QPushButton("Search")
        
        combo_filter = QComboBox()
        combo_filter.addItems(["Edit Items", "Tab 1", "Tab 2", "Tab 3"])

        top_layout.addWidget(search_input)
        top_layout.addWidget(btn_search)
        top_layout.addWidget(combo_filter)

        btn_all_conversations = QPushButton("All Conversations")

        table = QTableWidget()
        table.setColumnCount(5)
        table.setHorizontalHeaderLabels(["Candidate", "Mentor", "Date", "Topic", "Result"])
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        btn_return = QPushButton("Return to Preferences Screen")
        btn_return.setStyleSheet("background-color: #FAB387; color: #11111B;")
        btn_return.clicked.connect(self.main_app.return_to_preferences)

        frame_layout.addLayout(top_layout)
        frame_layout.addWidget(btn_all_conversations)
        frame_layout.addWidget(table)
        frame_layout.addWidget(btn_return)

        layout.addWidget(frame)
        self.setLayout(layout)

# ---------------------------------------------------------
# 6. INTERVIEWS PAGE
# ---------------------------------------------------------
class InterviewsWindow(QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        frame = QFrame()
        frame.setStyleSheet("QFrame { background-color: #1E1E2E; border: 2px solid #CBA6F7; border-radius: 12px; padding: 16px; }")
        frame_layout = QVBoxLayout(frame)

        search_layout = QHBoxLayout()
        search_input = QLineEdit()
        search_input.setPlaceholderText("Search Interviews...")
        btn_search = QPushButton("Search")
        search_layout.addWidget(search_input)
        search_layout.addWidget(btn_search)

        btn_layout = QHBoxLayout()
        btn_proj_sent = QPushButton("Project Sent")
        btn_proj_received = QPushButton("Project Received")
        btn_layout.addWidget(btn_proj_sent)
        btn_layout.addWidget(btn_proj_received)

        table = QTableWidget()
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(["Candidate Name", "Project Name", "Sent Date", "Received Date"])
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        btn_return = QPushButton("Return to Preferences Screen")
        btn_return.setStyleSheet("background-color: #FAB387; color: #11111B;")
        btn_return.clicked.connect(self.main_app.return_to_preferences)

        frame_layout.addLayout(search_layout)
        frame_layout.addLayout(btn_layout)
        frame_layout.addWidget(table)
        frame_layout.addWidget(btn_return)

        layout.addWidget(frame)
        self.setLayout(layout)

# ---------------------------------------------------------
# 7. ADMIN MENU
# ---------------------------------------------------------
class AdminMenuWindow(QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        frame = QFrame()
        frame.setStyleSheet("QFrame { background-color: #1E1E2E; border: 2px solid #F5C2E7; border-radius: 12px; padding: 16px; }")
        frame_layout = QVBoxLayout(frame)

        title = QLabel("Admin Menu")
        title.setStyleSheet("font-size: 16px; font-weight: bold; color: #F5C2E7;")

        btn_layout = QHBoxLayout()
        btn_event = QPushButton("Event Record")
        btn_mail = QPushButton("Mail")
        btn_layout.addWidget(btn_event)
        btn_layout.addWidget(btn_mail)

        table = QTableWidget()
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(["Event Title", "Date", "Participants", "Mail Status"])
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        bottom_layout = QHBoxLayout()
        btn_return_admin = QPushButton("Preferences — Return to Admin Screen")
        btn_return_admin.setStyleSheet("background-color: #FAB387; color: #11111B;")
        btn_return_admin.clicked.connect(lambda: self.main_app.show_page("admin_preferences"))

        btn_exit = QPushButton("Exit")
        btn_exit.setStyleSheet("background-color: #F38BA8; color: #11111B;")
        btn_exit.clicked.connect(QApplication.instance().quit)

        bottom_layout.addWidget(btn_return_admin)
        bottom_layout.addWidget(btn_exit)

        frame_layout.addWidget(title)
        frame_layout.addLayout(btn_layout)
        frame_layout.addWidget(table)
        frame_layout.addLayout(bottom_layout)

        layout.addWidget(frame)
        self.setLayout(layout)

# ---------------------------------------------------------
# ANA UYGULAMA VE SAYFA GEÇİŞLERİ
# ---------------------------------------------------------
class CRMApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRM Capstone Project — Interface Design")
        self.resize(950, 680)
        self.setStyleSheet(BASE_STYLE)

        self.is_admin = False

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.pages = {
            "login": LoginWindow(self),
            "user_preferences": UserPreferencesWindow(self),
            "admin_preferences": AdminPreferencesWindow(self),
            "applications": ApplicationsWindow(self),
            "mentor_interview": MentorInterviewWindow(self),
            "interviews": InterviewsWindow(self),
            "admin_menu": AdminMenuWindow(self)
        }

        for page in self.pages.values():
            self.stacked_widget.addWidget(page)

        self.show_page("login")

    def show_page(self, page_name):
        if page_name in self.pages:
            self.stacked_widget.setCurrentWidget(self.pages[page_name])

    def return_to_preferences(self):
        if self.is_admin:
            self.show_page("admin_preferences")
        else:
            self.show_page("user_preferences")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = CRMApplication()
    main_win.show()
    sys.exit(app.exec())
