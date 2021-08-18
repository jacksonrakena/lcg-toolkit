from tkinter import *
from tkinter.font import BOLD, ITALIC
from utils import delete_text_in_entry, replace_text_in_entry
import utils
import plot
import templates

def frame(root, **kwargs):
    return LabelFrame(root, **kwargs)

def create_options(root, options): 
    var = StringVar()
    var.set(options[0])
    return OptionMenu(root, var, *options), var

# Load all templates

root = Tk()
root.title("Linear Congruential Generator Functions")

"""
Naming scheme:
root = Root frame
f_ = Frame
i_ = Input (Entry)
d_ = Data
t_ = Label (text)
v_ = Variable (input)
p_ = Process (function)
m_ = Menu (OptionMenu)
"""

# Window root

## Main label
Label(text='Linear Congruential Generator Functions', font=('', 24, BOLD)).grid(row=0, column=0, columnspan=2, pady=(15,0))
## Subtitle
Label(text='Exploring the function X(n+1) = (a(Xn)+c) mod m', font=('', 16, ITALIC)).grid(row=1,column=0,columnspan=2)

# 'Function Setup' subframe

f_function_setup = LabelFrame(root, text='Function Setup')
f_function_setup.grid(row=2,column=0,padx=(30,30))

## Populate text
Label(f_function_setup, text='Populate:', font=('', 14, BOLD)).grid(row=0,column=0)
Label(f_function_setup, text='Formulas will be calculated automatically', font=('', 10, ITALIC)).grid(row=0,column=1)

## Multiplicative factor (A)

Label(f_function_setup, text='Multiplicative factor (A):').grid(row=1,column=0)
i_factor_a = Entry(f_function_setup)
i_factor_a.grid(row=1,column=1,padx=20)

## Additive factor (C)

Label(f_function_setup, text='Additive factor (C):').grid(row=2,column=0)
i_factor_c = Entry(f_function_setup)
i_factor_c.grid(row=2,column=1)

## Modulus factor (M)

Label(f_function_setup, text='Modulus factor (M):').grid(row=3,column=0)
i_factor_m = Entry(f_function_setup)
i_factor_m.grid(row=3,column=1)

## First seed value (X0)
Label(f_function_setup, text='First seed value (X0):').grid(row=4,column=0)
i_seed = Entry(f_function_setup)
i_seed.insert(0, '1')
i_seed.grid(row=4, column=1)

## Template selector
Label(f_function_setup, text='Or, select a template:', font=('', 14, BOLD)).grid(row=5,column=0)
d_template_options = templates.open_templates()
v_selected_template = StringVar()
v_selected_template.set(list(d_template_options.keys())[0])

def p_template_selected(self, *args):
    new_options = d_template_options[v_selected_template.get()]
    replace_text_in_entry(i_factor_a, new_options[0])
    replace_text_in_entry(i_factor_c, new_options[1])
    replace_text_in_entry(i_factor_m, new_options[2])

m_template_selector = OptionMenu(f_function_setup, v_selected_template, command=p_template_selected, *d_template_options.keys())
m_template_selector.grid(row=5,column=1)

# 'Rendering Options' subframe

f_render_options = frame(root, text = 'Rendering Options')
f_render_options.grid(row=2,column=1,padx=(0,30))

## Plot name

Label(f_render_options, text='Plot name:').grid(row=0,column=0)
i_plot_name = Entry(f_render_options)
i_plot_name.grid(row=0,column=1)

## Dot colour
Label(f_render_options, text='Colour of dots:').grid(row=1,column=0)
d_colour_options = {
    'Pink': '#f79ee1',
    'Black': '#000000',
    'Grey': '#aaa9aa',
    'Red': '#fc5d6f',
    'Orange': '#ea9f1e',
    'Yellow': '#dcea1e',
    'Green (Neon)': '#7aea1e',
    'Green (Dark)': '#3e7a0d',
    'Cyan': '#34ecef',
    'Blue': '#3469ef',
    'Purple': '#a134ef'
}
v_selected_dot_colour = StringVar()
v_selected_dot_colour.set(list(d_colour_options.keys())[0])
m_dot_colours = OptionMenu(f_render_options, v_selected_dot_colour, *d_colour_options.keys())
m_dot_colours.grid(row=1,column=1)

## Blank labels, to fill up space

Label(f_render_options, text='').grid(row=2,column=0)
Label(f_render_options, text='').grid(row=3,column=0)
Label(f_render_options, text='').grid(row=4,column=0)
Label(f_render_options, text='').grid(row=5,column=0)

## Plot, Reset, Exit buttons + logic
def p_init_plot(*args):
    if not utils.compute_and_replace([i_factor_a, i_factor_c, i_factor_m]):
        return
    plot.run_plot(i_plot_name.get(), int(i_factor_a.get()), int(i_factor_c.get()), int(i_factor_m.get()), 1, d_colour_options[v_selected_dot_colour.get()])

Button(f_render_options, text='Plot', command=p_init_plot).grid(row=6,column=0)

def p_reset_options(*args):
    for factor in [i_factor_a, i_factor_c, i_factor_m, i_seed, i_plot_name]:
        delete_text_in_entry(factor)

Button(f_render_options, text='Reset', command=p_reset_options).grid(row=6,column=1)

def p_exit(*args):
    exit(0)

Button(f_render_options, text='Exit', command=p_exit).grid(row=6,column=2)

## Branding

Label(text='Jackson Rakena, 2021 - AS91906 Digital Technologies', font=(
    '',
    12,
    ITALIC
)).grid(row=4,column=0,pady=(0,30))

## Run!

root.mainloop()
