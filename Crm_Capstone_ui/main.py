import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow, QPushButton,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
)

# ---------------------------------------------------------
# MODERN DARK TEMA (QSS)
# ---------------------------------------------------------
MODERN_STYLE = """
    QWidget {
        font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
        font-size: 13px;
        color: #E2E8F0;
        background-color: #0F172A;
    }
    
    /* Input & Search Fields */
    QLineEdit {
        background-color: #1E293B;
        border: 1px solid #334155;
        border-radius: 8px;
        padding: 10px 14px;
        color: #F8FAFC;
        font-size: 13px;
    }
    QLineEdit:focus {
        border: 1px solid #3B82F6;
        background-color: #0F172A;
    }
    
    /* Buttons */
    QPushButton {
        background-color: #1E293B;
        border: 1px solid #334155;
        border-radius: 8px;
        padding: 10px 16px;
        font-weight: 600;
        color: #CBD5E1;
    }
    QPushButton:hover {
        background-color: #334155;
        color: #FFFFFF;
        border-color: #475569;
    }
    QPushButton:pressed {
        background-color: #0F172A;
    }
    
    /* Primary Accent Button */
    QPushButton#primaryBtn {
        background-color: #3B82F6;
        color: #FFFFFF;
        border: none;
    }
    QPushButton#primaryBtn:hover {
        background-color: #2563EB;
    }
    
    /* Danger / Close Button */
    QPushButton#dangerBtn {
        background-color: #EF4444;
        color: #FFFFFF;
        border: none;
    }
    QPushButton#dangerBtn:hover {
        background-color: #DC2626;
    }

    /* Table Styling */
    QTableWidget {
        background-color: #1E293B;
        border: 1px solid #334155;
        border-radius: 10px;
        gridline-color: #334155;
        outline: none;
    }
    QTableWidget::item {
        padding: 8px;
    }
    QTableWidget::item:selected {
        background-color: #3B82F6;
        color: #FFFFFF;
    }
    QHeaderView::section {
        background-color: #0F172A;
        color: #94A3B8;
        padding: 10px;
        font-weight: 700;
        border: none;
        border-bottom: 2px solid #334155;
        text-transform: uppercase;
        font-size: 11px;
    }

    /* ComboBox Styling */
    QComboBox {
        background-color: #1E293B;
        border: 1px solid #334155;
        border-radius: 8px;
        padding: 8px 12px;
        color: #F8FAFC;
    }
    QComboBox::drop-down { border: none; }
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

        card = QFrame()
        card.setFixedWidth(380)
        card.setStyleSheet("""
            QFrame {
                background-color: #1E293B;
                border: 1px solid #334155;
                border-radius: 16px;
                padding: 32px;
            }
        """)
        card_layout = QVBoxLayout(card)
        card_layout.setSpacing(14)

        logo_label = QLabel("⚡ CRM PORTAL")
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo_label.setStyleSheet("font-size: 22px; font-weight: 800; color: #3B82F6; border: none; background: transparent;")

        sub_label = QLabel("Giriş yapmak için bilgilerinizi girin")
        sub_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sub_label.setStyleSheet("font-size: 12px; color: #94A3B8; border: none; background: transparent; margin-bottom: 10px;")

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Kullanıcı Adı (Admin için 'admin')")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Şifre")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.warning_label = QLabel("")
        self.warning_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.warning_label.setStyleSheet("color: #EF4444; font-size: 12px; border: none; background: transparent;")

        btn_login = QPushButton("Giriş Yap")
        btn_login.setObjectName("primaryBtn")
        btn_login.clicked.connect(self.handle_login)

        btn_close = QPushButton("Uygulamayı Kapat")
        btn_close.setObjectName("dangerBtn")
        btn_close.clicked.connect(QApplication.instance().quit)

        card_layout.addWidget(logo_label)
        card_layout.addWidget(sub_label)
        card_layout.addWidget(self.username_input)
        card_layout.addWidget(self.password_input)
        card_layout.addWidget(self.warning_label)
        card_layout.addWidget(btn_login)
        card_layout.addWidget(btn_close)

        layout.addWidget(card)
        self.setLayout(layout)

    def handle_login(self):
        user = self.username_input.text().strip().lower()
        if user == "admin":
            self.main_app.is_admin = True
            self.main_app.show_main_layout("admin_preferences")
        else:
            self.main_app.is_admin = False
            self.main_app.show_main_layout("user_preferences")

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

        card = QFrame()
        card.setFixedWidth(420)
        card.setStyleSheet("QFrame { background-color: #1E293B; border: 1px solid #10B981; border-radius: 16px; padding: 28px; }")
        card_layout = QVBoxLayout(card)
        card_layout.setSpacing(12)

        title = QLabel("Kullanıcı Tercihleri")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: 700; color: #10B981; border: none; background: transparent;")

        btn_apps = QPushButton("Applications")
        btn_apps.clicked.connect(lambda: self.main_app.navigate_to("applications"))

        btn_mentor = QPushButton("Mentor Interview")
        btn_mentor.clicked.connect(lambda: self.main_app.navigate_to("mentor_interview"))

        btn_interviews = QPushButton("Interviews")
        btn_interviews.clicked.connect(lambda: self.main_app.navigate_to("interviews"))

        btn_close = QPushButton("Çıkış Yap")
        btn_close.setObjectName("dangerBtn")
        btn_close.clicked.connect(self.main_app.logout)

        card_layout.addWidget(title)
        card_layout.addWidget(btn_apps)
        card_layout.addWidget(btn_mentor)
        card_layout.addWidget(btn_interviews)
        card_layout.addWidget(btn_close)

        layout.addWidget(card)
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

        card = QFrame()
        card.setFixedWidth(420)
        card.setStyleSheet("QFrame { background-color: #1E293B; border: 1px solid #EC4899; border-radius: 16px; padding: 28px; }")
        card_layout = QVBoxLayout(card)
        card_layout.setSpacing(12)

        title = QLabel("Admin Tercihleri")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: 700; color: #EC4899; border: none; background: transparent;")

        btn_apps = QPushButton("Applications")
        btn_apps.clicked.connect(lambda: self.main_app.navigate_to("applications"))

        btn_mentor = QPushButton("Mentor Interview")
        btn_mentor.clicked.connect(lambda: self.main_app.navigate_to("mentor_interview"))

        btn_interviews = QPushButton("Interviews")
        btn_interviews.clicked.connect(lambda: self.main_app.navigate_to("interviews"))

        btn_admin = QPushButton("Admin Settings")
        btn_admin.setStyleSheet("background-color: #EC4899; color: #FFFFFF; border: none;")
        btn_admin.clicked.connect(lambda: self.main_app.navigate_to("admin_menu"))

        btn_close = QPushButton("Çıkış Yap")
        btn_close.setObjectName("dangerBtn")
        btn_close.clicked.connect(self.main_app.logout)

        card_layout.addWidget(title)
        card_layout.addWidget(btn_apps)
        card_layout.addWidget(btn_mentor)
        card_layout.addWidget(btn_interviews)
        card_layout.addWidget(btn_admin)
        card_layout.addWidget(btn_close)

        layout.addWidget(card)
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
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(16)

        # Top Bar (Search + Filter)
        top_bar = QHBoxLayout()
        search_input = QLineEdit()
        search_input.setPlaceholderText("Başvurularda ara...")
        btn_search = QPushButton("Ara")
        btn_search.setObjectName("primaryBtn")
        
        top_bar.addWidget(search_input)
        top_bar.addWidget(btn_search)

        filter_bar = QHBoxLayout()
        filter_bar.addWidget(QPushButton("All Applications"))
        filter_bar.addWidget(QPushButton("Mentor Meeting Defined"))
        filter_bar.addWidget(QPushButton("Mentor Meeting Not Defined"))

        # Table
        table = QTableWidget()
        table.setColumnCount(7)
        table.setHorizontalHeaderLabels([
            "ID", "Name", "Email", "Application Date", 
            "Mentor Status", "Interview Status", "Notes"
        ])
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        btn_return = QPushButton("Return to Preferences Screen")
        btn_return.clicked.connect(self.main_app.return_to_preferences)

        layout.addLayout(top_bar)
        layout.addLayout(filter_bar)
        layout.addWidget(table)
        layout.addWidget(btn_return)

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
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(16)

        top_bar = QHBoxLayout()
        search_input = QLineEdit()
        search_input.setPlaceholderText("Görüşmelerde ara...")
        btn_search = QPushButton("Ara")
        btn_search.setObjectName("primaryBtn")

        combo_filter = QComboBox()
        combo_filter.addItems(["Edit Items", "Tab 1", "Tab 2", "Tab 3"])

        top_bar.addWidget(search_input)
        top_bar.addWidget(btn_search)
        top_bar.addWidget(combo_filter)

        btn_all = QPushButton("All Conversations")

        table = QTableWidget()
        table.setColumnCount(5)
        table.setHorizontalHeaderLabels(["Candidate", "Mentor", "Date", "Topic", "Result"])
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        btn_return = QPushButton("Return to Preferences Screen")
        btn_return.clicked.connect(self.main_app.return_to_preferences)

        layout.addLayout(top_bar)
        layout.addWidget(btn_all)
        layout.addWidget(table)
        layout.addWidget(btn_return)

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
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(16)

        top_bar = QHBoxLayout()
        search_input = QLineEdit()
        search_input.setPlaceholderText("Mülakatlarda ara...")
        btn_search = QPushButton("Ara")
        btn_search.setObjectName("primaryBtn")
        top_bar.addWidget(search_input)
        top_bar.addWidget(btn_search)

        filter_bar = QHBoxLayout()
        filter_bar.addWidget(QPushButton("Project Sent"))
        filter_bar.addWidget(QPushButton("Project Received"))

        table = QTableWidget()
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(["Candidate Name", "Project Name", "Sent Date", "Received Date"])
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        btn_return = QPushButton("Return to Preferences Screen")
        btn_return.clicked.connect(self.main_app.return_to_preferences)

        layout.addLayout(top_bar)
        layout.addLayout(filter_bar)
        layout.addWidget(table)
        layout.addWidget(btn_return)

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
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(16)

        action_bar = QHBoxLayout()
        btn_event = QPushButton("Event Record")
        btn_event.setObjectName("primaryBtn")
        btn_mail = QPushButton("Mail")
        action_bar.addWidget(btn_event)
        action_bar.addWidget(btn_mail)

        table = QTableWidget()
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(["Event Title", "Date", "Participants", "Mail Status"])
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        bottom_bar = QHBoxLayout()
        btn_return_admin = QPushButton("Preferences — Return to Admin Screen")
        btn_return_admin.clicked.connect(lambda: self.main_app.navigate_to("admin_preferences"))

        btn_exit = QPushButton("Exit")
        btn_exit.setObjectName("dangerBtn")
        btn_exit.clicked.connect(QApplication.instance().quit)

        bottom_bar.addWidget(btn_return_admin)
        bottom_bar.addWidget(btn_exit)

        layout.addLayout(action_bar)
        layout.addWidget(table)
        layout.addLayout(bottom_bar)

        self.setLayout(layout)

# ---------------------------------------------------------
# MODERN MAIN LAYOUT WITH SIDEBAR & STACKED WIDGET
# ---------------------------------------------------------
class CRMApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRM Capstone Portal — Modern UI")
        self.resize(1100, 700)
        self.setStyleSheet(MODERN_STYLE)

        self.is_admin = False

        # Central Layout Container
        self.main_container = QWidget()
        self.root_layout = QHBoxLayout(self.main_container)
        self.root_layout.setContentsMargins(0, 0, 0, 0)
        self.root_layout.setSpacing(0)

        # 1. Sidebar Setup
        self.sidebar = QFrame()
        self.sidebar.setFixedWidth(220)
        self.sidebar.setStyleSheet("""
            QFrame {
                background-color: #1E293B;
                border-right: 1px solid #334155;
            }
            QPushButton {
                text-align: left;
                padding: 12px 16px;
                background: transparent;
                border: none;
                border-radius: 6px;
                color: #94A3B8;
            }
            QPushButton:hover {
                background-color: #334155;
                color: #FFFFFF;
            }
        """)
        self.sidebar_layout = QVBoxLayout(self.sidebar)
        self.sidebar_layout.setContentsMargins(12, 20, 12, 20)

        sidebar_title = QLabel("⚡ CRM PORTAL")
        sidebar_title.setStyleSheet("font-size: 16px; font-weight: 800; color: #3B82F6; margin-bottom: 20px; border: none;")
        self.sidebar_layout.addWidget(sidebar_title)

        # Sidebar Buttons
        self.btn_nav_pref = QPushButton("🏠 Preferences")
        self.btn_nav_apps = QPushButton("📋 Applications")
        self.btn_nav_mentor = QPushButton("👥 Mentor Interview")
        self.btn_nav_interviews = QPushButton("💼 Interviews")
        self.btn_nav_admin = QPushButton("⚙️ Admin Menu")

        self.btn_nav_pref.clicked.connect(self.return_to_preferences)
        self.btn_nav_apps.clicked.connect(lambda: self.navigate_to("applications"))
        self.btn_nav_mentor.clicked.connect(lambda: self.navigate_to("mentor_interview"))
        self.btn_nav_interviews.clicked.connect(lambda: self.navigate_to("interviews"))
        self.btn_nav_admin.clicked.connect(lambda: self.navigate_to("admin_menu"))

        self.sidebar_layout.addWidget(self.btn_nav_pref)
        self.sidebar_layout.addWidget(self.btn_nav_apps)
        self.sidebar_layout.addWidget(self.btn_nav_mentor)
        self.sidebar_layout.addWidget(self.btn_nav_interviews)
        self.sidebar_layout.addWidget(self.btn_nav_admin)
        self.sidebar_layout.addStretch()

        btn_logout = QPushButton("🚪 Logout")
        btn_logout.clicked.connect(self.logout)
        self.sidebar_layout.addWidget(btn_logout)

        # 2. Content Stack Setup
        self.stacked_widget = QStackedWidget()

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

        # Add to Root Layout
        self.root_layout.addWidget(self.sidebar)
        self.root_layout.addWidget(self.stacked_widget)

        self.setCentralWidget(self.main_container)
        self.show_login()

    def show_login(self):
        self.sidebar.hide()
        self.stacked_widget.setCurrentWidget(self.pages["login"])

    def show_main_layout(self, pref_page):
        self.sidebar.show()
        # Admin butonu gizleme/gösterme kontrolü
        self.btn_nav_admin.setVisible(self.is_admin)
        self.stacked_widget.setCurrentWidget(self.pages[pref_page])

    def navigate_to(self, page_name):
        if page_name in self.pages:
            self.stacked_widget.setCurrentWidget(self.pages[page_name])

    def return_to_preferences(self):
        if self.is_admin:
            self.navigate_to("admin_preferences")
        else:
            self.navigate_to("user_preferences")

    def logout(self):
        self.is_admin = False
        self.show_login()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = CRMApplication()
    main_win.show()
    sys.exit(app.exec())
