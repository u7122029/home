from flet import *

class MainPage:
    def __init__(self, page: Page):
        self._page = page
        self._page.title = "Callum Koh"

        self._nav = Row(alignment=MainAxisAlignment.END,
                        controls=[Container(padding=padding.only(right=21),
                                            height=64,
                                            content=Row(controls=[Container(on_hover=self.change_text_color,
                                                                            content=Text("About Me",
                                                                                         weight=FontWeight.W_600,
                                                                                         color="#475569")),
                                                                  Container(on_hover=self.change_text_color,
                                                                            content=Text("Contact",
                                                                                         weight=FontWeight.W_600,
                                                                                         color="#475569")),
                                                                  Container(on_hover=self.change_text_color,
                                                                            content=Text("Services",
                                                                                         weight=FontWeight.W_600,
                                                                                         color="#475569"))
                                                                  ]
                                                        )
                                            )
                                 ]
                        )

        self._title = ResponsiveRow(alignment=MainAxisAlignment.CENTER,
                                    controls=[Container(col={'xs': 6, 'sm': 10, 'md': 10, 'lg': 10, 'xl': 12},
                                                        alignment=alignment.top_center,
                                                        padding=20,
                                                        content=Text("Hi, I'm Callum.",
                                                                     size=45,
                                                                     weight=FontWeight.W_600,
                                                                     text_align=TextAlign.CENTER,
                                                                     color="white"
                                                                     )
                                                        )
                                              ]
                                    )

        self._min_nav = Row(visible=False,
                            controls=[PopupMenuButton(items=[PopupMenuItem(text="About Me"),
                                                             PopupMenuItem(text="Contact"),
                                                             PopupMenuItem(text="Services")
                                                             ]
                                                      )
                                      ]
                            )
        self._sub_title_text = "I'm a Software Engineer, Computer Science Enthusiast and a School Tutor.\nWelcome to my personal site!"
        self._sub_title = ResponsiveRow(alignment=MainAxisAlignment.CENTER,
                                        controls=[Container(col={'xs': 6, 'sm': 10, 'md': 10, 'lg': 10, 'xl': 12},
                                                            padding=20,
                                                            alignment=alignment.top_center,
                                                            content=Text(self._sub_title_text,
                                                                         text_align=TextAlign.CENTER,
                                                                         size=16,
                                                                         weight=FontWeight.W_500,
                                                                         color="white"
                                                                         )
                                                            )
                                                  ]
                                        )

        self._contact_row = Row(alignment=MainAxisAlignment.CENTER,
                                controls=[FilledButton("LinkedIn"),
                                          FilledButton("Email"),
                                          FilledButton("Discord")])

        self._main_col = Column(horizontal_alignment=CrossAxisAlignment.CENTER,
                                scroll=ScrollMode.AUTO
                                )

        self._main_col.controls.append(self._nav)
        self._main_col.controls.append(self._min_nav)
        self._main_col.controls.append(self._title)
        self._main_col.controls.append(self._sub_title)
        self._main_col.controls.append(self._contact_row)

        self._background = Container(expand=True,
                                     margin=-10,
                                     height=page.height,
                                     gradient=LinearGradient(begin=alignment.bottom_left,
                                                             end=alignment.top_right,
                                                             colors=["#13547a", "#0f172a"]),
                                     content=self._main_col
                                     )

        self._page.add(self._background)
        self._page.on_resized = self.on_resize

    def on_resize(self, e):
        if self._page.width <= 730:
            self._nav.controls[0].visible = False
            self._min_nav.visible = True
        else:
            self._nav.controls[0].visible = True
            self._min_nav.visible = False

        self._min_nav.update()
        self._nav.update()

    def change_text_color(self, e):
        if e.control.content.color == "#475569":
            e.control.content.color = "white70"
        else:
            e.control.content.color = "#475569"
        e.control.content.update()

app(target=MainPage)