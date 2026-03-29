import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df07 = pd.read_csv('2007_YRBS_data.csv', low_memory=False)
df23 = pd.read_csv('2023_YRBS_data.csv', low_memory=False)

# Sleep question codes: 1=<=4hr, 2=5hr, 3=6hr, 4=7hr, 5=8hr, 6=9hr, 7=>=10hr
# Insufficient sleep = codes 1-4 (<=7 hrs); q97 in 2007, q85 in 2023

def sleep_stats(df, sleep_col, mask=None):
    """Return weighted % insufficient sleep, Wald 95% CI half-width, and n."""
    if mask is not None:
        df = df.loc[mask]
    s = df[sleep_col].dropna()
    w = df.loc[s.index, 'weight']
    p = w[s <= 4].sum() / w.sum() * 100          # weighted proportion
    ci = 1.96 * np.sqrt(p/100 * (1 - p/100) / len(s)) * 100   # Wald CI
    return p, ci, len(s)

def grouped_bar(rows, title, filename, ylim=(55, 95)):
    """Side-by-side bar chart comparing 2007 vs 2023 for a list of (label, p07, ci07, p23, ci23)."""
    labels = [r[0] for r in rows]
    x = np.arange(len(rows))
    w = 0.35
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.bar(x - w/2, [r[1] for r in rows], w, yerr=[r[2] for r in rows],
           capsize=5, color='steelblue', label='2007')
    ax.bar(x + w/2, [r[3] for r in rows], w, yerr=[r[4] for r in rows],
           capsize=5, color='coral', label='2023')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylim(*ylim)
    ax.set_ylabel('Insufficient sleep (%)')
    ax.set_title(title)
    ax.legend()
    plt.tight_layout()
    plt.savefig(filename, dpi=150)
    plt.show()

# q3: 1=Freshman, 2=Sophomore, 3=Junior, 4=Senior
GRADES = {1: 'Freshman', 2: 'Sophomore', 3: 'Junior', 4: 'Senior'}

print("\nInsufficient sleep by Grade  (paper values in parentheses)")
print(f"  {'':12} {'2007%':>7}  {'2023%':>7}  {'Change':>7}")
grade_rows = []
for code, label in GRADES.items():
    p07, ci07, n07 = sleep_stats(df07, 'q97', mask=df07['q3'] == code)
    p23, ci23, n23 = sleep_stats(df23, 'q85', mask=df23['q3'] == code)
    print(f"  {label:12} {p07:6.1f}%  {p23:6.1f}%  {p23-p07:+6.1f}%")
    grade_rows.append((label, p07, ci07, p23, ci23))

grouped_bar(grade_rows, 'Insufficient Sleep by Grade', 'plot_grade.png', ylim=(50, 90))

# Analysis 1: Sex
# q2: 1=Female, 2=Male
# Paper: Female 71.3->78.3%, Male 66.6->75.4%
SEX = {1: 'Female', 2: 'Male'}

print("\nInsufficient sleep by Sex  (paper values in parentheses)")
print(f"  {'':8} {'2007%':>7} {'95% CI':>14}   {'2023%':>7} {'95% CI':>14}   {'Change':>7}")
sex_rows = []
for code, label in SEX.items():
    p07, ci07, n07 = sleep_stats(df07, 'q97', mask=df07['q2'] == code)
    p23, ci23, n23 = sleep_stats(df23, 'q85', mask=df23['q2'] == code)
    print(f"  {label:8} {p07:6.1f}% ({p07-ci07:.1f}, {p07+ci07:.1f})  "
          f"{p23:6.1f}% ({p23-ci23:.1f}, {p23+ci23:.1f})  {p23-p07:+6.1f}%")
    sex_rows.append((label, p07, ci07, p23, ci23))

grouped_bar(sex_rows, 'Insufficient Sleep by Sex', 'plot_sex.png')

# Analysis 2: Cannabis use in past 30 days
# q48: 1=0 times, 2=1-2, 3=3-9, 4=10-19, 5=20-39, 6=40+ times in past 30 days
# Paper: Never 66.9->75.1%, <10 times 78.1->83.9%, >=10 times 74.9->86.1%
cannabis_map = {1: 'Never', 2: '<10 times', 3: '<10 times',
                4: '>=10 times', 5: '>=10 times', 6: '>=10 times'}
df07['cannabis'] = df07['q48'].map(cannabis_map)
df23['cannabis'] = df23['q48'].map(cannabis_map)
CAN_GROUPS = ['Never', '<10 times', '>=10 times']

print("\nInsufficient sleep by Cannabis use (past 30 days)  (paper values in parentheses)")
print(f"  {'':12} {'2007%':>7} {'95% CI':>14}   {'2023%':>7} {'95% CI':>14}   {'Change':>7}")
can_rows = []
for label in CAN_GROUPS:
    p07, ci07, n07 = sleep_stats(df07, 'q97', mask=df07['cannabis'] == label)
    p23, ci23, n23 = sleep_stats(df23, 'q85', mask=df23['cannabis'] == label)
    print(f"  {label:12} {p07:6.1f}% ({p07-ci07:.1f}, {p07+ci07:.1f})  "
          f"{p23:6.1f}% ({p23-ci23:.1f}, {p23+ci23:.1f})  {p23-p07:+6.1f}%")
    can_rows.append((label, p07, ci07, p23, ci23))

grouped_bar(can_rows, 'Insufficient Sleep by Cannabis Use (past 30 days)', 'plot_cannabis.png')

# Analysis 3 (new query): Physical activity vs sleep by sex, 2023
# q76: days of >=60 min activity in past 7 days (1=0d, 2=1d, ..., 8=7d)
# Conjecture: more active days => less insufficient sleep, with a larger effect for males
activ_map = {1: '0 days',   2: '1-2 days', 3: '1-2 days',
             4: '3-4 days', 5: '3-4 days',
             6: '5+ days',  7: '5+ days',  8: '5+ days'}
df23['activ'] = df23['q76'].map(activ_map)
ACTIV = ['0 days', '1-2 days', '3-4 days', '5+ days']

print("\nInsufficient sleep by Physical Activity Level (2023), split by Sex")
print(f"  {'':22} {'n':>7} {'%':>7} {'95% CI':>14}")
fig, axes = plt.subplots(1, 2, figsize=(10, 4), sharey=True)
for ax, (sex_code, sex_label) in zip(axes, SEX.items()):
    props, errs = [], []
    for a in ACTIV:
        mask = (df23['q2'] == sex_code) & (df23['activ'] == a)
        p, ci, n = sleep_stats(df23, 'q85', mask=mask)
        props.append(p)
        errs.append(ci)
        print(f"  {sex_label + ', ' + a:22} {n:7,} {p:6.1f}%  ({p-ci:.1f}, {p+ci:.1f})")
    ax.bar(ACTIV, props, yerr=errs, capsize=5, color='steelblue')
    ax.set_title(sex_label)
    ax.set_ylim(55, 95)
    ax.set_ylabel('Insufficient sleep (%)')
    ax.set_xlabel('Days physically active (>=60 min)')
    ax.tick_params(axis='x', labelsize=9)
fig.suptitle('Insufficient Sleep vs Physical Activity by Sex (2023)')
plt.tight_layout()
plt.savefig('plot_activ_sex.png', dpi=150)
plt.show()
