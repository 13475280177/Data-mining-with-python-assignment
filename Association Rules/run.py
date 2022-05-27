import pandas as pd
from mlxtend.frequent_patterns import apriori,association_rules,fpgrowth
from mlxtend.preprocessing import TransactionEncoder

# question1
# 2
def Q2():
    gpa_raw = pd.read_csv('./specs/gpa_question1.csv')
    gpa = []
    count = gpa_raw.pop('count').values
    gpa_tem = gpa_raw.values.tolist()
    # to list, in order to multiply count numbers
    for i in range(0,len(count)):
        for j in range(0,count[i]):
            gpa.append(gpa_tem[i])
    print(gpa)
    print('-----------------------------------------------------------------------------\n')
    te = TransactionEncoder()
    te_ary = te.fit(gpa).transform(gpa)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    print(df)
    print('-----------------------------------------------------------------------------\n')
    fre_items = apriori(df, min_support=0.15, use_colnames=True)
    print(fre_items)
    print('-----------------------------------------------------------------------------\n')
    return fre_items
# t =Q2()
# 3 pop the count
def Q3():
    gpa = pd.read_csv('./specs/gpa_question1.csv', dtype=object)
    count = gpa.pop('count')
    gpa = gpa.values.tolist()
    print(gpa)
    print('-----------------------------------------------------------------------------\n')
    te = TransactionEncoder()
    te_ary = te.fit(gpa).transform(gpa)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    print(df)
    print('-----------------------------------------------------------------------------\n')
    fre_items = apriori(df, min_support=0.15, use_colnames=True)
    print(fre_items)
    print('-----------------------------------------------------------------------------\n')
    return fre_items

def q4():
    test = Q2()
    write = test.sort_values("support",ascending= False)
    pd.DataFrame(write).to_csv('./output/question1_out_apriori.csv')
# a =q4()
def q5and6():
    AR = association_rules(Q2(),metric='confidence',min_threshold=0.6)
    write = AR.sort_values("confidence", ascending=False)
    pd.DataFrame(write).to_csv('./output/question1_out_rules06.csv')
    print(AR)
# t= q5and6()
def q7and8():
    AR = association_rules(Q2(), metric='confidence', min_threshold=0.9)
    write = AR.sort_values("confidence", ascending=False)
    pd.DataFrame(write).to_csv('./output/question1_out_rules09.csv')
    print(AR)
# t =q7and8()

# question2
# data read and pre-processing
def A():
    bank_raw = pd.read_csv('./specs/bank_data_question2.csv')
    del bank_raw['id']
    # Discretize the numeric attributes into 3 bins of equal width
    bank_raw['income'] = pd.cut(bank_raw['income'],bins=3 ,labels=['low','medium','high'])
    bank_raw['age'] = pd.cut(bank_raw['age'],bins=3 ,labels=['youth','middle-aged','elder people'])
    bank_raw['children'] = pd.cut(bank_raw['children'],bins=3 ,labels=['less than one child','two children','three or more children'])
    # replace yes no with no_car, no_save_act etc, because when hot encode, yes and no will be confused.
    bank_raw['car'] = bank_raw['car'].replace('NO','NO_car')
    bank_raw['car'] = bank_raw['car'].replace('YES', 'YES_car')
    bank_raw['pep'] = bank_raw['pep'].replace('NO','NO_pep')
    bank_raw['pep'] = bank_raw['pep'].replace('YES', 'YES_pep')
    bank_raw['mortgage'] = bank_raw['mortgage'].replace('NO', 'NO_mortgage')
    bank_raw['mortgage'] = bank_raw['mortgage'].replace('YES', 'YES_mortgage')
    bank_raw['current_act'] = bank_raw['current_act'].replace('NO', 'NO_current_act')
    bank_raw['current_act'] = bank_raw['current_act'].replace('YES', 'YES_current_act')
    bank_raw['save_act'] = bank_raw['save_act'].replace('NO', 'NO_save_act')
    bank_raw['save_act'] = bank_raw['save_act'].replace('YES', 'YES_save_act')
    bank_raw['married'] = bank_raw['married'].replace('NO', 'NO_married')
    bank_raw['married'] = bank_raw['married'].replace('YES', 'YES_married')
    return bank_raw

# t = A()

# FP-Growth algorithm to generate frequent all frequent itemsets.
def B():
    # to list
    bank_raw = A()
    bank_list = bank_raw.values.tolist()
    # hot encode
    te = TransactionEncoder()
    te_ary = te.fit(bank_list).transform(bank_list)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    print(df)
    print('-----------------------------------------------------------------------------\n')
    fre_items = fpgrowth(df, min_support=0.2, use_colnames=True)
    print(fre_items)
    print('-----------------------------------------------------------------------------\n')
    return fre_items
# store the fre_items to csv file ,ordered by support descending
# t = B()
def C():
    test = B()
    write = test.sort_values("support", ascending=False)
    pd.DataFrame(write).to_csv('./output/question2_out_fpgrowth.csv')

# t = C()
# Generate all the rules associated to these frequent itemsets.
def D():
    AR = association_rules(B(), metric='confidence', min_threshold=0)
    write = AR.sort_values("confidence", ascending=False)
    pd.DataFrame(write).to_csv('./output/question2_out_rules.csv')
    print(AR)

# t =D()





