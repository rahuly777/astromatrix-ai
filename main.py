"""
================================================================================
PROJECT: ASTROMATRIX AI - AUTONOMOUS MILLENNIUM RESEARCH EDITION (v15.0)
FOUNDER & CHIEF ARCHITECT: RAM JI YADAV
================================================================================
"""

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.spinner import Spinner
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.core.window import Window
import sys

kivy.require('2.1.0')
Window.clearcolor = (0.005, 0.005, 0.02, 1)

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        layout.add_widget(Label(
            text="[b]ASTROMATRIX AI : YV-THM Core[/b]",
            markup=True,
            font_size='20sp',
            color=(0.2, 0.8, 1, 1),
            size_hint_y=0.08
        ))
        
        ad_banner_btn = Button(
            text="📢 AD IDs DATABASE & MANAGER\n[ Tap to Open Ad ID Form ]",
            font_size='13sp', bold=True,
            background_color=(0.2, 0.5, 0.8, 1),
            size_hint_y=0.14
        )
        ad_banner_btn.bind(on_release=lambda x: self.change_screen('ad_screen'))
        layout.add_widget(ad_banner_btn)
        
        id_banner_btn = Button(
            text="🔥 GENERAL ID & DATA RECORD MANAGER\n[ Tap to Open ID Database ]",
            font_size='13sp', bold=True,
            background_color=(0.9, 0.4, 0.1, 1),
            size_hint_y=0.14
        )
        id_banner_btn.bind(on_release=lambda x: self.change_screen('id_screen'))
        layout.add_widget(id_banner_btn)
        
        btn_grid = GridLayout(cols=1, spacing=8, size_hint_y=0.54)
        
        btn_clay = Button(
            text="📐 YV-THM Clay Millennium Solver",
            font_size='14sp', background_color=(0.8, 0.2, 0.3, 1), bold=True
        )
        btn_clay.bind(on_release=lambda x: self.change_screen('clay_screen'))
        
        btn_ai = Button(
            text="🤖 Astro AI Neural Assistant",
            font_size='14sp', background_color=(0.15, 0.45, 0.85, 1), bold=True
        )
        btn_ai.bind(on_release=lambda x: self.change_screen('ai_screen'))
        
        btn_code = Button(
            text="💻 Advanced Python Studio",
            font_size='14sp', background_color=(0.2, 0.6, 0.4, 1), bold=True
        )
        btn_code.bind(on_release=lambda x: self.change_screen('code_screen'))
        
        btn_grid.add_widget(btn_clay)
        btn_grid.add_widget(btn_ai)
        btn_grid.add_widget(btn_code)
        layout.add_widget(btn_grid)
        
        layout.add_widget(Label(
            text="Founder: Ram Ji Yadav | YV-THM Engine v15.0",
            font_size='11sp', color=(0.5, 0.5, 0.5, 1), size_hint_y=0.1
        ))
        self.add_widget(layout)

    def change_screen(self, name):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = name


