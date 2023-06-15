import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.popup import Popup


class HelmetApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=[20, 10, 20, 10], spacing=10)
        layout.background_color = (0.95, 0.95, 0.95, 1)

        # Create labels for instructions and battery status
        instructions_label = Label(text="Please follow these instructions to wear the helmet:", font_size=18, bold=True)
        instructions_label.color = (0.2, 0.2, 0.2, 1)
        battery_label = Label(text="Helmet battery status: 100%", font_size=14)
        battery_label.color = (0.4, 0.4, 0.4, 1)

        # Create buttons for step-by-step instructions
        step1_button = Button(text="Step 1: Adjust the straps", background_color=(0.2, 0.6, 0.9, 1), font_size=16)
        step2_button = Button(text="Step 2: Secure the chin strap", background_color=(0.2, 0.6, 0.9, 1), font_size=16)
        step3_button = Button(text="Step 3: Ensure a snug fit", background_color=(0.2, 0.6, 0.9, 1), font_size=16)

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
        content = BoxLayout(orientation='vertical', padding=[20, 10, 20, 10], spacing=10)
        content.background_color = (0.9, 0.9, 0.9, 1)

        step_label = Label(text=step, font_size=20, bold=True)
        step_label.color = (0.2, 0.2, 0.2, 1)
        description_label = Label(text=description)
        description_label.color = (0.4, 0.4, 0.4, 1)

        close_button = Button(text="Close", size_hint=(None, None), size=(100, 50), background_color=(0.2, 0.6, 0.9, 1),
                              font_size=16)
        close_button.bind(on_release=lambda x: popup.dismiss())

        # Add the content to the popup
        content.add_widget(step_label)
        content.add_widget(description_label)
        content.add_widget(close_button)

        # Create and open the popup
        popup = Popup(title="Helmet Instruction", content=content, size_hint=(None, None), size=(400, 300))
        popup.open()


if __name__ == '__main__':
    HelmetApp().run()
