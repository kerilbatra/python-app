import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.metrics import dp


class HelmetApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(10))
        layout.background_color = (0.1, 0.1, 0.1, 1)

        # Create labels for instructions and battery status
        instructions_label = Label(
            text="Please follow these instructions to wear the helmet:",
            font_size=dp(24), bold=True, color=(1, 1, 1, 1))

        battery_label = Label(
            text="Helmet battery status: 100%", font_size=dp(16), color=(1, 1, 1, 0.7))

        # Create buttons for step-by-step instructions
        step1_button = Button(
            text="Step 1: Adjust the straps", font_size=dp(20),
            background_color=(0.2, 0.6, 0.9, 1), background_normal='',
            size_hint=(1, None), height=dp(60))
        step2_button = Button(
            text="Step 2: Secure the chin strap", font_size=dp(20),
            background_color=(0.2, 0.6, 0.9, 1), background_normal='',
            size_hint=(1, None), height=dp(60))
        step3_button = Button(
            text="Step 3: Ensure a snug fit", font_size=dp(20),
            background_color=(0.2, 0.6, 0.9, 1), background_normal='',
            size_hint=(1, None), height=dp(60))

        # Bind button clicks to corresponding functions
        step1_button.bind(on_release=self.step1_clicked)
        step2_button.bind(on_release=self.step2_clicked)
        step3_button.bind(on_release=self.step3_clicked)

        # Add widgets to the layout
        layout.add_widget(instructions_label)
        layout.add_widget(step1_button)
        layout.add_widget(step2_button)
        layout.add_widget(step3_button)
        layout.add_widget(battery_label)

        return layout

    def step1_clicked(self, instance):
        self.show_popup("Step 1", "Adjust the straps")

    def step2_clicked(self, instance):
        self.show_popup("Step 2", "Secure the chin strap")

    def step3_clicked(self, instance):
        self.show_popup("Step 3", "Ensure a snug fit")

    def show_popup(self, step, description):
        # Create the popup content
        content = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(10))
        content.background_color = (0.2, 0.2, 0.2, 1)

        step_label = Label(
            text=step, font_size=dp(24), bold=True, color=(1, 1, 1, 1))
        description_label = Label(
            text=description, color=(1, 1, 1, 0.7))

        close_button = Button(
            text="Close", font_size=dp(20),
            background_color=(0.2, 0.6, 0.9, 1), background_normal='',
            size_hint=(None, None), size=(dp(120), dp(60)))
        close_button.bind(on_release=lambda x: popup.dismiss())

        # Add the content to the popup
        content.add_widget(step_label)
        content.add_widget(description_label)
        content.add_widget(close_button)

        # Create and open the popup
        popup = Popup(
            title="Helmet Instruction", content=content,
            size_hint=(None, None), size=(dp(400), dp(300)))
        popup.open()


if __name__ == '__main__':
    # Set the window size and other configurations
    Window.size = (500, 600)
    Window.clearcolor = (0.1, 0.1, 0.1, 1)

    HelmetApp().run()

