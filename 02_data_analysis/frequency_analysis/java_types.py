from utils import *


def java_types():
    df = execute_query(
        ''' 
        SELECT type.type_category, type.primitive,
        type.height, type.parentnode,
        type.parentchild, type.generics, 
        type.dimensions, type.user_class FROM type;
        ''')

    # DISCRETIZATION
    discretized_columns = {
        "height": [(0, 78), (78, 156), (156, inf)],  # min: 0 max: 233
        "generics": [(0, 3), (3, 6), (6, inf)],  # min: 0 max: 7
        "dimensions": [(0, 2), (2, 4), (4, inf)]  # min: 0 max: 4
    }
    discretize_columns(df, discretized_columns)
    # print(df.groupby(['height']).size())
    # print(df.groupby(['generics']).size())
    # print(df.groupby(['dimensions']).size())

    # SINGLE FEATURE
    print("--- SINGLE FEATURE ---")
    print(get_statistics(df, ['type_category'], 10))
    print(get_statistics(df, ['primitive'], 10))
    print(get_statistics(df, ['parentnode'], 10))
    print(get_statistics(df, ['parentchild'], 10))
    print(get_statistics(df, ['generics'], 10))
    print(get_statistics(df, ['dimensions'], 10))
    print(get_statistics(df, ['height'], 10))

    # 2 FEATURES
    print("--- TWO FEATURES ---")
    print(get_statistics(df, ['type_category', 'parentnode'], 10))
    print(get_statistics(df, ['type_category', 'parentchild'], 10))
    print(get_statistics(df, ['type_category', 'generics'], 10))
    print(get_statistics(df, ['type_category', 'dimensions'], 10))
    print(get_statistics(df, ['type_category', 'height'], 10))
    print(get_statistics(df, ['parentnode', 'parentchild'], 10))
    print(get_statistics(df, ['parentnode', 'primitive'], 10))

    # 3 FEATURES
    print("--- THREE FEATURES ---")
    print(get_statistics(df, ['type_category', 'parentnode', 'parentchild'], 10))
    print(get_statistics(df, ['type_category', 'parentnode', 'generics'], 10))
    print(get_statistics(df, ['type_category', 'parentnode', 'dimensions'], 10))
    print(get_statistics(df, ['parentnode', 'parentchild', 'primitive'], 10))

    # 4 FEATURES
    print("--- FOUR FEATURES ---")
    print(get_statistics(df, ['type_category', 'parentnode', 'parentchild', 'dimensions'], 10))
    print(get_statistics(df, ['type_category', 'parentnode', 'parentchild', 'generics'], 10))
    print(get_statistics(df, ['parentnode', 'parentchild', 'primitive', 'dimensions'], 10))

    # ALL FEATURES
    print("--- ALL FEATURES ---")
    print(get_statistics(df, ['type_category', 'parentnode', 'parentchild', 'dimensions', 'primitive', 'generics',
                              'height'], 10))