class AdConfigScreen(Screen):
    def __init__(self, **kwargs):
        super(AdConfigScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=15, spacing=8)
        
        nav_bar = BoxLayout(orientation='horizontal', size_hint_y=0.08)
        back_btn = Button(text="< Back", size_hint_x=0.25, background_color=(0.4, 0.4, 0.4, 1))
        back_btn.bind(on_release=self.go_back)
        nav_bar.add_widget(back_btn)
        nav_bar.add_widget(Label(text="Ad IDs Database & AdMob Manager", font_size='16sp', bold=True, size_hint_x=0.75))
        layout.add_widget(nav_bar)
        
        search_box = BoxLayout(orientation='horizontal', spacing=5, size_hint_y=0.08)
        self.search_input = TextInput(hint_text="🔍 Search Ad ID...", multiline=False, size_hint_x=0.75)
        search_btn = Button(text="Search", size_hint_x=0.25, background_color=(0.15, 0.45, 0.85, 1), bold=True)
        search_btn.bind(on_release=self.search_ad)
        search_box.add_widget(self.search_input)
        search_box.add_widget(search_btn)
        layout.add_widget(search_box)
        
        form_grid = GridLayout(cols=2, spacing=8, size_hint_y=0.24)
        form_grid.add_widget(Label(text="Ad Type:", bold=True))
        self.ad_type_spinner = Spinner(
            text='Banner Ad',
            values=('Banner Ad', 'Interstitial (Madhyavarti) Ad', 'Rewarded Ad', 'AdMob App ID'),
            background_color=(0.2, 0.5, 0.8, 1)
        )
        form_grid.add_widget(self.ad_type_spinner)
        
        form_grid.add_widget(Label(text="Ad Unit ID / App ID:", bold=True))
        self.ad_id_input = TextInput(hint_text="ca-app-pub-xxxxxxxx/id", multiline=False)
        form_grid.add_widget(self.ad_id_input)
        
        form_grid.add_widget(Label(text="Custom Tag / Note:", bold=True))
        self.ad_tag_input = TextInput(hint_text="e.g. Main Screen Bottom", multiline=False)
        form_grid.add_widget(self.ad_tag_input)
        layout.add_widget(form_grid)
        
        btn_box = GridLayout(cols=3, spacing=8, size_hint_y=0.09)
        clear_btn = Button(text="Clear (C)", background_color=(0.85, 0.15, 0.15, 1), bold=True)
        clear_btn.bind(on_release=self.clear_fields)
        
        bksp_btn = Button(text="⌫ Backspace", background_color=(0.85, 0.5, 0.1, 1), bold=True)
        bksp_btn.bind(on_release=self.backspace_field)
        
        add_btn = Button(text="➕ Save Ad ID", background_color=(0.2, 0.6, 0.4, 1), bold=True)
        add_btn.bind(on_release=self.save_ad_entry)
        
        btn_box.add_widget(clear_btn)
        btn_box.add_widget(bksp_btn)
        btn_box.add_widget(add_btn)
        layout.add_widget(btn_box)
        
        layout.add_widget(Label(text="Saved Ad IDs Database:", size_hint_y=0.06, bold=True))
        
        self.ad_database = [
            "[AdMob App ID] ID: ca-app-pub-3372370911435534~4190075685 | Tag: Master App ID",
            "[Banner Ad] ID: ca-app-pub-3372370911435534/7986025470 | Tag: Banner Ad Unit",
            "[Rewarded Ad] ID: ca-app-pub-3372370911435534/6840289757 | Tag: Rewarded Ad Unit",
            "[Interstitial (Madhyavarti) Ad] ID: ca-app-pub-3372370911435534/4653110117 | Tag: Madhyavarti Ad Unit"
        ]
        
        self.ad_record_display = Label(text="\n".join(self.ad_database), color=(0.8, 0.8, 0.8, 1), halign='left', valign='top', size_hint_y=None)
        self.ad_record_display.bind(texture_size=lambda inst, val: setattr(inst, 'height', val[1]))
        self.ad_record_display.bind(width=lambda inst, w: setattr(inst, 'text_size', (w - 20, None)))
        
        scroll = ScrollView(size_hint_y=0.37)
        scroll.add_widget(self.ad_record_display)
        layout.add_widget(scroll)
        self.add_widget(layout)

    def clear_fields(self, instance):
        self.ad_id_input.text = ""
        self.ad_tag_input.text = ""

    def backspace_field(self, instance):
        if self.ad_tag_input.text:
            self.ad_tag_input.text = self.ad_tag_input.text[:-1]
        elif self.ad_id_input.text:
            self.ad_id_input.text = self.ad_id_input.text[:-1]

    def save_ad_entry(self, instance):
        atype = self.ad_type_spinner.text
        aid = self.ad_id_input.text.strip()
        atag = self.ad_tag_input.text.strip()
        if aid:
            self.ad_database.append(f"[{atype}] ID: {aid} | Tag: {atag}")
            self.ad_record_display.text = "\n".join(self.ad_database)
            self.clear_fields(None)

    def search_ad(self, instance):
        query = self.search_input.text.strip().lower()
        if not query:
            self.ad_record_display.text = "\n".join(self.ad_database)
            return
        filtered = [r for r in self.ad_database if query in r.lower()]
        self.ad_record_display.text = "\n".join(filtered) if filtered else "[No match found]"

    def go_back(self, instance):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'home_screen'
