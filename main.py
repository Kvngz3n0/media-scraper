from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from scraper.scraper import start_scrape

class ScraperUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.url_input = TextInput(
            hint_text="Enter URL to scrape",
            size_hint_y=None,
            height=100
        )

        self.start_btn = Button(
            text="Start Scraping",
            size_hint_y=None,
            height=100
        )
        self.start_btn.bind(on_press=self.run)

        self.add_widget(self.url_input)
        self.add_widget(self.start_btn)

    def run(self, instance):
        start_scrape(self.url_input.text)

class MediaScraperApp(App):
    def build(self):
        return ScraperUI()

MediaScraperApp().run()