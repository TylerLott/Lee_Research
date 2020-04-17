import pandas as pd
import matplotlib.pyplot as plt

# COMBINE THE TEST RESULTS
test_percents = [0, 5, 10, 20, 30, 40, 50]

for perc in test_percents:
    fig, ax1 = plt.subplots(figsize=(7, 3))
    labels = []
    for num in range(1, 13):

        zero_fail = pd.read_csv(f"../res/res_{perc}/failureLoad/rawData/set-{num}.csv")
        zero_fail_arr = zero_fail['Failure Load'].to_numpy()
        zero_fibW = zero_fail['Fiber Weight'].to_numpy()

        zero_slop = pd.read_csv(f"../res/res_{perc}/iniSlope/rawData/set-{num}.csv")
        zero_slop_arr = zero_slop['Initial Slope'].to_numpy()

        # TEST CASE VARIABLES
        test_case = pd.read_csv(f"../synthData/{num}.csv")
        ft = "PR" if test_case['Fiber Type'][0] == 0 else "OX"
        da = "No" if test_case['Dispersing Agent'][0] == 0 else "Yes"
        mix = test_case['Mixing'][0]
        if mix == 0:
            mix = "SO"
        if mix == 1:
            mix = "HS"
        if mix == 2:
            mix = "SO+HS"

        labels.append("FT=%s, DA=%s, MIX=%s" % (ft, da, mix))

        ax1.set_xlim(0, 1)
        ax1.set_ylim(100, 1600)
        ax1.set_xlabel('Fiber Weight (phr)', fontsize=6)
        ax1.set_ylabel('Failure Load (N)', fontsize=6)
        ax1.plot(zero_fibW, zero_fail_arr)
        ax1.tick_params(axis='y')

        fig.tight_layout()
        plt.title("Failure Load of Composites with various Fiber Weights with %s%% Data Restricted" %
                  perc, fontsize=7)
        plt.subplots_adjust(top=0.9)

    box = ax1.get_position()
    ax1.set_position([box.x0, box.y0, box.width * 0.65, box.height])
    legend_x = 1.05
    legend_y = 0.5
    plt.legend([i for i in labels], loc='center left', bbox_to_anchor=(legend_x, legend_y), fontsize=8)
    plt.savefig("test-%s/combine_plot_Fail" % perc)
    plt.close()

for perc in test_percents:
    fig, ax1 = plt.subplots(figsize=(7, 3))
    labels = []
    for num in range(1, 13):

        zero_fail = pd.read_csv(f"../res/res_{perc}/failureLoad/rawData/set-{num}.csv")
        zero_fail_arr = zero_fail['Failure Load'].to_numpy()
        zero_fibW = zero_fail['Fiber Weight'].to_numpy()

        zero_slop = pd.read_csv(f"../res/res_{perc}/iniSlope/rawData/set-{num}.csv")
        zero_slop_arr = zero_slop['Initial Slope'].to_numpy()

        # TEST CASE VARIABLES
        test_case = pd.read_csv(f"../synthData/{num}.csv")
        ft = "PR" if test_case['Fiber Type'][0] == 0 else "OX"
        da = "No" if test_case['Dispersing Agent'][0] == 0 else "Yes"
        mix = test_case['Mixing'][0]
        if mix == 0:
            mix = "SO"
        if mix == 1:
            mix = "HS"
        if mix == 2:
            mix = "SO+HS"

        labels.append("FT=%s, DA=%s, MIX=%s" % (ft, da, mix))

        ax1.set_xlim(0, 1)
        ax1.set_ylim(100, 500)
        ax1.set_xlabel('Fiber Weight (phr)', fontsize=6)
        ax1.set_ylabel('Initial Slope (Load/Disp.)', fontsize=6)  # we already handled the x-label with ax1
        ax1.plot(zero_fibW, zero_slop_arr)
        ax1.tick_params(axis='y')

        fig.tight_layout()
        plt.title("Initial Slope of Composites with various Fiber Weights with %s%% Data Restricted" %
                  perc, fontsize=7)
        plt.subplots_adjust(top=0.9)

    box = ax1.get_position()
    ax1.set_position([box.x0, box.y0, box.width * 0.65, box.height])
    legend_x = 1.05
    legend_y = 0.5
    plt.legend([i for i in labels], loc='center left', bbox_to_anchor=(legend_x, legend_y), fontsize=8)
    plt.savefig("test-%s/combine_plot_Ini" % perc)
    plt.close()
