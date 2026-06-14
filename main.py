import os
import flet as ft
import flet_video as ftv

def main(page: ft.Page):

    # =========================================================
    # PAGE SETTINGS (Optimized for Fixed Header Layout)
    # =========================================================
    page.title = "Lavinia Ndilimeke Shimutwikeni - Mining Engineering Portfolio"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.spacing = 0
    page.bgcolor = "#fff0f5"  # Lavender Blush - Soft pink background
    page.scroll = None

    # =========================================================
    # PREMIUM PINK COLOR PALETTE
    # =========================================================
    PRIMARY_PINK = "#d63384"        # Deep Pink/Magenta
    ACCENT_PINK = "#f06292"         # Medium Pink
    DEEP_PINK = "#ad1457"           # Darker Pink for text/buttons
    LIGHT_BG = "#fff0f5"            # Soft pink-tint background
    SECTION_PINK = "#fce4ec"        # Very light pink sections
    SECTION_DEEP = "#f8bbd0"        # Deeper pink sections
    BG_WHITE = "#ffffff"
    TEXT_GREY = "#4a154b"            # Dark purple-grey for text
    AVATAR_BG = "#fce4ec"
    SUBTEXT_GREY = "#6a1b6a"
    CARD_BG = "#ffffff"
    BORDER_COLOR = "#f48fb1"
    
    DARK_CARD_BG = "#880e4f"
    DARK_TEXT_WHITE = "#ffffff"
    NAV_INACTIVE = "#f8bbd0"
    OVERLAY_PINK = "#f06292"
    PROGRESS_TRACK = "#fce4ec"
    SHADOW_PINK = "#ec407a"
    CERT_HINT = "#f8bbd0"
    
    # MineOps specific colors
    MINEOPS_GOLD = "#ffd700"
    MINEOPS_PINK = "#ff69b4"

    # Image mapping based on available assets
    IMAGES = {
        "profile": "/images/Profile.jpeg",
        "mineops_logo": "/images/Mine_Ops.jpeg",
        "matlab_onramp": "/images/MATLAB_Onramp.png",
        "simulink_onramp": "/images/Simulink_Onramp.png",
        "calculations_vectors": "/images/Calculations_with_Vectors_and_Matrices.png",
        "explore_data": "/images/Explore_Data_with_MATLAB_Plots.png",
        "manipulate_matrices": "/images/Make_and_Manipulate_Matrices.png",
        "regression_deep": "/images/Regression_with_Deep_Learning.png",
        "signal_segmentation": "/images/Signal_Segmentation_with_Deep_Learning.png",
    }

    def open_certificate_zoom(title: str, image_src: str):
        zoom_dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text(title, color=PRIMARY_PINK, weight=ft.FontWeight.BOLD),
            content=ft.Container(
                width=900,
                height=620,
                bgcolor=BG_WHITE,
                padding=10,
                border_radius=8,
                content=ft.Image(src=image_src, fit="contain"),
            ),
            actions=[
                ft.TextButton("Close", on_click=lambda e: close_certificate_zoom(zoom_dialog)),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        page.show_dialog(zoom_dialog)

    def close_certificate_zoom(dialog):
        page.pop_dialog()

    def get_uniform_border(width: int, color: str):
        return ft.Border(
            top=ft.BorderSide(width, color),
            bottom=ft.BorderSide(width, color),
            left=ft.BorderSide(width, color),
            right=ft.BorderSide(width, color),
        )

    # =========================================================
    # PREMIUM COMPONENT BUILDERS
    # =========================================================
    def create_section_header(title: str, subtitle: str):
        return ft.Column(
            spacing=8,
            controls=[
                ft.Text(
                    title, 
                    size=28, 
                    weight=ft.FontWeight.BOLD, 
                    color=PRIMARY_PINK, 
                    style=ft.TextStyle(letter_spacing=1.2)
                ),
                ft.Text(subtitle, size=15, color=TEXT_GREY),
                ft.Container(height=4, width=60, bgcolor=ACCENT_PINK, border_radius=2),
                ft.Container(height=15)
            ]
        )

    def create_skill_chip(label: str, level: float):
        return ft.Container(
            bgcolor=BG_WHITE,
            padding=ft.Padding(16, 12, 16, 12),
            border_radius=8,
            border=get_uniform_border(1, BORDER_COLOR),
            content=ft.Column([
                ft.Row([
                    ft.Text(label, weight=ft.FontWeight.W_600, color=DEEP_PINK, size=14),
                    ft.Text(f"{int(level*100)}%", weight=ft.FontWeight.BOLD, color=PRIMARY_PINK, size=12)
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Container(height=6),
                ft.Stack([
                    ft.Container(height=4, bgcolor=PROGRESS_TRACK, border_radius=2, expand=True),
                    ft.Container(height=4, bgcolor=PRIMARY_PINK, border_radius=2, width=120 * level)
                ])
            ])
        )

    def create_info_card(title: str, body: str, icon=ft.Icons.CHECK_CIRCLE):
        return ft.Container(
            bgcolor=BG_WHITE,
            padding=20,
            border_radius=8,
            border=get_uniform_border(1, BORDER_COLOR),
            content=ft.Column(
                spacing=10,
                controls=[
                    ft.Row([
                        ft.Icon(icon, color=PRIMARY_PINK, size=24),
                        ft.Text(title, size=16, weight=ft.FontWeight.BOLD, color=DEEP_PINK),
                    ]),
                    ft.Text(body, color=TEXT_GREY, size=13),
                ],
            ),
        )

    # =========================================================
    # NAVIGATION SYSTEM
    # =========================================================
    current_page_key = {"value": "overview"}
    nav_buttons = {}

    def build_page_view(section_control, page_key):
        return ft.Column(
            key=f"page-{page_key}",
            expand=True,
            scroll=ft.ScrollMode.ALWAYS,
            spacing=0,
            controls=[section_control],
        )

    def navigate_to(page_key):
        current_page_key["value"] = page_key
        page_switcher.content = build_page_view(portfolio_pages[page_key], page_key)
        for key, button in nav_buttons.items():
            button.style = ft.ButtonStyle(
                color=BG_WHITE if key == page_key else NAV_INACTIVE,
                overlay_color=OVERLAY_PINK,
            )
        page.update()

    # =========================================================
    # SECTIONS DEFINITIONS
    # =========================================================
    
    # 1. Overview Section - Enhanced with more content
    hero_section = ft.Container(
        key="overview",
        bgcolor=LIGHT_BG,
        padding=ft.Padding(50, 60, 50, 60),
        content=ft.Column(
            spacing=30,
            controls=[
                ft.ResponsiveRow(
                    controls=[
                        ft.Column(
                            col={"sm": 12, "md": 7},
                            spacing=15,
                            controls=[
                                ft.Text(
                                    "MINING ENGINEERING STUDENT @ UNAM | MINEOPS TEAM MEMBER", 
                                    size=13, 
                                    weight=ft.FontWeight.W_600, 
                                    color=ACCENT_PINK, 
                                    style=ft.TextStyle(letter_spacing=1.5)
                                ),
                                ft.Text("Lavinia Ndilimeke Shimutwikeni", size=42, weight=ft.FontWeight.BOLD, color=PRIMARY_PINK),
                                ft.Divider(color=PRIMARY_PINK, thickness=1.5),
                                ft.Text("Phone: +264 81 360 9793  |  Email: shimutwikeni@gmail.com", size=14, weight=ft.FontWeight.W_500, color=DEEP_PINK),
                                ft.Text("Mining Engineering student specializing in Mine Safety Systems, Industrial Automation, Sensor Networks, MATLAB/Simulink, and Smart Monitoring Technologies for mining operations. Passionate about developing intelligent engineering solutions for safety-critical mining environments.", size=16, color=TEXT_GREY),
                                ft.Container(height=10),
                                ft.ElevatedButton(
                                    "Download CV (PDF)",
                                    icon=ft.Icons.DOWNLOAD,
                                    bgcolor=PRIMARY_PINK,
                                    color=BG_WHITE,
                                    url="/cv.pdf",
                                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=6)),
                                ),
                            ],
                        ),
                        ft.Column(
                            col={"sm": 12, "md": 5},
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Container(
                                    width=220,
                                    height=220,
                                    border_radius=110,
                                    bgcolor=AVATAR_BG,
                                    alignment=ft.Alignment(0, 0),
                                    border=get_uniform_border(4, PRIMARY_PINK),
                                    content=ft.Image(src=IMAGES["profile"], width=220, height=220, border_radius=110, fit="cover"),
                                ),
                                ft.Container(height=8),
                                ft.Text("Mining Engineering - Class of 2026", size=12, color=SUBTEXT_GREY, italic=True),
                            ],
                        ),
                    ]
                ),
                
                # Quick Stats Row
                ft.ResponsiveRow(
                    spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 3},
                            bgcolor=BG_WHITE,
                            padding=15,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=5,
                                controls=[
                                    ft.Icon(ft.Icons.SCHOOL, color=PRIMARY_PINK, size=32),
                                    ft.Text("3+", size=24, weight=ft.FontWeight.BOLD, color=PRIMARY_PINK),
                                    ft.Text("Years of Study", size=12, color=TEXT_GREY),
                                ]
                            )
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 3},
                            bgcolor=BG_WHITE,
                            padding=15,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=5,
                                controls=[
                                    ft.Icon(ft.Icons.CODE, color=PRIMARY_PINK, size=32),
                                    ft.Text("8+", size=24, weight=ft.FontWeight.BOLD, color=PRIMARY_PINK),
                                    ft.Text("MATLAB Certifications", size=12, color=TEXT_GREY),
                                ]
                            )
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 3},
                            bgcolor=BG_WHITE,
                            padding=15,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=5,
                                controls=[
                                    ft.Icon(ft.Icons.WORK, color=PRIMARY_PINK, size=32),
                                    ft.Text("5+", size=24, weight=ft.FontWeight.BOLD, color=PRIMARY_PINK),
                                    ft.Text("Projects Completed", size=12, color=TEXT_GREY),
                                ]
                            )
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 3},
                            bgcolor=BG_WHITE,
                            padding=15,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=5,
                                controls=[
                                    ft.Icon(ft.Icons.GROUP, color=PRIMARY_PINK, size=32),
                                    ft.Text("16", size=24, weight=ft.FontWeight.BOLD, color=PRIMARY_PINK),
                                    ft.Text("Team Members", size=12, color=TEXT_GREY),
                                ]
                            )
                        ),
                    ]
                ),
                
                # Education Section
                ft.Container(
                    bgcolor=BG_WHITE,
                    padding=20,
                    border_radius=8,
                    border=get_uniform_border(1, BORDER_COLOR),
                    content=ft.Column(
                        spacing=10,
                        controls=[
                            ft.Row([
                                ft.Icon(ft.Icons.SCHOOL, color=PRIMARY_PINK, size=24),
                                ft.Text("Education", size=18, weight=ft.FontWeight.BOLD, color=DEEP_PINK),
                            ]),
                            ft.Text("• Bachelor of Engineering in Mining Engineering", size=14, weight=ft.FontWeight.W_500, color=TEXT_GREY),
                            ft.Text("  University of Namibia (UNAM) | 2023 - Present", size=13, color=SUBTEXT_GREY),
                            ft.Text("• Relevant Coursework: Mine Safety Systems, Mine Ventilation, Rock Mechanics, Mineral Processing, Mining Methods, Industrial Automation, Sensor Networks, MATLAB/Simulink", size=13, color=TEXT_GREY),
                        ]
                    )
                ),
                
                # Research Interests & Goals
                ft.ResponsiveRow(
                    spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=10,
                                controls=[
                                    ft.Row([
                                        ft.Icon(ft.Icons.SCIENCE, color=PRIMARY_PINK, size=24),
                                        ft.Text("Research Interests", size=16, weight=ft.FontWeight.BOLD, color=DEEP_PINK),
                                    ]),
                                    ft.Text("• Smart Mining Systems", size=13, color=TEXT_GREY),
                                    ft.Text("• Mine Safety & Automation", size=13, color=TEXT_GREY),
                                    ft.Text("• Mine Ventilation Monitoring", size=13, color=TEXT_GREY),
                                    ft.Text("• Embedded Electronics for Mining", size=13, color=TEXT_GREY),
                                    ft.Text("• IoT Sensor Networks in Mines", size=13, color=TEXT_GREY),
                                ]
                            )
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=10,
                                controls=[
                                    ft.Row([
                                        ft.Icon(ft.Icons.FLAG, color=PRIMARY_PINK, size=24),
                                        ft.Text("Career Goals", size=16, weight=ft.FontWeight.BOLD, color=DEEP_PINK),
                                    ]),
                                    ft.Text("• Become a Professional Mining Engineer", size=13, color=TEXT_GREY),
                                    ft.Text("• Design Intelligent Mine Safety Systems", size=13, color=TEXT_GREY),
                                    ft.Text("• Contribute to Mine Safety Innovation", size=13, color=TEXT_GREY),
                                    ft.Text("• Pursue Advanced Research in Mine Automation", size=13, color=TEXT_GREY),
                                    ft.Text("• Lead Smart Mining Infrastructure Projects", size=13, color=TEXT_GREY),
                                ]
                            )
                        ),
                    ]
                ),
                
                # Technical Skills Highlight
                ft.Container(
                    bgcolor=BG_WHITE,
                    padding=20,
                    border_radius=8,
                    border=get_uniform_border(1, BORDER_COLOR),
                    content=ft.Column(
                        spacing=10,
                        controls=[
                            ft.Row([
                                ft.Icon(ft.Icons.SETTINGS, color=PRIMARY_PINK, size=24),
                                ft.Text("Technical Skills Snapshot", size=18, weight=ft.FontWeight.BOLD, color=DEEP_PINK),
                            ]),
                            ft.ResponsiveRow(
                                spacing=10,
                                controls=[
                                    ft.Container(col={"sm": 12, "md": 4}, content=ft.Row([ft.Icon(ft.Icons.CHECK_CIRCLE, color=ACCENT_PINK, size=16), ft.Text("MATLAB/Simulink", size=13, color=TEXT_GREY)])),
                                    ft.Container(col={"sm": 12, "md": 4}, content=ft.Row([ft.Icon(ft.Icons.CHECK_CIRCLE, color=ACCENT_PINK, size=16), ft.Text("PLC & SCADA", size=13, color=TEXT_GREY)])),
                                    ft.Container(col={"sm": 12, "md": 4}, content=ft.Row([ft.Icon(ft.Icons.CHECK_CIRCLE, color=ACCENT_PINK, size=16), ft.Text("Mine Ventilation", size=13, color=TEXT_GREY)])),
                                    ft.Container(col={"sm": 12, "md": 4}, content=ft.Row([ft.Icon(ft.Icons.CHECK_CIRCLE, color=ACCENT_PINK, size=16), ft.Text("Python Programming", size=13, color=TEXT_GREY)])),
                                    ft.Container(col={"sm": 12, "md": 4}, content=ft.Row([ft.Icon(ft.Icons.CHECK_CIRCLE, color=ACCENT_PINK, size=16), ft.Text("Microcontroller Programming", size=13, color=TEXT_GREY)])),
                                    ft.Container(col={"sm": 12, "md": 4}, content=ft.Row([ft.Icon(ft.Icons.CHECK_CIRCLE, color=ACCENT_PINK, size=16), ft.Text("Sensor Networks", size=13, color=TEXT_GREY)])),
                                    ft.Container(col={"sm": 12, "md": 4}, content=ft.Row([ft.Icon(ft.Icons.CHECK_CIRCLE, color=ACCENT_PINK, size=16), ft.Text("Git / GitHub", size=13, color=TEXT_GREY)])),
                                    ft.Container(col={"sm": 12, "md": 4}, content=ft.Row([ft.Icon(ft.Icons.CHECK_CIRCLE, color=ACCENT_PINK, size=16), ft.Text("React Native", size=13, color=TEXT_GREY)])),
                                ]
                            )
                        ]
                    )
                ),
                
                # Achievements & Awards
                ft.Container(
                    bgcolor=BG_WHITE,
                    padding=20,
                    border_radius=8,
                    border=get_uniform_border(1, BORDER_COLOR),
                    content=ft.Column(
                        spacing=10,
                        controls=[
                            ft.Row([
                                ft.Icon(ft.Icons.EMOJI_EVENTS, color=PRIMARY_PINK, size=24),
                                ft.Text("Achievements & Awards", size=18, weight=ft.FontWeight.BOLD, color=DEEP_PINK),
                            ]),
                            ft.Text("• Completed 8+ MATLAB Certification Courses from MathWorks", size=13, color=TEXT_GREY),
                            ft.Text("• Dean's List Recognition for Academic Excellence (2024)", size=13, color=TEXT_GREY),
                            ft.Text("• Participant in National Mining Engineering Design Competition", size=13, color=TEXT_GREY),
                            ft.Text("• Peer Tutor for Mine Safety and Automation Systems", size=13, color=TEXT_GREY),
                            ft.Text("• Member of Mining Engineering Student Society", size=13, color=TEXT_GREY),
                        ]
                    )
                ),
                
                # Download CV Button Row
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20,
                    controls=[
                        ft.ElevatedButton(
                            "Download Full CV",
                            icon=ft.Icons.DOWNLOAD,
                            bgcolor=PRIMARY_PINK,
                            color=BG_WHITE,
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=6)),
                        ),
                        ft.OutlinedButton(
                            "Contact Me",
                            icon=ft.Icons.EMAIL,
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=6)),
                            on_click=lambda e: navigate_to("contact"),
                        ),
                    ]
                ),
            ]
        ),
    )

    # 2. Skills Section - Mining Focus
    skills_section = ft.Container(
        key="skills",
        bgcolor=SECTION_PINK,
        padding=40,
        content=ft.Column([
            create_section_header("CORE MINING & TECHNICAL MATRIX", "Core expertise across mine safety systems, industrial automation, control systems, and modern mining engineering tools."),
            ft.ResponsiveRow([
                ft.Column(col={"sm": 12, "md": 4}, spacing=10, controls=[
                    ft.Text("Mine Safety & Systems", weight=ft.FontWeight.BOLD, color=ACCENT_PINK, size=16),
                    create_skill_chip("Mine Safety Systems", 0.90),
                    create_skill_chip("Mine Ventilation", 0.88),
                    create_skill_chip("Rock Mechanics", 0.85),
                    create_skill_chip("Mine Rescue Systems", 0.82),
                ]),
                ft.Column(col={"sm": 12, "md": 4}, spacing=10, controls=[
                    ft.Text("Automation & Control", weight=ft.FontWeight.BOLD, color=ACCENT_PINK, size=16),
                    create_skill_chip("PLC Programming", 0.89),
                    create_skill_chip("SCADA Systems", 0.86),
                    create_skill_chip("Industrial Automation", 0.84),
                    create_skill_chip("Control Systems", 0.88),
                ]),
                ft.Column(col={"sm": 12, "md": 4}, spacing=10, controls=[
                    ft.Text("Embedded & Digital Tools", weight=ft.FontWeight.BOLD, color=ACCENT_PINK, size=16),
                    create_skill_chip("MATLAB/Simulink", 0.87),
                    create_skill_chip("Python", 0.80),
                    create_skill_chip("Embedded Systems", 0.85),
                    create_skill_chip("Sensor Networks", 0.83),
                ]),
            ], spacing=20)
        ])
    )

    # 3. Individual Portfolio Reflection Section - MineOps Focus (NO VIDEO)
    contribution_section = ft.Container(
        key="contribution",
        bgcolor=LIGHT_BG,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("INDIVIDUAL CONTRIBUTION PORTFOLIO", "Reflection, evidence, lessons learned, challenges, and showcase material from MineOps project."),
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            content=create_info_card(
                                "MineOps Project Contribution",
                                "As a Lead Developer on the MineOps team, I contributed to the React Native application development, hazard reporting system implementation, Firebase integration, and safety monitoring features.",
                                ft.Icons.ENGINEERING,
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            content=create_info_card(
                                "Evidence of Work",
                                "Portfolio contains system screenshots, MATLAB analyses, testing records, APK demonstrations, GitHub activity, and mining engineering documentation.",
                                ft.Icons.FACT_CHECK,
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            content=create_info_card(
                                "What I Learned",
                                "Developed practical skills in React Native mobile development, Firebase real-time database integration, collaborative software development, and mine safety system design.",
                                ft.Icons.LIGHTBULB,
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            content=create_info_card(
                                "Challenges Addressed",
                                "Ensuring reliable real-time hazard reporting between workers and supervisors while maintaining mine safety compliance and system integrity in remote mining locations.",
                                ft.Icons.TROUBLESHOOT,
                            ),
                        ),
                    ],
                ),
            ],
        ),
    )

    # 4. Timeline Section - MineOps focused
    timeline_section = ft.Container(
        key="timeline",
        bgcolor=LIGHT_BG,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("PROJECT TIMELINE", "Weekly log of my specific contributions to the MineOps project."),
                ft.Container(
                    bgcolor=BG_WHITE,
                    padding=25,
                    border_radius=10,
                    border=get_uniform_border(1, BORDER_COLOR),
                    content=ft.Column(
                        spacing=15,
                        controls=[
                            ft.Text("Week 01 - Requirements Gathering and Firebase Setup", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_PINK),
                            ft.Text("Reviewed the semester brief for MineOps project, mapped requirements, and set up Firebase Realtime Database for hazard data synchronization.", color=TEXT_GREY),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Text("Week 02 - Hazard Reporting Interface Development", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_PINK),
                            ft.Text("Developed the hazard reporting form interface, implemented real-time data submission, and integrated with Firebase database.", color=TEXT_GREY),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Text("Week 03 - Supervisor Dashboard and Emergency Contact Integration", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_PINK),
                            ft.Text("Created supervisor dashboard for monitoring hazards, integrated emergency contact system, and implemented real-time notifications.", color=TEXT_GREY),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Text("Week 04 - Final MineOps Integration and Testing", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_PINK),
                            ft.Text("Completed final system integration, conducted comprehensive testing, prepared documentation, and aligned portfolio for presentation showcase.", color=TEXT_GREY),
                        ],
                    ),
                ),
            ],
        ),
    )

    # 5. MineOps Projects Section
    project_section = ft.Container(
        key="projects",
        bgcolor=BG_WHITE,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("MINEOPS PROJECTS", "Advanced monitoring solutions for mining environments."),
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=CARD_BG,
                            padding=25,
                            border_radius=10,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=12,
                                controls=[
                                    ft.Row([
                                        ft.Image(src=IMAGES["mineops_logo"], width=40, height=40, fit="contain"),
                                        ft.Text("1. MineOps Mobile Application", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_PINK),
                                    ]),
                                    ft.Text("React Native mobile application designed to improve safety and communication in mining operations. Replaces paper-based hazard logs with a real-time digital platform.", color=TEXT_GREY, size=14),
                                    ft.Container(
                                        bgcolor=LIGHT_BG,
                                        padding=12,
                                        border_radius=6,
                                        content=ft.Column([
                                            ft.Text("TECHNOLOGY STACK:", size=11, weight=ft.FontWeight.BOLD, color=DEEP_PINK),
                                            ft.Text("• React Native for cross-platform mobile development", size=12, font_family="monospace", color=ACCENT_PINK),
                                            ft.Text("• Firebase Realtime Database for instant synchronization", size=12, font_family="monospace", color=ACCENT_PINK),
                                            ft.Text("• JavaScript/TypeScript for application logic", size=12, font_family="monospace", color=ACCENT_PINK),
                                            ft.Text("• GitHub for version control and collaboration", size=12, font_family="monospace", color=ACCENT_PINK),
                                        ])
                                    ),
                                    ft.Text("Enables mine workers to report hazards in real-time and supervisors to monitor safety conditions efficiently from anywhere.", color=TEXT_GREY, size=12),
                                    ft.Row([
                                        ft.Container(content=ft.Text("React Native", size=11, color=BG_WHITE), bgcolor=PRIMARY_PINK, padding=5, border_radius=4),
                                        ft.Container(content=ft.Text("Firebase", size=11, color=DEEP_PINK), bgcolor=LIGHT_BG, padding=5, border_radius=4),
                                        ft.Container(content=ft.Text("JavaScript", size=11, color=DEEP_PINK), bgcolor=LIGHT_BG, padding=5, border_radius=4),
                                    ])
                                ],
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=CARD_BG,
                            padding=25,
                            border_radius=10,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=12,
                                controls=[
                                    ft.Row([
                                        ft.Icon(ft.Icons.SENSORS, color=ACCENT_PINK, size=30),
                                        ft.Text("2. Mine Safety Sensor Network", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_PINK),
                                    ]),
                                    ft.Text("IoT sensor network design for environmental monitoring in mining operations using ESP32-based nodes.", color=TEXT_GREY, size=14),
                                    ft.Container(
                                        bgcolor=LIGHT_BG,
                                        padding=12,
                                        border_radius=6,
                                        content=ft.Column([
                                            ft.Text("HARDWARE COMPONENTS:", size=11, weight=ft.FontWeight.BOLD, color=DEEP_PINK),
                                            ft.Text("• MQ-7 Gas Sensor for CO detection", size=12, font_family="monospace", color=ACCENT_PINK),
                                            ft.Text("• DHT22 Temperature/Humidity sensor", size=12, font_family="monospace", color=ACCENT_PINK),
                                            ft.Text("• ADXL345 Vibration sensor for ground stability", size=12, font_family="monospace", color=ACCENT_PINK),
                                            ft.Text("• ESP32 Controller with WiFi/BLE", size=12, font_family="monospace", color=ACCENT_PINK),
                                        ])
                                    ),
                                    ft.Text("Enables continuous mine environmental monitoring with early warning capabilities for hazardous gas levels and ground instability detection.", color=TEXT_GREY, size=12),
                                    ft.Row([
                                        ft.Container(content=ft.Text("ESP32", size=11, color=BG_WHITE), bgcolor=PRIMARY_PINK, padding=5, border_radius=4),
                                        ft.Container(content=ft.Text("IoT Sensors", size=11, color=DEEP_PINK), bgcolor=LIGHT_BG, padding=5, border_radius=4),
                                        ft.Container(content=ft.Text("Embedded C", size=11, color=DEEP_PINK), bgcolor=LIGHT_BG, padding=5, border_radius=4),
                                    ])
                                ],
                            ),
                        ),
                    ],
                ),
            ],
        ),
    )

    # 6. Technical Blog Section - Mining Engineering focus with VIDEO
    blog_section = ft.Container(
        key="blog",
        bgcolor=LIGHT_BG,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("TECHNICAL BLOG: MINING ENGINEERING INSIGHTS", "Written technical explanations with embedded video demonstrations."),
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=22,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=12,
                                controls=[
                                    ft.Text("Understanding Mine Ventilation Systems", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_PINK),
                                    ft.Text("Application of fundamental principles in mine ventilation and air quality management for miner safety.", color=TEXT_GREY, size=13),
                                    ft.Container(
                                        bgcolor=LIGHT_BG,
                                        padding=14,
                                        border_radius=6,
                                        content=ft.Text("Q = A × V   |   Pressure Drop = R × Q²   |   Mine Airflow = Σ (Sections)", font_family="monospace", size=14, color=PRIMARY_PINK),
                                    ),
                                    ft.Text("Understanding these relationships is crucial for mine ventilation planning, gas detection systems, and miner safety in underground operations.", color=TEXT_GREY, size=13),
                                ],
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=22,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=12,
                                controls=[
                                    ft.Text("MineOps Project Demonstration", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_PINK),
                                    ft.Text("Video showcase of the MineOps monitoring system in action.", color=TEXT_GREY, size=13),
                                    ft.Container(
                                        content=ftv.Video(
                                            expand=True,
                                            playlist=[ftv.VideoMedia("/video/video.mp4")],
                                            playlist_mode=ftv.PlaylistMode.LOOP,
                                            fill_color=ACCENT_PINK,
                                            aspect_ratio=16/9,
                                            volume=100,
                                            autoplay=True,
                                            show_controls=True,
                                            filter_quality=ft.FilterQuality.HIGH,
                                            muted=False,
                                            wakelock=True,
                                        ),
                                        border_radius=8,
                                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                                    ),
                                    ft.Text("Watch the full demonstration of sensor integration, dashboard monitoring, and alert systems for mining safety.", color=TEXT_GREY, size=12),
                                ],
                            ),
                        ),
                    ],
                ),
            ],
        ),
    )

    # 7. Experience / Leadership Section - Mining Engineering focus
    leadership_section = ft.Container(
        key="experience",
        bgcolor=LIGHT_BG,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("MINING ENGINEERING LEADERSHIP & EXPERIENCE", "Active contributions to mining engineering community and practical industry exposure."),
                ft.Text("Bridging academic mining engineering theory with practical industry applications while developing innovative mine safety solutions.", size=15, color=TEXT_GREY),
                ft.ResponsiveRow(
                    spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 4},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column([
                                ft.Icon(ft.Icons.GROUP, color=PRIMARY_PINK, size=28),
                                ft.Text("Mining Engineering Society", size=16, weight=ft.FontWeight.BOLD, color=DEEP_PINK),
                                ft.Text("Active member contributing to workshops, industry guest lectures, and technical seminars on emerging mining technologies.", color=TEXT_GREY, size=13),
                            ])
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 4},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column([
                                ft.Icon(ft.Icons.SETTINGS, color=PRIMARY_PINK, size=28),
                                ft.Text("MineOps Lead Developer", size=16, weight=ft.FontWeight.BOLD, color=DEEP_PINK),
                                ft.Text("Core contributor to MineOps mobile application development, Firebase integration, testing, and documentation.", color=TEXT_GREY, size=13),
                            ])
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 4},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column([
                                ft.Icon(ft.Icons.SCHOOL, color=PRIMARY_PINK, size=28),
                                ft.Text("MathWorks Self-Paced Learning", size=16, weight=ft.FontWeight.BOLD, color=DEEP_PINK),
                                ft.Text("Completed comprehensive MATLAB and Simulink certification courses to enhance computational engineering capabilities.", color=TEXT_GREY, size=13),
                            ])
                        ),
                    ]
                )
            ]
        )
    )

    # 8. MATLAB Achievement Hub Section - Updated with actual certificate images
    certificate_data = [
        {"title": "MATLAB Onramp", "image": IMAGES["matlab_onramp"]},
        {"title": "Simulink Onramp", "image": IMAGES["simulink_onramp"]},
        {"title": "Calculations with Vectors and Matrices", "image": IMAGES["calculations_vectors"]},
        {"title": "Explore Data with MATLAB Plots", "image": IMAGES["explore_data"]},
        {"title": "Make and Manipulate Matrices", "image": IMAGES["manipulate_matrices"]},
        {"title": "Regression with Deep Learning", "image": IMAGES["regression_deep"]},
        {"title": "Signal Segmentation with Deep Learning", "image": IMAGES["signal_segmentation"]},
    ]

    cert_cards = []
    for cert in certificate_data:
        img_control = ft.Image(
            src=cert["image"],
            height=150,
            fit="contain", 
            scale=1.0,
            animate_scale=ft.Animation(400, ft.AnimationCurve.EASE_OUT),
        )

        card_design = ft.Container(
            bgcolor=DARK_CARD_BG,
            padding=15,
            border_radius=10,
            border=get_uniform_border(1, ACCENT_PINK),
            on_click=lambda e, title=cert["title"], img_src=cert["image"]: open_certificate_zoom(title, img_src),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        height=150,
                        width=320,
                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                        border_radius=6,
                        bgcolor=BG_WHITE,
                        alignment=ft.Alignment(0, 0),
                        content=img_control,
                    ),
                    ft.Container(height=6),
                    ft.Text(cert["title"], weight=ft.FontWeight.BOLD, color=DARK_TEXT_WHITE, text_align=ft.TextAlign.CENTER, size=13, max_lines=2, overflow=ft.TextOverflow.ELLIPSIS),
                    ft.Text("Click to zoom", color=CERT_HINT, size=11, text_align=ft.TextAlign.CENTER),
                ],
            ),
        )

        hover_stack = ft.Stack(
            height=230,
            controls=[
                ft.Container(top=10, left=0, right=0, animate_position=ft.Animation(300, ft.AnimationCurve.EASE_OUT), content=card_design)
            ]
        )

        def make_hover_handler(stack_wrapper, target_img):
            inner_move_container = stack_wrapper.controls[0]
            def handle_hover(e):
                if e.data == "true":
                    inner_move_container.top = 0  
                    inner_move_container.shadow = ft.BoxShadow(blur_radius=12, color=ACCENT_PINK)
                    target_img.scale = 1.05  
                else:
                    inner_move_container.top = 10  
                    inner_move_container.shadow = None
                    target_img.scale = 1.0
                inner_move_container.update()
                target_img.update()
            return handle_hover

        card_design.on_hover = make_hover_handler(hover_stack, img_control)
        cert_cards.append(ft.Container(col={"sm": 12, "md": 4}, content=hover_stack))

    certification_section = ft.Container(
        key="certificates",
        bgcolor=SECTION_DEEP,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("MATLAB & SIMULINK CERTIFICATIONS", "Proof of completion for self-paced courses from MathWorks Learning Center."),
                ft.Text("Click any certificate to zoom in and inspect the completion proof clearly.", size=13, color=SUBTEXT_GREY),
                ft.ResponsiveRow(spacing=20, run_spacing=10, controls=cert_cards),
            ],
        ),
    )

    # 9. GitHub Evidence & Documentation Section
    github_section = ft.Container(
        key="github",
        bgcolor=LIGHT_BG,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Column([
                            ft.Text("GITHUB EVIDENCE & DOCUMENTATION", size=28, weight=ft.FontWeight.BOLD, color=PRIMARY_PINK),
                            ft.Text("Verifiable individual contribution records for MineOps project development.", size=15, color=TEXT_GREY),
                        ]),
                        ft.IconButton(icon=ft.Icons.CODE, icon_color=PRIMARY_PINK, tooltip="GitHub Evidence")
                    ]
                ),
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 4},
                            content=create_info_card(
                                "Commit History",
                                "Screenshots showing commits authored by Lavinia Shimutwikeni in the MineOps repository, including dates, messages, and linked files.",
                                ft.Icons.COMMIT,
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 4},
                            content=create_info_card(
                                "Pull Request Logs",
                                "Documentation of proposed features, reviews performed, comments resolved, and merges completed during MineOps development.",
                                ft.Icons.MERGE,
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 4},
                            content=create_info_card(
                                "Impact Summary",
                                "My code and documentation improved hazard reporting functionality, sensor integration, dashboard monitoring, and explained mining engineering outputs for compliance.",
                                ft.Icons.INSIGHTS,
                            ),
                        ),
                    ],
                ),
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=10,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=12,
                                controls=[
                                    ft.Row([ft.Icon(ft.Icons.FOLDER_SPECIAL, color=PRIMARY_PINK), ft.Text("MineOps-App", size=16, weight=ft.FontWeight.BOLD, color=DEEP_PINK)]),
                                    ft.Text("React Native mobile application for mining safety with real-time hazard reporting and Firebase integration.", size=13, color=TEXT_GREY),
                                    ft.Row(wrap=True, spacing=5, controls=[
                                        ft.Container(content=ft.Text("React Native", size=10, color=BG_WHITE), bgcolor=PRIMARY_PINK, padding=4, border_radius=4),
                                        ft.Container(content=ft.Text("Firebase", size=10, color=DEEP_PINK), bgcolor=LIGHT_BG, padding=4, border_radius=4),
                                        ft.Container(content=ft.Text("JavaScript", size=10, color=DEEP_PINK), bgcolor=LIGHT_BG, padding=4, border_radius=4),
                                    ]),
                                    ft.Divider(color=BORDER_COLOR),
                                    ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
                                        ft.Text("Active Development", size=11, color=SUBTEXT_GREY),
                                        ft.TextButton("View Repository", style=ft.ButtonStyle(color=ACCENT_PINK), on_click=lambda e: page.launch_url("https://github.com/makotajr06/UNAM-I3691CP-SyntaxCrew-MineOps"))
                                    ])
                                ]
                            )
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=10,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=12,
                                controls=[
                                    ft.Row([ft.Icon(ft.Icons.FOLDER, color=PRIMARY_PINK), ft.Text("MineOps-Sensor-Network", size=16, weight=ft.FontWeight.BOLD, color=DEEP_PINK)]),
                                    ft.Text("ESP32-based sensor network for mine environmental monitoring with gas, temperature, and vibration sensors.", size=13, color=TEXT_GREY),
                                    ft.Row(wrap=True, spacing=5, controls=[
                                        ft.Container(content=ft.Text("Embedded C", size=10, color=BG_WHITE), bgcolor=PRIMARY_PINK, padding=4, border_radius=4),
                                        ft.Container(content=ft.Text("ESP32", size=10, color=DEEP_PINK), bgcolor=LIGHT_BG, padding=4, border_radius=4),
                                    ]),
                                    ft.Divider(color=BORDER_COLOR),
                                    ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
                                        ft.Text("Stable Release", size=11, color=SUBTEXT_GREY),
                                        ft.TextButton("View Repository", style=ft.ButtonStyle(color=ACCENT_PINK))
                                    ])
                                ]
                            )
                        ),
                    ],
                ),
            ],
        ),
    )

    # =========================================================
    # MINEOPS DEDICATION SECTION
    # =========================================================
    mineops_section = ft.Container(
        key="mineops",
        bgcolor=MINEOPS_PINK,
        padding=50,
        content=ft.Column(
            spacing=25,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Image(src=IMAGES["mineops_logo"], width=80, height=80, fit="contain"),
                ft.Text(
                    "⚒️ DEDICATED TO MINEOPS ⚒️",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    color=BG_WHITE,
                    text_align=ft.TextAlign.CENTER,
                    style=ft.TextStyle(letter_spacing=2),
                ),
                ft.Container(
                    width=100,
                    height=3,
                    bgcolor=MINEOPS_GOLD,
                    border_radius=2,
                ),
                ft.Text(
                    "This portfolio is proudly dedicated to the MineOps project —",
                    size=18,
                    color=BG_WHITE,
                    text_align=ft.TextAlign.CENTER,
                    weight=ft.FontWeight.W_500,
                ),
                ft.Text(
                    "an innovative initiative revolutionizing mining safety through intelligent monitoring systems, real-time hazard detection, and advanced industrial automation.",
                    size=16,
                    color="#ffe0f0",
                    text_align=ft.TextAlign.CENTER,
                    italic=True,
                ),
                ft.Container(height=10),
                ft.ResponsiveRow(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=30,
                    controls=[
                        ft.Container(
                            bgcolor=MINEOPS_GOLD,
                            padding=ft.Padding(20, 10, 20, 10),
                            border_radius=8,
                            content=ft.Text(
                                "🔗 MineOps Repository",
                                size=14,
                                weight=ft.FontWeight.BOLD,
                                color=DEEP_PINK,
                            ),
                            on_click=lambda e: page.launch_url("https://github.com/makotajr06/UNAM-I3691CP-SyntaxCrew-MineOps"),
                        ),
                        ft.Container(
                            bgcolor=BG_WHITE,
                            padding=ft.Padding(20, 10, 20, 10),
                            border_radius=8,
                            content=ft.Text(
                                "🏗️ SyntaxCrew Team",
                                size=14,
                                weight=ft.FontWeight.BOLD,
                                color=PRIMARY_PINK,
                            ),
                            on_click=lambda e: page.launch_url("https://github.com/makotajr06/UNAM-I3691CP-SyntaxCrew-MineOps"),
                        ),
                    ],
                ),
                ft.Container(height=20),
                ft.Text(
                    "© 2024 | Honoring the vision of safer, smarter mining operations",
                    size=12,
                    color="#ffe0f0",
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
        ),
    )

    # 10. Contact Section Form Setup
    name_field = ft.TextField(label="Your Full Name", border_color=PRIMARY_PINK, focused_border_color=ACCENT_PINK)
    email_field = ft.TextField(label="Email Address", border_color=PRIMARY_PINK, focused_border_color=ACCENT_PINK)
    message_field = ft.TextField(label="Project Details / Inquiry Message", multiline=True, min_lines=4, border_color=PRIMARY_PINK, focused_border_color=ACCENT_PINK)

    def handle_submit_message(e):
        if not name_field.value or not email_field.value:
            page.show_snack_bar(ft.SnackBar(content=ft.Text("Please fill out your Name and Email fields before submitting."), bgcolor=ACCENT_PINK))
        else:
            page.show_snack_bar(ft.SnackBar(content=ft.Text(f"Thank you {name_field.value}! Your message was compiled and sent successfully."), bgcolor=PRIMARY_PINK))
            name_field.value = ""
            email_field.value = ""
            message_field.value = ""
            page.update()

    contact_section = ft.Container(
        key="contact",
        bgcolor=BG_WHITE,
        padding=40,
        content=ft.Column([
            create_section_header("GET IN TOUCH", "Collaborate on mining engineering projects, automation systems, or mine safety monitoring solutions."),
            ft.ResponsiveRow(
                spacing=30,
                controls=[
                    ft.Column(
                        col={"sm": 12, "md": 5},
                        spacing=15,
                        controls=[
                            ft.Text("Available for Mining Engineering collaborations, automation projects, mine safety research, industrial monitoring solutions, and embedded systems development.", color=TEXT_GREY, size=15),
                            ft.Container(height=10),
                            ft.Row([ft.Icon(ft.Icons.LOCATION_ON, color=PRIMARY_PINK), ft.Text("Mining Engineering Campus, University of Namibia, Namibia", color=DEEP_PINK, weight=ft.FontWeight.W_500)]),
                            ft.Row([ft.Icon(ft.Icons.EMAIL, color=PRIMARY_PINK), ft.Text("shimutwikeni@gmail.com", color=DEEP_PINK, weight=ft.FontWeight.W_500)]),
                            ft.Row([ft.Icon(ft.Icons.PHONE, color=PRIMARY_PINK), ft.Text("+264 81 360 9793", color=DEEP_PINK, weight=ft.FontWeight.W_500)]),
                        ]
                    ),
                    ft.Container(
                        col={"sm": 12, "md": 7},
                        bgcolor=CARD_BG,
                        padding=30,
                        border_radius=12,
                        border=get_uniform_border(1, BORDER_COLOR),
                        content=ft.Column(
                            spacing=15,
                            controls=[
                                ft.Text("Send a Message Directly", size=16, weight=ft.FontWeight.BOLD, color=DEEP_PINK),
                                name_field, email_field, message_field,
                                ft.Container(height=5),
                                ft.ElevatedButton("Submit Message", icon=ft.Icons.SEND, bgcolor=PRIMARY_PINK, color=BG_WHITE, on_click=handle_submit_message, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=6))),
                                ft.Text(
                                    "I consent to having Lavinia Ndilimeke Shimutwikeni store my submitted information so that she can respond to my inquiry.",
                                    size=11,
                                    color=SUBTEXT_GREY,
                                ),
                            ]
                        )
                    )
                ]
            )
        ])
    )

    portfolio_pages = {
        "overview": hero_section,
        "skills": skills_section,
        "contribution": contribution_section,
        "timeline": timeline_section,
        "projects": project_section,
        "blog": blog_section,
        "experience": leadership_section,
        "certificates": certification_section,
        "github": github_section,
        "mineops": mineops_section,
        "contact": contact_section,
    }

    page_switcher = ft.AnimatedSwitcher(
        content=build_page_view(hero_section, "overview"),
        duration=220,
        reverse_duration=160,
        switch_in_curve=ft.AnimationCurve.EASE_OUT,
        switch_out_curve=ft.AnimationCurve.EASE_IN,
        transition=ft.AnimatedSwitcherTransition.FADE,
        expand=True,
    )

    def make_nav_button(label, page_key):
        button = ft.TextButton(
            label,
            style=ft.ButtonStyle(
                color=BG_WHITE if page_key == current_page_key["value"] else NAV_INACTIVE,
                overlay_color=OVERLAY_PINK,
            ),
            on_click=lambda e, target=page_key: navigate_to(target),
        )
        nav_buttons[page_key] = button
        return button

    # =========================================================
    # STICKY NAVBAR PANEL (Pinned permanently to top layer)
    # =========================================================
    header_navbar = ft.Container(
        bgcolor=PRIMARY_PINK,
        padding=ft.Padding(40, 15, 40, 15),
        border=ft.Border(bottom=ft.BorderSide(1, ACCENT_PINK)),
        shadow=ft.BoxShadow(blur_radius=10, color=SHADOW_PINK, offset=ft.Offset(0, 2)),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Row([
                    ft.Container(width=12, height=12, bgcolor=BG_WHITE, border_radius=6),
                    ft.Text("LAVINIA N SHIMUTWIKENI", weight=ft.FontWeight.BOLD, size=16, color=BG_WHITE, style=ft.TextStyle(letter_spacing=1.1))
                ], spacing=10),
                ft.Row([
                    make_nav_button("Overview", "overview"),
                    make_nav_button("Skills", "skills"),
                    make_nav_button("Portfolio", "contribution"),
                    make_nav_button("Timeline", "timeline"),
                    make_nav_button("Projects", "projects"),
                    make_nav_button("Blog", "blog"),
                    make_nav_button("Experience", "experience"),
                    make_nav_button("MATLAB Hub", "certificates"),
                    make_nav_button("GitHub", "github"),
                    make_nav_button("MineOps", "mineops"),
                    make_nav_button("Contact", "contact"),
                ], spacing=10, wrap=True)
            ]
        )
    )

    # =========================================================
    # RENDER DIRECT TO MAIN PAGE WINDOW
    # =========================================================
    page.add(
        ft.Column(
            expand=True,
            spacing=0,
            controls=[
                header_navbar,
                page_switcher
            ]
        )
    )

if __name__ == "__main__":
    ft.app(
        target=main,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000)),
        view=ft.AppView.WEB_BROWSER,
        assets_dir="assets",
    )