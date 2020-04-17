# IMPORTS
import pandas as pd
import matplotlib.pyplot as plt

# ORIGINAL DATA
df = pd.read_excel('../Flex_Data.xlsx', usecols='B:E,G,K', skiprows=3)

# one-hotify the data that is not numerical
df['Fiber\nType'] = df['Fiber\nType'].map({'PR': 0, 'OX': 1})
df['Dispersing\nAgent'] = df['Dispersing\nAgent'].map({'No': 0, 'Yes': 1})
df['Mixing'] = df['Mixing'].map({'SO': 0, 'HS': 1, 'SO+HS': 2})

# rename the columns
df.rename(columns={'Unnamed: 6': 'Initial Slope'}, inplace=True)
df.rename(columns={'Unnamed: 10': 'Failure Load'}, inplace=True)

# COMBINE THE TEST RESULTS
test_percents = [0, 5, 10, 20, 30, 40, 50]

for perc in test_percents:
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

        # EXPERIMENTAL DATA
        fail_points = []
        fiber_points = []
        slop_points = []

        for index in range(96):

            df_ft = df['Fiber\nType'][index]
            tc_ft = test_case['Fiber Type'][0]

            df_da = df['Dispersing\nAgent'][index]
            tc_da = test_case['Dispersing Agent'][0]

            df_mix = df['Mixing'][index]
            tc_mix = test_case['Mixing'][0]

            if df_ft == tc_ft and df_da == tc_da and df_mix == tc_mix:
                fiber_points.append(df['Fiber\nWeight (phr)'][index])
                fail_points.append([df['Failure Load'][index]])
                slop_points.append([df['Initial Slope'][index]])

        fig, ax1 = plt.subplots()

        color = 'tab:red'
        ax1.set_xlim(-0.1, 1.1)
        ax1.set_ylim(0, 1500)
        ax1.set_xlabel('Fiber Weight (phr)')
        ax1.set_ylabel('Failure Load (N)', color=color)
        ax1.plot(zero_fibW, zero_fail_arr, color=color)
        ax1.plot(fiber_points, fail_points, 'r.')
        ax1.tick_params(axis='y', labelcolor=color)

        ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

        color = 'tab:blue'
        ax2.set_xlim(-0.1, 1.1)
        ax2.set_ylim(0, 500)
        ax2.set_ylabel('Initial Slope (Load/Disp.)', color=color)  # we already handled the x-label with ax1
        ax2.plot(zero_fibW, zero_slop_arr, color=color)
        ax2.plot(fiber_points, slop_points, 'b.')
        ax2.tick_params(axis='y', labelcolor=color)

        fig.tight_layout()
        plt.title("Failure Load and Initial Slope of Composites with various Fiber Weights \n"
                  "(FT=%s, DA=%s, Mix=%s, Test Percentage=%s)" % (ft, da, mix, perc), fontsize=10)
        plt.subplots_adjust(top=0.88)
        plt.savefig("test-%s/plot-%s" % (perc, num))
        plt.close()
