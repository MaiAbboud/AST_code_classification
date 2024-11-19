from utils import *


def statements():
    df = execute_query(
        '''SELECT statement.statement_category, statement.firstchild, statement.secondchild,
        statement.thirdchild, statement.parentnode, statement.parentchild, statement.height, statement.depth,
        statement.user_class
        FROM statement;
        ''')

    # DISCRETIZATION
    discretized_columns = {
        "height": [(1, 32), (32, 63), (63, inf)],  # min: 1 max: 92
        "depth": [(0, 33),  (33, 66), (66, inf)]  # min: 0 max: 95
    }
    discretize_columns(df, discretized_columns)
    # print(df.groupby(['height']).size())
    # print(df.groupby(['depth']).size())

    # SINGLE FEATURE
    print("--- SINGLE FEATURE ---")
    print(get_statistics(df, ['statement_category'], 10))
    print(get_statistics(df, ['firstchild'], 10))
    print(get_statistics(df, ['secondchild'], 10))
    print(get_statistics(df, ['thirdchild'], 10))
    print(get_statistics(df, ['parentnode'], 10))
    print(get_statistics(df, ['parentchild'], 10))
    print(get_statistics(df, ['height'], 10))
    print(get_statistics(df, ['depth'], 10))

    # 2 FEATURES
    print("--- TWO FEATURES ---")
    print(get_statistics(df, ['statement_category', 'firstchild'], 10))
    print(get_statistics(df, ['statement_category', 'parentnode'], 10))
    print(get_statistics(df, ['statement_category', 'parentchild'], 10))
    print(get_statistics(df, ['statement_category', 'height'], 10))
    print(get_statistics(df, ['statement_category', 'depth'], 10))
    print(get_statistics(df, ['parentnode', 'height'], 10))
    print(get_statistics(df, ['parentnode', 'depth'], 10))

    # 3 FEATURES
    print("--- THREE FEATURES ---")
    print(get_statistics(df, ['statement_category', 'firstchild', 'secondchild'], 10))
    print(get_statistics(df, ['statement_category', 'parentnode', 'parentchild'], 10))
    print(get_statistics(df, ['statement_category', 'parentnode', 'height'], 10))
    print(get_statistics(df, ['statement_category', 'parentnode', 'depth'], 10))

    # 4 FEATURES
    print("--- FOUR FEATURES ---")
    print(get_statistics(df, ['statement_category', 'firstchild', 'secondchild', 'thirdchild'], 10))
    print(get_statistics(df, ['statement_category', 'parentnode', 'parentchild', 'height'], 10))
    print(get_statistics(df, ['statement_category', 'parentnode', 'parentchild', 'depth'], 10))

    # ALL FEATURES
    print("--- ALL FEATURES ---")
    print(get_statistics(df,
                         ['statement_category', 'parentnode', 'parentchild', 'firstchild', 'secondchild', 'thirdchild',
                          'height', 'depth'], 10))
