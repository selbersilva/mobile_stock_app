from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from inventory import InventoryScreen
from sales import SalesScreen

class MainApp(App):
    def build(self):
        self.screen_manager = ScreenManager()
        
        self.screen_manager.add_widget(InventoryScreen(name='inventory'))
        self.screen_manager.add_widget(SalesScreen(name='sales'))
        
        return self.screen_manager

if __name__ == '__main__':
    MainApp().run()