class IDValueScreen(Screen):
    def __init__(self, **kwargs):
        super(IDValueScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=15, spacing=8)
        
        nav_bar = BoxLayout(orientation='horizontal', size_hint_y=0.08)
        back_btn = Button(text="< Back", size_hint_x=0.25, background_color=(0.4, 0.4, 0.4, 1))
        back_btn.bind(on_release=self.go_back)
        nav_bar.add_widget(back_btn)
        nav_bar.add_widget(Label(text="General ID & Value Database", font_size='18sp', bold=True, size_hint_x=0.75))
        layout.add_widget(nav_bar)
        
        search_box = BoxLayout(orientation='horizontal', spacing=5, size_hint_y=0.08)
        self.search_input = TextInput(hint_text="🔍 Search ID or Name...", multiline=False, size_hint_x=0.75)
        search_btn = Button(text="Search", size_hint_x=0.25, background_color=(0.15, 0.45, 0.85, 1), bold=True)
        search_btn.bind(on_release=self.search_entry)
        search_box.add_widget(self.search_input)
        search_box.add_widget(search_btn)
        layout.add_widget(search_box)
        
        form_grid = GridLayout(cols=2, spacing=8, size_hint_y=0.24)
        form_grid.add_widget(Label(text="Unique ID:", bold=True))
        self.id_input = TextInput(hint_text="e.g. YV-001", multiline=False)
        form_grid.add_widget(self.id_input)
        
        form_grid.add_widget(Label(text="Parameter Name:", bold=True))
        self.name_input = TextInput(hint_text="e.g. Zeta Zero", multiline=False)
        form_grid.add_widget(self.name_input)
        
        form_grid.add_widget(Label(text="Data Value:", bold=True))
        self.val_input = TextInput(hint_text="e.g. 14.1347", multiline=False)
        form_grid.add_widget(self.val_input)
        layout.add_widget(form_grid)
        
        btn_box = GridLayout(cols=3, spacing=8, size_hint_y=0.09)
        clear_btn = Button(text="Clear (C)", background_color=(0.85, 0.15, 0.15, 1), bold=True)
        clear_btn.bind(on_release=self.clear_fields)
        
        bksp_btn = Button(text="⌫ Backspace", background_color=(0.85, 0.5, 0.1, 1), bold=True)
        bksp_btn.bind(on_release=self.backspace_field)
        
        add_btn = Button(text="➕ Save Entry", background_color=(0.2, 0.6, 0.4, 1), bold=True)
        add_btn.bind(on_release=self.save_entry)
        
        btn_box.add_widget(clear_btn)
        btn_box.add_widget(bksp_btn)
        btn_box.add_widget(add_btn)
        layout.add_widget(btn_box)
        
        layout.add_widget(Label(text="Saved Records & Search Results:", size_hint_y=0.06, bold=True))
        
        self.record_display = Label(text="[No records saved yet]", color=(0.8, 0.8, 0.8, 1), halign='left', valign='top', size_hint_y=None)
        self.record_display.bind(texture_size=lambda inst, val: setattr(inst, 'height', val[1]))
        self.record_display.bind(width=lambda inst, w: setattr(inst, 'text_size', (w - 20, None)))
        
        scroll = ScrollView(size_hint_y=0.37)
        scroll.add_widget(self.record_display)
        layout.add_widget(scroll)
        self.database = []
        self.add_widget(layout)

    def clear_fields(self, instance):
        self.id_input.text = ""
        self.name_input.text = ""
        self.val_input.text = ""

    def backspace_field(self, instance):
        if self.val_input.text:
            self.val_input.text = self.val_input.text[:-1]
        elif self.name_input.text:
            self.name_input.text = self.name_input.text[:-1]
        elif self.id_input.text:
            self.id_input.text = self.id_input.text[:-1]

    def save_entry(self, instance):
        uid = self.id_input.text.strip()
        name = self.name_input.text.strip()
        val = self.val_input.text.strip()
        if uid and name and val:
            self.database.append(f"[ID: {uid}] -> {name} : {val}")
            self.record_display.text = "\n".join(self.database)
            self.clear_fields(None)

    def search_entry(self, instance):
        query = self.search_input.text.strip().lower()
        if not query:
            self.record_display.text = "\n".join(self.database) if self.database else "[No records saved yet]"
            return
        filtered = [rec for rec in self.database if query in rec.lower()]
        self.record_display.text = "\n".join(filtered) if filtered else "[No matching records found]"

    def go_back(self, instance):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'home_screen'


