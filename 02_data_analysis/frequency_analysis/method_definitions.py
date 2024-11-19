from utils import *


def method_definitions():
    df = execute_query(
        '''SELECT methoddefinition.methodvisibility, methoddefinition.defaultimplementation, 
        methoddefinition.isfinal,
        methoddefinition.hasoverride, methoddefinition.isstatic, 
        methoddefinition.numberparameters, methoddefinition.numbergenerictypes,
        methoddefinition.numberthrows, methoddefinition.returntype, 
        methoddefinition.firstparametertype, methoddefinition.secondparametertype, 
        methoddefinition.thirdparametertype,
        methoddefinition.numberannotations, methoddefinition.numberstmts,
        methoddefinition.methodlocalvars, methoddefinition.locvarnaming, 
        methoddefinition.namingconvention, methoddefinition.isabstract,
        methoddefinition.numberinnerclasses, methoddefinition.isconstructor,
        methoddefinition.isstrictfp, methoddefinition.isnative, 
        methoddefinition.issynchronized, methoddefinition.numberofoverloaded, 
        methoddefinition.user_class FROM methoddefinition;
        ''')

    # DISCRETIZATION
    discretized_columns = {
        "numberparameters": [(0, 22), (22, 45), (45, inf)],  # min: 0 max: 65
        "numberinnerclasses": [(0, 12), (12, 24), (24, inf)],  # min: 0 max: 31
        "numberofoverloaded": [(1, 10), (10, 19), (19, inf)],  # min: 1 max: 28
        "numbergenerictypes": [(0, 1), (1, 2), (2, inf)],  # min: 0 max: 3
        "numberthrows": [(0, 4), (4, 8), (8, inf)],  # min: 0 max: 13
        "numberannotations": [(0, 2), (2, 4), (4, inf)],  # min: 0 max: 6
        "numberstmts": [(0, 326), (326, 652), (652, inf)],  # min: 0 max: 976
        "methodlocalvars": [(0, 29), (29, 58), (58, inf)]  # min: 0 max: 85
    }
    discretize_columns(df, discretized_columns)
    # print(df.groupby(['numberparameters']).size())
    # print(df.groupby(['numberinnerclasses']).size())
    # print(df.groupby(['numberofoverloaded']).size())
    # print(df.groupby(['numbergenerictypes']).size())
    # print(df.groupby(['numberthrows']).size())
    # print(df.groupby(['numberannotations']).size())
    # print(df.groupby(['numberstmts']).size())
    # print(df.groupby(['methodlocalvars']).size())

    # SINGLE FEATURE
    print("--- SINGLE FEATURE ---")
    print(get_statistics(df, ['methodvisibility'], 10))
    print(get_statistics(df, ['defaultimplementation'], 10))
    print(get_statistics(df, ['isfinal'], 10))
    print(get_statistics(df, ['hasoverride'], 10))
    print(get_statistics(df, ['isstatic'], 10))
    print(get_statistics(df, ['numberparameters'], 10))
    print(get_statistics(df, ['numbergenerictypes'], 10))
    print(get_statistics(df, ['numberthrows'], 10))
    print(get_statistics(df, ['returntype'], 10))
    print(get_statistics(df, ['firstparametertype'], 10))
    print(get_statistics(df, ['secondparametertype'], 10))
    print(get_statistics(df, ['thirdparametertype'], 10))
    print(get_statistics(df, ['numberannotations'], 10))
    print(get_statistics(df, ['numberstmts'], 10))
    print(get_statistics(df, ['methodlocalvars'], 10))
    print(get_statistics(df, ['locvarnaming'], 10))
    print(get_statistics(df, ['namingconvention'], 10))
    print(get_statistics(df, ['isabstract'], 10))
    print(get_statistics(df, ['numberinnerclasses'], 10))
    print(get_statistics(df, ['isconstructor'], 10))
    print(get_statistics(df, ['isstrictfp'], 10))
    print(get_statistics(df, ['isnative'], 10))
    print(get_statistics(df, ['issynchronized'], 10))
    print(get_statistics(df, ['numberofoverloaded'], 10))

    # 2 FEATURES
    print("--- TWO FEATURES ---")
    print(get_statistics(df, ['methodvisibility', 'isstatic'], 10))
    print(get_statistics(df, ['methodvisibility', 'isfinal'], 10))
    print(get_statistics(df, ['methodvisibility', 'numberparameters'], 10))
    print(get_statistics(df, ['methodvisibility', 'isconstructor'], 10))
    print(get_statistics(df, ['methodvisibility', 'numberofoverloaded'], 10))
    print(get_statistics(df, ['methodvisibility', 'numberstmts'], 10))
    print(get_statistics(df, ['methodvisibility', 'methodlocalvars'], 10))
    print(get_statistics(df, ['methodvisibility', 'returntype'], 10))
    print(get_statistics(df, ['methodvisibility', 'hasoverride'], 10))
    print(get_statistics(df, ['methodvisibility', 'isabstract'], 10))
    print(get_statistics(df, ['methodvisibility', 'numberannotations'], 10))
    print(get_statistics(df, ['methodvisibility', 'numberthrows'], 10))
    print(get_statistics(df, ['methodvisibility', 'firstparametertype'], 10))
    print(get_statistics(df, ['methodvisibility', 'numberinnerclasses'], 10))
    print(get_statistics(df, ['methodvisibility', 'namingconvention'], 10))
    print(get_statistics(df, ['isconstructor', 'numberofoverloaded'], 10))
    print(get_statistics(df, ['isconstructor', 'numberannotations'], 10))
    print(get_statistics(df, ['isconstructor', 'numberstmts'], 10))
    print(get_statistics(df, ['isconstructor', 'numbergenerictypes'], 10))
    print(get_statistics(df, ['isconstructor', 'firstparametertype'], 10))
    print(get_statistics(df, ['isconstructor', 'numberthrows'], 10))
    print(get_statistics(df, ['isconstructor', 'methodlocalvars'], 10))
    print(get_statistics(df, ['isconstructor', 'numberparameters'], 10))
    print(get_statistics(df, ['isstatic', 'numberparameters'], 10))
    print(get_statistics(df, ['isabstract', 'numberparameters'], 10))
    print(get_statistics(df, ['numberparameters', 'numberstmts'], 10))
    print(get_statistics(df, ['numberparameters', 'methodlocalvars'], 10))

    # 3 FEATURES
    print("--- THREE FEATURES ---")
    print(get_statistics(df, ['methodvisibility', 'isstatic', 'isfinal'], 10))
    print(get_statistics(df, ['methodvisibility', 'isstatic', 'isabstract'], 10))
    print(get_statistics(df, ['methodvisibility', 'isstatic', 'returntype'], 10))
    print(get_statistics(df, ['methodvisibility', 'isabstract', 'returntype'], 10))
    print(get_statistics(df, ['methodvisibility', 'hasoverride', 'numberstmts'], 10))
    print(get_statistics(df, ['methodvisibility', 'hasoverride', 'numberparameters'], 10))
    print(get_statistics(df, ['methodvisibility', 'isconstructor', 'numberparameters'], 10))
    print(get_statistics(df, ['methodvisibility', 'isconstructor', 'firstparametertype'], 10))
    print(get_statistics(df, ['methodvisibility', 'firstparametertype', 'returntype'], 10))
    print(get_statistics(df, ['methodvisibility', 'firstparametertype', 'secondparametertype'], 10))
    print(get_statistics(df, ['methodvisibility', 'numberofoverloaded', 'numberstmts'], 10))
    print(get_statistics(df, ['isconstructor', 'firstparametertype', 'secondparametertype'], 10))
    print(get_statistics(df, ['isconstructor', 'numberofoverloaded', 'numberstmts'], 10))
    print(get_statistics(df, ['isconstructor', 'numberparameters', 'numberstmts'], 10))
    print(get_statistics(df, ['isstatic', 'firstparametertype', 'secondparametertype'], 10))
    print(get_statistics(df, ['isstatic', 'firstparametertype', 'returntype'], 10))
    print(get_statistics(df, ['isstatic', 'numberofoverloaded', 'numberstmts'], 10))
    print(get_statistics(df, ['isstatic', 'numberparameters', 'numberstmts'], 10))
    print(get_statistics(df, ['isabstract', 'firstparametertype', 'secondparametertype'], 10))
    print(get_statistics(df, ['isabstract', 'firstparametertype', 'returntype'], 10))
    print(get_statistics(df, ['isabstract', 'numberofoverloaded', 'numberstmts'], 10))
    print(get_statistics(df, ['isabstract', 'numberparameters', 'numberstmts'], 10))

    # 4 FEATURES
    print("--- FOUR FEATURES ---")
    print(get_statistics(df, ['methodvisibility', 'firstparametertype', 'secondparametertype', 'returntype'], 10))
    print(get_statistics(df, ['methodvisibility', 'firstparametertype', 'secondparametertype', 'thirdparametertype'], 10))
    print(get_statistics(df, ['methodvisibility', 'hasoverride', 'firstparametertype', 'returntype'], 10))
    print(get_statistics(df, ['methodvisibility', 'hasoverride', 'numberparameters', 'returntype'], 10))
    print(get_statistics(df, ['methodvisibility', 'numberofoverloaded', 'numberstmts', 'returntype'], 10))
    print(get_statistics(df, ['methodvisibility', 'numberparameters', 'numberstmts', 'returntype'], 10))
    print(get_statistics(df, ['methodvisibility', 'numberparameters', 'numberstmts', 'methodlocalvars'], 10))
    print(get_statistics(df, ['methodvisibility', 'isstatic', 'isfinal', 'isabstract'], 10))
    print(get_statistics(df, ['methodvisibility', 'isstatic', 'isabstract', 'returntype'], 10))
    print(get_statistics(df, ['isconstructor', 'firstparametertype', 'secondparametertype', 'thirdparametertype'], 10))
    print(get_statistics(df, ['isconstructor', 'numberparameters', 'numberstmts', 'methodlocalvars'], 10))
    print(get_statistics(df, ['isstatic', 'firstparametertype', 'secondparametertype', 'thirdparametertype'], 10))
    print(get_statistics(df, ['isabstract', 'firstparametertype', 'secondparametertype', 'thirdparametertype'], 10))
