from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window


class TelaInicial(Screen):
    pass

class gerenciador_Telas(ScreenManager):
    pass
class gerenciadorProjetos(MDApp):
    def build(self):
        Window.borderless = True
        #tira as bordas do app#define  o  app para abrir do lado esquerdo
        Window.top = Window.height-150 #define o top
        Window.size = (Window.width * 0.4, Window.height * 0.3)
        return Builder.load_file('telas.kv')



gerenciadorProjetos().run()