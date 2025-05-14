import ast
import keyword
import token as TK
import tokenize

from io import BytesIO
from zipfile import ZipFile

from featureVector import FeatureVector

def read_zipFile(path):
    raw_codes = []
    
    archive = ZipFile(path, 'r')
    files = archive.namelist()
    
    for file in files:
        with archive.open(file) as file_content:
            content = file_content.read().decode('utf-8')
            raw_codes.append(content)
    
    return raw_codes
            
def normalization(raw_codes):
    normalized_codes = []

    for code in raw_codes:
        normalized_tokens = []

        byte_stream = BytesIO(code.encode('utf-8')).readline
        tokens = tokenize.tokenize(byte_stream)
        
        for token in tokens:
            if token.type == TK.NAME and not keyword.iskeyword(token.string):
                normalized_tokens.append(tokenize.TokenInfo(token.type, 'NAME', token.start, token.end, token.line))
            else:
                normalized_tokens.append(token)
        result = tokenize.untokenize(normalized_tokens).decode('utf-8')
        normalized_codes.append(result)

    return normalized_codes
    
def gen_tree(normalized_codes):
    asts_codes = []
    
    for code in normalized_codes:
        tree = ast.parse(code)
        asts_codes.append(tree)
    
    return asts_codes

def extract_features(asts_codes):
    feature_vectors = []
    
    for tree in asts_codes:
        extractor = FeatureVector()
        extractor.visit(tree)
        feature_vectors.append(extractor.features)
    
    return feature_vectors

def diff_features(feature_vectors):
    diff_vectors = []
    
    for i in range(len(feature_vectors)):
        for j in range(i + 1, len(feature_vectors)):
            fv1 = feature_vectors[i]
            fv2 = feature_vectors[j]
            
            keys = set(fv1.keys()).union(fv2.keys())
            
            diff = {key: abs(fv1.get(key, 0) - fv2.get(key, 0)) for key in keys}
            diff_vectors.append(diff)
    
    return diff_vectors

# MAIN
r_codes = read_zipFile('codes/add.zip')

n_codes = normalization(r_codes)

a_codes = gen_tree(n_codes)
# print(ast.dump(a_codes[0], indent=4))

f_vectors = extract_features(a_codes)
# print(f_vectors[0])

d_vectors = diff_features(f_vectors)
print(d_vectors)
