import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as poly
import pandas as pd
import mplcursors
from string import ascii_lowercase

'''
TODO
functions to implement
- Plot per county data
- Plot per state data
- Plot per country data (Eventually)

'''
csv_path = './data/raw/climdiv-avgtmp.csv'
headers = ['Codes', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def get_test_data():
    df = pd.read_csv(csv_path, delimiter=',', nrows=127, header=None)
    df.columns = headers

    print(df.head())

    x_dates_format = []
    x_data = []
    for i in df['Codes']:
        for j in range(1,13):
            x_dates_format.append(str(i)[-4:] + '-' + str(j))
            x_data.append(int(str(i)[-4:]) + (j-1) / 12)

    y_data = []
    for i, row in df.head(127).iterrows():
        for j in row[1:]:
            y_data.append(j)

    return [x_data, y_data, x_dates_format]
 

def get_test_data_raw():
    df = pd.read_csv(csv_path, delimiter=',', nrows=127, header=None)
    df.columns = headers
    return df

def plot(ptype, df, plot_vars_map):

    x_data, y_data = process_data(df, plot_vars_map['process_type'], plot_vars_map['range'])
    if ptype == 'scatter':
        pass
    elif ptype == 'poly':
        pass
    elif ptype == 'poly_deriv':
        plot_poly_deriv(x_data, y_data, plot_vars_map['degree'], plot_vars_map['deriv_degree'])
        return plot_poly_deriv(x_data_list, y_data_list, plot_vars_map['degree'], plot_vars_map['deriv_degree'], 
                               plot_vars_map['plots_per_graph'], plot_vars_map['counties'])
    elif ptype == 'scatter_poly':
        scatter_poly(x_data, y_data, plot_vars_map['degree'])
    elif ptype == 'us_heatmap':
        pass
    else:
        return 'Invalid plot type!'


def process_data(df, process_type, data_range):
    x_data = []
    y_data = []

    if process_type == 'months':
        for i in df.iloc[:,0]:
            for j in data_range:
                x_data.append(int(str(i)[-4:]) + j / 12)

        for i, row in df.iterrows():
            for j in row[data_range.start+1:data_range.stop+1]:
                y_data.append(j)
    return x_data, y_data

def scatter_poly(x, y, deg):
    # Example of what coeffs and fiteq do, for a 3rd degree polynomial
    #d, c, b, a = poly.polyfit(x, y, 3)
    #fiteq = lambda x: a * x ** 3 + b * x ** 2 + c * x + d

    coeffs = poly.polyfit(x, y, deg)
    def fiteq(x, idx=0):
        if idx == deg:
            return coeffs[idx] * x ** (idx)
        else:
            return coeffs[idx] * x ** (idx) + fiteq(x, idx+1)

    x_fit = np.array(x)
    y_fit = fiteq(x_fit)

    fig, ax1 = plt.subplots()
    lines = ax1.plot(x_fit, y_fit, color='r', alpha=0.5, label='Polynomial fit')
    ax1.scatter(x, y, s=4, color='b', label='Data points')
    ax1.set_title(f'Polynomial fit example deg={deg}')
    ax1.legend()
    #plt.subplots_adjust(right=0.8)
    #plt.table([['{:.10f}'.format(coeffs[x])[:9]] for x in range(len(coeffs)-1, -1, -1)], 
    #          rowLabels=[ascii_lowercase[x] for x in range(deg+1)], 
    #          colLabels=['Poly Coeffs'], loc='right', colWidths = [0.2])
    #plt.text(15, 3.4, 'Coefficients', size=12)
    cursor = mplcursors.cursor()
    plt.show()

def plot_poly_deriv(x, y, deg, deriv_deg, plots_per_graph, counties):
    
    fig, ax1 = plt.subplots()
    colors = cm.rainbow(np.linspace(0, 1, len(counties)))
    for x, y, county, color in zip(x, y, counties, colors):
        coeffs = poly.polyfit(x, y, deg)
        dcoeffs = poly.polyder(coeffs, deriv_deg)
        def fiteq(x, idx=0):
            if idx == deg - deriv_deg:
                return dcoeffs[idx] * x ** (idx)
            else:
                return dcoeffs[idx] * x ** (idx) + fiteq(x, idx+1)

        x_fit = np.array(x)
        y_fit = fiteq(x_fit)

        lines = ax1.plot(x_fit, y_fit, color=color, alpha=0.5, label=county)
        #ax1.scatter(x, y, s=4, color=color)
    
    ax1.set_title(f'Derivitive deg={deriv_deg} of polynomial fit deg={deg}')
    ax1.legend()
    cursor = mplcursors.cursor()
    return fig

    x_fit = np.array(x)
    y_fit = fiteq(x_fit)

    fig, ax1 = plt.subplots()
    lines = ax1.plot(x_fit, y_fit, color='r', alpha=0.5, label=f'Polynomial deg={deg}, Derivative d={deriv_deg}')
    ax1.legend()
    plt.show()

def scatter_plot(x, y):
    x_data = np.array(x)
    y_data = np.array(y)

    y_axis = np.arange(0, 120, 10)
    x_axis = np.arange(x_data[0], x_data[-1], 2)

    plt.figure(figsize=(20,5))
    plt.xticks(x_axis)
    plt.yticks(y_axis)
    plt.scatter(x_data, y_data)
    plt.show()
    lines = ax1.plot(x_fit, y_fit, color='r', alpha=0.5, label='Polynomial fit')
    scatter = ax1.scatter(x, y, s=4, color='b', label='Data points')
    ax1.set_title(f'Polynomial fit example deg={deg}')
    ax1.legend()
    plt.subplots_adjust(right=0.8)
    plt.table([['{:.10f}'.format(coeffs[x])[:9]] for x in range(len(coeffs)-1, -1, -1)],
              rowLabels=[ascii_lowercase[x] for x in range(deg+1)],
              colLabels=['Poly Coeffs'], loc='right', colWidths = [0.2])

    canvas = FigureCanvasTkAgg(fig, master=window) # window is main tkinter window
    canvas.get_tk_widget().pack()

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   window)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()


if __name__ == '__main__':

    # TODO: Add plot color preferences to the input map
    #plot('scatter_poly', get_test_data_raw(), {'process_type': 'months', 'range': range(0,12), 'degree': 3})
    plot('poly_deriv', get_test_data_raw(), {'process_type': 'months', 'range': range(0,12), 'degree': 5, 'deriv_degree' : 2})
