from utils import *


def expressions():
    df = execute_query(
        '''
        SELECT expression.expression_category, expression.firstchild, expression.secondchild,
        expression.thirdchild, expression.parentnode, expression.parentchild, expression.height, expression.depth,
        expression.user_class FROM expression;
        ''')

    # DISCRETIZATION
    discretized_columns = {
        "height": [(1, 78), (78, 156), (156, inf)],  # min: 1 max: 232
        "depth": [(0, 77), (77, 154), (154, inf)]  # min: 0 max: 230
    }
    discretize_columns(df, discretized_columns)
    # print(df.groupby(['height']).size())
    # print(df.groupby(['depth']).size())

    # SINGLE FEATURE
    print("--- SINGLE FEATURE ---")
    print(get_statistics(df, ['expression_category'], 10))
    print(get_statistics(df, ['firstchild'], 10))
    print(get_statistics(df, ['secondchild'], 10))
    print(get_statistics(df, ['thirdchild'], 10))
    print(get_statistics(df, ['parentnode'], 10))
    print(get_statistics(df, ['parentchild'], 10))
    print(get_statistics(df, ['height'], 10))
    print(get_statistics(df, ['depth'], 10))

    # 2 FEATURES
    print("--- TWO FEATURES ---")
    print(get_statistics(df, ['expression_category', 'firstchild'], 10))
    print(get_statistics(df, ['expression_category', 'parentnode'], 10))
    print(get_statistics(df, ['expression_category', 'parentchild'], 10))
    print(get_statistics(df, ['expression_category', 'height'], 10))
    print(get_statistics(df, ['expression_category', 'depth'], 10))
    print(get_statistics(df, ['parentnode', 'height'], 10))
    print(get_statistics(df, ['parentnode', 'depth'], 10))

    # 3 FEATURES
    print("--- THREE FEATURES ---")
    print(get_statistics(df, ['expression_category', 'parentnode', 'parentchild'], 10))
    print(get_statistics(df, ['expression_category', 'parentnode', 'height'], 10))
    print(get_statistics(df, ['expression_category', 'parentnode', 'depth'], 10))

    # 4 FEATURES
    print("--- FOUR FEATURES ---")
    print(get_statistics(df, ['expression_category', 'parentnode', 'parentchild', 'height'], 10))
    print(get_statistics(df, ['expression_category', 'parentnode', 'parentchild', 'depth'], 10))

    # ALL FEATURES
    print("--- ALL FEATURES ---")
    print(get_statistics(df,
                         ['expression_category', 'parentnode', 'parentchild', 'firstchild', 'secondchild', 'thirdchild',
                          'height', 'depth'], 10))
