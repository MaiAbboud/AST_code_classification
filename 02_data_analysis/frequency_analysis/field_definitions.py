from utils import *


def field_definitions():
    df = execute_query(
        '''SELECT fielddefinition.fieldvisibility, fielddefinition.isfinal, 
        fielddefinition.isstatic, fielddefinition.numberannotations, 
        fielddefinition.namingconvention, fielddefinition.initialvalue,
        fielddefinition.type, fielddefinition.isvolatile, 
        fielddefinition.istransient, fielddefinition.parentnode,
        fielddefinition.user_class FROM fielddefinition;
        ''')

    # DISCRETIZATION
    discretized_columns = {
        "numberannotations": [(0, 1), (1, 2), (2, inf)]  # min: 0 max: 3
    }
    discretize_columns(df, discretized_columns)
    # print(df.groupby(['numberannotations']).size())

    # SINGLE FEATURE
    print("--- SINGLE FEATURE ---")
    print(get_statistics(df, ['fieldvisibility'], 10))
    print(get_statistics(df, ['isfinal'], 10))
    print(get_statistics(df, ['isstatic'], 10))
    print(get_statistics(df, ['numberannotations'], 10))
    print(get_statistics(df, ['namingconvention'], 10))
    print(get_statistics(df, ['initialvalue'], 10))
    print(get_statistics(df, ['type'], 10))
    print(get_statistics(df, ['isvolatile'], 10))
    print(get_statistics(df, ['istransient'], 10))
    print(get_statistics(df, ['parentnode'], 10))

    # 2 FEATURES
    print("--- TWO FEATURES ---")
    print(get_statistics(df, ['fieldvisibility', 'isfinal'], 10))
    print(get_statistics(df, ['fieldvisibility', 'isstatic'], 10))
    print(get_statistics(df, ['fieldvisibility', 'namingconvention'], 10))
    print(get_statistics(df, ['fieldvisibility', 'type'], 10))
    print(get_statistics(df, ['fieldvisibility', 'initialvalue'], 10))
    print(get_statistics(df, ['fieldvisibility', 'parentnode'], 10))
    print(get_statistics(df, ['fieldvisibility', 'numberannotations'], 10))
    print(get_statistics(df, ['type', 'initialvalue'], 10))
    print(get_statistics(df, ['type', 'parentnode'], 10))
    print(get_statistics(df, ['isstatic', 'namingconvention'], 10))
    print(get_statistics(df, ['isstatic', 'type'], 10))
    print(get_statistics(df, ['isstatic', 'isfinal'], 10))
    print(get_statistics(df, ['isfinal', 'initialvalue'], 10))

    # 3 FEATURES
    print("--- THREE FEATURES ---")
    print(get_statistics(df, ['fieldvisibility', 'isstatic', 'isfinal'], 10))
    print(get_statistics(df, ['fieldvisibility', 'isstatic', 'type'], 10))
    print(get_statistics(df, ['fieldvisibility', 'isstatic', 'namingconvention'], 10))
    print(get_statistics(df, ['fieldvisibility', 'isfinal', 'namingconvention'], 10))
    print(get_statistics(df, ['fieldvisibility', 'type', 'initialvalue'], 10))
    print(get_statistics(df, ['fieldvisibility', 'isfinal', 'initialvalue'], 10))
    print(get_statistics(df, ['fieldvisibility', 'isstatic', 'initialvalue'], 10))
    print(get_statistics(df, ['isstatic', 'isfinal', 'initialvalue'], 10))

    # 4 FEATURES
    print("--- FOUR FEATURES ---")
    print(get_statistics(df, ['fieldvisibility', 'isstatic', 'isfinal', 'initialvalue'], 10))
    print(get_statistics(df, ['fieldvisibility', 'isstatic', 'isfinal', 'type'], 10))
    print(get_statistics(df, ['fieldvisibility', 'isstatic', 'isfinal', 'namingconvention'], 10))
    print(get_statistics(df, ['fieldvisibility', 'type', 'isstatic', 'initialvalue'], 10))
    print(get_statistics(df, ['fieldvisibility', 'type', 'isfinal', 'initialvalue'], 10))

    # ALL FEATURES
    print("--- ALL FEATURES ---")
    print(get_statistics(df, ['fieldvisibility', 'isfinal', 'isstatic', 'numberannotations', 'namingconvention',
                              'initialvalue', 'type', 'isvolatile', 'istransient', 'parentnode'], 10))
