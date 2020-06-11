from kivy.app import App
from time import strftime
from kivy.clock import Clock


class StopWatchApp(App):
    sw_seconds = 0
    sw_started = False

    def update_time(self, nap):
        if self.sw_started:
            self.sw_seconds += nap
        minutes, seconds = divmod(self.sw_seconds, 60)
        part_seconds = seconds * 100 % 100
        self.root.ids.stopwatch.text = f'{int(minutes):02}:{int(seconds):02}.[size=40]{int(part_seconds):02}[/size]'
        self.root.ids.time.text = strftime('[b]%H[/b]:%M:%S')

    def on_start(self):
        Clock.schedule_interval(self.update_time, 0)

    def start_stop(self):
        self.root.ids.start_stop.text = 'Start' if self.sw_started else 'Stop'
        self.sw_started = not self.sw_started

    def reset(self):
        if self.sw_started:
            self.root.ids.start_stop.text = 'Start'
            self.sw_started = False
        self.sw_seconds = 0


if __name__ == '__main__':
    from kivy.core.window import Window
    from kivy.utils import get_color_from_hex
    from kivy.core.text import LabelBase
    Window.clearcolor = get_color_from_hex('#4b5162')
    LabelBase.register(name='Roboto', fn_regular='Roboto-Thin.ttf',
                       fn_bold='Roboto-Medium.ttf')
    StopWatchApp().run()
