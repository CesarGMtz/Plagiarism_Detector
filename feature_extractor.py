import ast
from featureVector import FeatureVector

FIXED_KEYS = [
    'Assign', 'AugAssign', 'BinOp:+', 'BinOp:-', 'BinOp:*', 'BinOp:/', 'BinOp://', 'BinOp:%',
    'BoolOp:and', 'BoolOp:or',
    'Call', 'Cmp:==', 'Cmp:!=', 'Cmp:<', 'Cmp:<=', 'Cmp:>', 'Cmp:>=', 'Cmp:is', 'Cmp:is not', 'Cmp:in', 'Cmp:not in',
    'Dict', 'For', 'FunctionDef', 'If', 'IfElse', 'List', 'Name', 'Return', 'TotalArgs', 'Tuple', 'While',
    'FunctionDepth', 'NestedFunc', 'AvgFuncLength', 'NestedIf',
    'var_name_jaccard', 'var_name_overlap', 'var_name_diff',
    'lex_common_tokens', 'lex_total_tokens_1', 'lex_total_tokens_2', 'lex_jaccard', 'lex_token_ratio',
    'lex_ngram_sim',
    'line_length_diff', 'literal_overlap', 'literal_jaccard',
'token_edit_ratio', 'call_sequence_similarity', 'num_funcs_1', 'num_funcs_2', 'func_count_diff', 'func_line_ratio_1', 'func_line_ratio_2', 'func_line_ratio_diff',
"tokens_per_func_diff", 'control_flow_sim','func_name_sequence_similarity'




]
def get_feature_vector(file1, file2):
    with open(file1, "r", encoding="utf-8") as f1:
        code1 = f1.read()
    with open(file2, "r", encoding="utf-8") as f2:
        code2 = f2.read()

    extractor = FeatureVector(code1, code2)
    return extractor.extract()

def extract_features_from_pair(file1, file2):
    features = get_feature_vector(file1, file2)
    diff = {key: features.get(key, 0) for key in FIXED_KEYS}
    return diff
