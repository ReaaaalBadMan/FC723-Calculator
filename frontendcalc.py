import tkinter as tk
import math

class calculatorapp:
    def __init__(self):
        # Initialize main window
        self.root = tk.Tk()
        self.root.title("Scientific Calculator")
        self.root.geometry("400x500")  # Set initial window size
        self.root.configure(bg='#E8E8E8')  # Set background color
        
        # Configure grid weights for responsive layout
        # This ensures the calculator stays centered and scales properly
        self.root.grid_rowconfigure(0, weight=1)    
        self.root.grid_rowconfigure(2, weight=1)    
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

        # Create main display frame to hold the calculator display
        display_frame = tk.Frame(self.root, bg='#E8E8E8')
        display_frame.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)
        
        # Create display entry widget where calculations will be shown
        self.display = tk.Entry(display_frame, width=25, font=('Arial', 20), 
                              justify='right', bd=5, relief='sunken')
        self.display.grid(row=0, column=0, padx=5, pady=10)

        # Create frame to hold all calculator buttons
        center_frame = tk.Frame(self.root, bg='#E8E8E8')
        center_frame.grid(row=1, column=1, padx=5, pady=5)
        
        # Define common button styling properties
        button_style = {
            'width': 8,
            'height': 2,
            'font': ('Arial', 10, 'bold'),
            'bd': 3,
            'relief': 'raised'
        }
        
        # Create basic operation buttons (+ - × ÷) with light blue background
        op_style = dict(button_style, **{'bg': '#ADD8E6'})
        self.add = tk.Button(center_frame, text="+", **op_style)
        self.add.grid(row=0, column=0, padx=4, pady=3)
        self.sub = tk.Button(center_frame, text="-", **op_style)
        self.sub.grid(row=0, column=1, padx=4, pady=3)
        self.div = tk.Button(center_frame, text="÷", **op_style)
        self.div.grid(row=0, column=2, padx=4, pady=3)
        self.mul = tk.Button(center_frame, text="×", **op_style)
        self.mul.grid(row=0, column=3, padx=4, pady=3)

        # Create trigonometric function buttons with light green background
        trig_style = dict(button_style, **{'bg': '#90EE90'})
        self.sin = tk.Button(center_frame, text="sin", **trig_style)
        self.sin.grid(row=1, column=0, padx=3, pady=3)
        self.cos = tk.Button(center_frame, text="cos", **trig_style)
        self.cos.grid(row=1, column=1, padx=3, pady=3)
        self.tan = tk.Button(center_frame, text="tan", **trig_style)
        self.tan.grid(row=1, column=2, padx=3, pady=3)
        self.arcsin = tk.Button(center_frame, text="arcsin", **trig_style)
        self.arcsin.grid(row=1, column=3, padx=2, pady=3)
        self.arccos = tk.Button(center_frame, text="arccos", **trig_style)
        self.arccos.grid(row=2, column=0, padx=2, pady=3)
        self.arctan = tk.Button(center_frame, text="arctan", **trig_style)
        self.arctan.grid(row=2, column=1, padx=2, pady=3)

        # Create advanced math function buttons with light orange background
        math_style = dict(button_style, **{'bg': '#FFB366'})
        self.square = tk.Button(center_frame, text="x²", **math_style)
        self.square.grid(row=2, column=2, padx=2, pady=3)
        self.squareroot = tk.Button(center_frame, text="√", **math_style)
        self.squareroot.grid(row=2, column=3, padx=2, pady=3)
        self.log = tk.Button(center_frame, text="log", **math_style)
        self.log.grid(row=3, column=0, padx=4, pady=3)
        self.ln = tk.Button(center_frame, text="ln", **math_style)
        self.ln.grid(row=3, column=1, padx=4, pady=3)

        # Create control buttons (clear, backspace) with light red background
        ctrl_style = dict(button_style, **{'bg': '#FFB3B3'})
        self.erase = tk.Button(center_frame, text="⌫", **ctrl_style)  # Backspace button
        self.erase.grid(row=3, column=2, padx=4, pady=3)
        self.clear = tk.Button(center_frame, text="C", **ctrl_style)  # Clear button
        self.clear.grid(row=3, column=3, padx=4, pady=3)

        # Create number pad (1-9) with white background
        num_style = dict(button_style, **{'bg': '#FFFFFF'})
        numbers = '789456123'  # Numbers arranged in calculator layout
        row = 4
        col = 0
        for num in numbers:
            tk.Button(center_frame, text=num, **num_style).grid(
                row=row, column=col, padx=4, pady=3)
            col += 1
            if col > 2:  # Move to next row after 3 buttons
                col = 0
                row += 1
                
        # Add bottom row buttons (0, decimal point, equals)
        tk.Button(center_frame, text="0", **num_style).grid(
            row=7, column=0, padx=4, pady=3)
        tk.Button(center_frame, text=".", **num_style).grid(
            row=7, column=1, padx=4, pady=3)
        self.equals = tk.Button(center_frame, text="=", **op_style)
        self.equals.grid(row=7, column=2, padx=4, pady=3)
        
        # Start the main event loop
        self.root.mainloop()
        
if __name__ == "__main__":
    app = calculatorapp()
