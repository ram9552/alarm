import time

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

Window.size = (400, 700)

class myclock(Label):
	def update(self, *args):
		self.text = time.asctime()

class myclock2(Label):
	def update(self, *args):
		t = time.gmtime()
		self.text = time.asctime(t)

class TimeApp(App):

	def build(self):
		layout = BoxLayout(orientation='vertical')

		clock1 = myclock()
		Clock.schedule_interval(clock1.update, 1)
		layout.add_widget(clock1)
		layout.add_widget(Label(text='INDIA'))

		clock2 = myclock2()
		Clock.schedule_interval(clock2.update, 1)
		layout.add_widget(clock2)
		layout.add_widget(Label(text='LONDON'))

		return layout

root = TimeApp()
root.run()
