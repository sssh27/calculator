from tkinter import*
    

class Mybutton(Button):
    def __init__(self, text, scale, pos, calc): #scale =  [width, height]
        super().__init__(text=text, width=scale[0], height=scale[1], command=self.onclick)
        self.grid(column=pos[0], row=(pos[1])+1)
        self.text = text
        self.calc = calc
    def onclick(self):
        self.calc.add(self.text)

class Calc():
    def __init__(self, label):
        self.text = []
        self.label = label
    def add(self, input_text):
        symbol = [' + ', ' - ', ' * ', ' / ', '.']
        if input_text == '=':
            ans = self.run()
            self.text = [str(ans[0])]
        elif input_text == 'AC':
            self.text = []
        elif input_text == 'del' :#and len(self.text)>0:
            self.text = self.text[:-1]
        
        elif input_text in symbol and self.text[-1] in symbol:
            self.text[-1] = input_text  
        else:
            self.text.append(input_text)
        self.label.configure(text = ''.join(self.text))
    def run(self):
        form = ''.join(self.text)
        return self.count(form)

    def count(self, text = ''):
        text = text.split(' ')
        for index in range(len(text)):
            if text[index] not in ['+', '-', '*', '/']:
                    text[index] = float(text[index])

        while '√' in text:
            index = text.index('√')
            text[index] = text[index+1]**0.5
            del text[index+1]

        while '%' in text:
            index = text.index('%')
            text[index] = text[index-1]*0.01
            del text[index-1]

        while '*' in text or '/' in text:
            if '*' in text and '/' in text:
                index = min(text.index('*'), text.index('/'))
            elif '*' in text:
                index = text.index('*')
            else:
                index = text.index('/')
            if text[index] == '*':
                text[index] = text[index-1]*text[index+1]
            if text[index] == '/':
                text[index] = text[index-1]/text[index+1]
            del text[index+1]
            del text[index-1]

        while '+' in text:
            index = text.index('+')
            text[index] = text[index-1]+text[index+1]
            del text[index+1]
            del text[index-1]

        while '-' in text:
            index = text.index('-')
            text[index] = text[index-1]-text[index+1]
            del text[index+1]
            del text[index-1]
        return text

class Root(Tk):
    def __init__(self):
        super().__init__()
        self.label = Label(text = '0', width = 53, height = 6, bg = 'light grey')
        self.label.grid(column = 0, row = 0, columnspan = 4)
        self.calc = Calc(self.label)
        text_list = [['√','%','del','AC'],
                     ['7','8','9',' + '],
                     ['4','5','6',' - '],
                     ['1','2','3',' * '],
                     ['0','.','=',' / ']]

        for x in range(len(text_list[0])):
            for y in range(len(text_list)):
                Mybutton(text_list[y][x], (12,5), (x,y), self.calc)
root = Root()
root.resizable(height = 0, width = 0)
root.mainloop()