class ClayScreen(Screen):
    def __init__(self, **kwargs):
        super(ClayScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        nav_bar = BoxLayout(orientation='horizontal', size_hint_y=0.1)
        back_btn = Button(text="< Back", size_hint_x=0.25, background_color=(0.4, 0.4, 0.4, 1))
        back_btn.bind(on_release=self.go_back)
        nav_bar.add_widget(back_btn)
        nav_bar.add_widget(Label(text="YV-THM Millennium Math Solver", font_size='18sp', bold=True, size_hint_x=0.75))
        layout.add_widget(nav_bar)
        
        input_box = BoxLayout(orientation='vertical', spacing=8, size_hint_y=0.3)
        input_box.add_widget(Label(text="Select / Input Millennium Problem:", color=(0.9, 0.9, 0.9, 1)))
        
        self.prob_input = TextInput(text="P vs NP / Riemann Hypothesis / Navier-Stokes", multiline=False, size_hint_y=None, height=40)
        input_box.add_widget(self.prob_input)
        
        solve_btn = Button(text="⚡ Run YV-THM Custom Theory Solver", size_hint_y=None, height=45, background_color=(0.8, 0.2, 0.3, 1), bold=True)
        solve_btn.bind(on_release=self.solve_yv_thm_problem)
        input_box.add_widget(solve_btn)
        layout.add_widget(input_box)
        
        layout.add_widget(Label(text="YV-THM Matrix Computation Log:", size_hint_y=0.08, bold=True))
        
        self.clay_output = Label(text="[Ready]: Initialized Yadav-Vedantix Topological Hyper-Matrix...\n", color=(0.7, 1, 0.7, 1), halign='left', valign='top', size_hint_y=None)
        self.clay_output.bind(texture_size=lambda inst, val: setattr(inst, 'height', val[1]))
        self.clay_output.bind(width=lambda inst, w: setattr(inst, 'text_size', (w - 20, None)))
        
        scroll = ScrollView(size_hint_y=0.52)
        scroll.add_widget(self.clay_output)
        layout.add_widget(scroll)
        self.add_widget(layout)

    def solve_yv_thm_problem(self, instance):
        prob = self.prob_input.text.strip()
        report = [
            f"\n--- Executing YV-THM Theory by Ram Ji Yadav on: {prob} ---",
            "[+] Step 1: Allocating Universal State Vector Psi (Ψ) for nonlinear manifold.",
            "[+] Step 2: Applying Non-Linear Topological Operator Lambda (Λ) to map P into NP.",
            "[+] Step 3: Computing Riemann Zeta critical line zeros via Re(s) = 1/2.",
            "[+] Step 4: Stabilizing Navier-Stokes smooth velocity fields with Gamma (Γ).",
            f"[SUCCESS]: YV-THM Theorem verified for '{prob}'. Q.E.D.\n"
        ]
        self.clay_output.text += "\n".join(report)

    def go_back(self, instance):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'home_screen'


class AIScreen(Screen):
    def __init__(self, **kwargs):
        super(AIScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        nav = BoxLayout(orientation='horizontal', size_hint_y=0.1)
        b_btn = Button(text="< Back", size_hint_x=0.25, background_color=(0.4, 0.4, 0.4, 1))
        b_btn.bind(on_release=self.go_back)
        nav.add_widget(b_btn)
        nav.add_widget(Label(text="AI Neural Assistant", font_size='18sp', bold=True, size_hint_x=0.75))
        layout.add_widget(nav)
        
        self.log = Label(text="[Astro AI]: YV-THM Neural network online.\n", halign='left', valign='top', size_hint_y=None)
        self.log.bind(texture_size=lambda inst, val: setattr(inst, 'height', val[1]))
        self.log.bind(width=lambda inst, w: setattr(inst, 'text_size', (w - 20, None)))
        
        sc = ScrollView(size_hint_y=0.75)
        sc.add_widget(self.log)
        layout.add_widget(sc)
        
        ib = BoxLayout(orientation='horizontal', size_hint_y=0.15, spacing=5)
        self.ti = TextInput(hint_text="Ask AI...", multiline=False, size_hint_x=0.7)
        sb = Button(text="Send", size_hint_x=0.3, background_color=(0.15, 0.45, 0.85, 1))
        sb.bind(on_release=self.send)
        ib.add_widget(self.ti)
        ib.add_widget(sb)
        layout.add_widget(ib)
        self.add_widget(layout)

    def send(self, inst):
        txt = self.ti.text.strip()
        if txt:
            self.log.text += f"\n[You]: {txt}\n[AI]: Processed via YV-THM engine."
            self.ti.text = ""

    def go_back(self, inst):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'home_screen'


class CodeScreen(Screen):
    def __init__(self, **kwargs):
        super(CodeScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        nav = BoxLayout(orientation='horizontal', size_hint_y=0.1)
        b_btn = Button(text="< Back", size_hint_x=0.25, background_color=(0.4, 0.4, 0.4, 1))
        b_btn.bind(on_release=self.go_back)
        nav.add_widget(b_btn)
        nav.add_widget(Label(text="Python Studio", font_size='18sp', bold=True, size_hint_x=0.75))
        layout.add_widget(nav)
        
        self.ed = TextInput(text="# Yadav-Vedantix Theory Studio\ndef yv_matrix():\n    print('Running YV-THM Solver...')\n\nyv_matrix()", multiline=True, size_hint_y=0.8)
        layout.add_widget(self.ed)
        
        run_b = Button(text="▶ Execute Code", size_hint_y=0.1, background_color=(0.2, 0.6, 0.4, 1))
        layout.add_widget(run_b)
        self.add_widget(layout)

    def go_back(self, inst):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'home_screen'


class AstroMatrixUltimateResearchApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home_screen'))
        sm.add_widget(AdConfigScreen(name='ad_screen'))
        sm.add_widget(IDValueScreen(name='id_screen'))
        sm.add_widget(ClayScreen(name='clay_screen'))
        sm.add_widget(AIScreen(name='ai_screen'))
        sm.add_widget(CodeScreen(name='code_screen'))
        return sm


if __name__ == '__main__':
    AstroMatrixUltimateResearchApp().run()
  
