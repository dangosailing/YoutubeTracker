import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def generate_ccv_plot(data) -> None:
    pass

    df = pd.DataFrame.from_dict(data)
    fig, ax = plt.subplots()
    ax.plot(df["timestamp"], df["ccv"])

    ax.xaxis.set_major_locator(ticker.AutoLocator())
    ax.xaxis.set_minor_locator(ticker.AutoMinorLocator())

    ax.set_ylim([0, 10000])

    plt.show()