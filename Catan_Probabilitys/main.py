from unittest import main
import Catan_Probabilitys
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.properties import ListProperty


class MainPage(BoxLayout):
    end = True
    
    def end_game(self):
        self.end = True




class StackNumber(StackLayout):
    roll_list = ListProperty([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for number in range (2, 13):
            btn = Button(text = str(number), size_hint=(.25, .33))
            btn.bind(on_press = self.on_number_button_click)
            self.add_widget(btn)
        btn = Button(text = u"\u2190", size_hint = (.25, .33))
        self.add_widget(btn)

    def on_number_button_click(self, number):
        self.roll_list.append(number.text)
        print(self.roll_list)


class CatanApp(App):
    pass


if __name__ == '__main__':
    CatanApp().run()
    game_end = False
    roll_list = []
    total_rolls = 0
    
    #Game Loop while game is still being played ends once Y or y given to comandline

    while game_end == False:
     
        roll = input('Dice Roll: ')
        number = Catan_Probabilitys.prove_if_int(roll)
        if number is True:
            range = Catan_Probabilitys.prove_range(int(roll))

        
        
        if range is True and number is True:
            game_rolled_list = Catan_Probabilitys.add_to_roll_list(int(roll), roll_list)
            total_rolls = Catan_Probabilitys.total_roll(total_rolls)
            end_question = input('Has the game ended? (Y/y) ')

        #game_end = Catan_Probabilitys.game_ended(end_question)
         
            game_end = MainPage.end


    #The Probabiltys will be compared and plotted in for comparison
    probs = Catan_Probabilitys.create_average_probability_dic()



    roll_list = Catan_Probabilitys.rolled_dic(game_rolled_list)
    amount_rolls = Catan_Probabilitys.expected_amount_rolls(probs, total_rolls)
    actual_game_prob = Catan_Probabilitys.calculate_game_prob(roll_list, total_rolls)
    for rolls in roll_list:
        if rolls < 10:
            print(f'{rolls}  Expected: {amount_rolls[rolls]}   Actual In Game: {roll_list[rolls]}  Probability: {actual_game_prob[rolls] * 100}%')
        else:
            print(f'{rolls} Expected: {amount_rolls[rolls]}   Actual In Game: {roll_list[rolls]}  Probability: {actual_game_prob[rolls] * 100}%')
    print(f'Total Rolls: {total_rolls}')

    main(module='Test_Module', exit=False)
